import types
from trame import get_app_instance, trigger_key


def str_key_prefix(txt):
    if txt.startswith("{") or txt.startswith("`"):
        return ":"

    return ""


def py2js_key(key):
    return key.replace("_", "-")


class ElementContextManager:
    def __init__(self):
        self.element_stack = []

    def enter(self, elem):
        self.element_stack.append(elem)

    def exit(self, elem):
        if len(self.element_stack) and elem == self.element_stack[-1]:
            self.element_stack.pop()

    def add_child(self, elem):
        if len(self.element_stack):
            self.element_stack[-1].add_child(elem)


HTML_CTX = ElementContextManager()


class AbstractElement:
    """
    A Vue component which can integrate with the rest of Trame. See Vue docs |vue_doc_link| for more info.

    .. |vue_doc_link| raw:: html

        <a href="https://vuejs.org/v2/guide/instance.html" target="_blank">here</a>

    :param name: The name of the element, like 'div' for a ``<div/>`` element.
    :type name: str
    :param children: The children nested within this element
    :type children: None | str | list[trame.html.*] | trame.html.*
    :param __properties: Add more attributes to this element
    :param __events: Add more events to this element

    Html attributes

    :param id:
    :param classes:
    :param style:

    Vue attributes

    :param ref:
    :param v_model:
    :param v_if:
    :param v_show:
    :param v_for:
    :param key:

    Events

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    _next_id = 1

    def __init__(self, name, children=None, **kwargs):
        AbstractElement._next_id += 1
        self._id = AbstractElement._next_id
        self._elem_name = name
        self._allowed_keys = set()
        self._attr_names = kwargs.get("__properties", [])
        self._event_names = kwargs.get("__events", [])

        self._attributes = {}
        self._py_attr = kwargs
        self._children = []

        if children:
            if isinstance(children, list):
                self._children.extend(children)
            else:
                self._children.append(children)

        # Add standard Vue attr/event handling
        self._attr_names += [
            "id",
            "ref",
            ("classes", "class"),
            "style",
            "v_model",
            "v_if",
            "v_show",
            "v_for",
            ("key", ":key"),
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]

        # Add ourself to context is any
        HTML_CTX.add_child(self)

    def _attr_str(self):
        return " ".join(self._attributes.values())

    def _update_allowed_keys(self):
        if hasattr(self, "_attr_names") and hasattr(self, "_event_names"):
            for items in [self._attr_names, self._event_names]:
                for item in items:
                    if isinstance(item, str):
                        self._allowed_keys.add(item)
                    else:
                        self._allowed_keys.add(item[0])

    # -------------------------------------------------------------------------
    # Buildin API
    # -------------------------------------------------------------------------

    def __getitem__(self, name):
        return self._py_attr[name]

    def __setitem__(self, name, value):
        if name in self._allowed_keys:
            self._py_attr[name] = value
        else:
            print(f"Attribute {name} is not defined for {self._elem_name}")

    def __getattr__(self, name):
        if name[0] == "_":
            raise AttributeError()

        return self._py_attr[name]

    def __setattr__(self, name, value):
        if name[0] == "_":
            self.__dict__[name] = value
        elif name == "children":
            self._children = value
        elif name in self._allowed_keys:
            self._py_attr[name] = value
        else:
            self.__dict__[name] = value

        if name in ["_attr_names", "_event_names"]:
            self._update_allowed_keys()

    # -------------------------------------------------------------------------
    # helpers
    # -------------------------------------------------------------------------

    def ttsSensitive(self):
        """
        Set this element to be reactive to a global timestamp.
        """
        self._attributes["__tts"] = f':key="`w{self._id}-${{tts}}`"'
        return self

    def attrs(self, *names):
        _app = get_app_instance()
        for _name in names:
            js_key = None
            name = _name
            if isinstance(_name, tuple):
                name = _name[0]
                js_key = _name[1]

            if name in self._py_attr:
                if js_key is None:
                    js_key = py2js_key(name)
                value = self._py_attr[name]

                if value is None:
                    continue

                if (
                    _app._debug
                    and js_key.startswith("v-")
                    and not isinstance(value, (tuple, list))
                ):
                    print(
                        f'Warning: A Vue directive is evaluating your expression and Trame would expect a tuple instead of a plain type. <{self._elem_name} {js_key}="{value}" ... />'
                    )

                if isinstance(value, (tuple, list)):
                    if len(value) > 1 and value[0] not in _app.state:
                        _app.state[value[0]] = value[1]

                    if js_key.startswith("v-"):
                        self._attributes[name] = f'{js_key}="{value[0]}"'
                    elif js_key.startswith(":"):
                        self._attributes[name] = f'{js_key}="{value[0]}"'
                    else:
                        self._attributes[name] = f':{js_key}="{value[0]}"'
                elif isinstance(value, bool):
                    if value:
                        self._attributes[name] = js_key
                elif isinstance(value, (str, int, float)):
                    self._attributes[name] = f'{js_key}="{value}"'
                else:
                    print(
                        f"Error: Don't know how to handle attribue name '{name}' with value '{value}' in {self.__class__}::{self._elem_name}"
                    )

        return self

    def events(self, *names):
        _app = get_app_instance()
        for _name in names:
            js_key = None
            name = _name
            if isinstance(_name, tuple):
                name = _name[0]
                js_key = _name[1]
            if name in self._py_attr:
                if js_key is None:
                    js_key = py2js_key(name)
                js_key = f"@{js_key}"
                value = self._py_attr[name]

                if value is None:
                    continue

                if isinstance(value, str):
                    self._attributes[name] = f'{js_key}="{value}"'
                elif isinstance(value, (types.FunctionType, types.MethodType)):
                    trigger_name = trigger_key(value)
                    self._attributes[name] = f"{js_key}=\"trigger('{trigger_name}')\""
                elif isinstance(value, tuple):
                    trigger_name = value[0]
                    if isinstance(trigger_name, (types.FunctionType, types.MethodType)):
                        trigger_name = trigger_key(trigger_name)
                    if len(value) == 1:
                        self._attributes[
                            name
                        ] = f"{js_key}=\"trigger('{trigger_name}')\""
                    if len(value) == 2:
                        self._attributes[
                            name
                        ] = f"{js_key}=\"trigger('{trigger_name}', {value[1]})\""
                    if len(value) == 3:
                        self._attributes[
                            name
                        ] = f"{js_key}=\"trigger('{trigger_name}', {value[1]}, {value[2]})\""
                else:
                    print(
                        f"Error: Don't know how to handle event name '{name}' with value '{value}' in {self.__class__}::{self._elem_name}"
                    )
        return self

    def clear(self):
        """
        Remove all children
        """
        self._children.clear()

    def hide(self):
        """
        Hide element while keeping it in the DOM.
        """
        self._attributes["__style"] = 'style="display: none"'

    def add_child(self, child):
        self._children.append(child)

    def add_children(self, children):
        self._children += children

    @property
    def children(self):
        return self._children

    def set_text(self, value):
        self.clear()
        self._children.append(value)

    @property
    def html(self):
        """
        A string representation of the HTML component.
        """
        # Build attributes
        self.attrs(*self._attr_names)
        self.events(*self._event_names)

        # Compute HTML str
        if len(self._children):
            out_buffer = []
            out_buffer.append(f"<{self._elem_name} {self._attr_str()}>")
            for child in self._children:
                if isinstance(child, str):
                    out_buffer.append(child)
                else:
                    out_buffer.append(child.html)
            out_buffer.append(f"</{self._elem_name}>")
            return "\n".join(out_buffer)
        else:
            return f"<{self._elem_name} {self._attr_str()} />"

    # -------------------------------------------------------------------------
    # Resource manager
    # -------------------------------------------------------------------------

    def __enter__(self):
        HTML_CTX.enter(self)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        HTML_CTX.exit(self)


class Element(AbstractElement):
    """
    Any html element you would like to use in Trame.

    :param _elem_name: The name of the element, like 'div' for a ``<div/>`` element.
    :type _elem_name: str
    :param children: The children nested within this element
    :type children: None | str | list[trame.html.*] | trame.html.*
    """

    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)


class Div(AbstractElement):
    """
    The standard html content division element.

    :param children: The children nested within this element
    :type children: None | str | list[trame.html.*] | trame.html.*
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("div", children, **kwargs)


class Span(AbstractElement):
    """
    The standard html content span element.

    :param children: The children nested within this element
    :type children: None | str | list[trame.html.*] | trame.html.*
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("span", children, **kwargs)


class Form(AbstractElement):
    """
    The standard html form element.

    :param children: The children nested within this element
    :type children: None | str | list[trame.html.*] | trame.html.*
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("form", children, **kwargs)
        self._attr_names += ["action"]


class Label(AbstractElement):
    """
    The standard html input label element.

    :param children: The children nested within this element
    :type children: None | str | list[trame.html.*] | trame.html.*
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("label", children, **kwargs)


class Input(AbstractElement):
    """
    The standard html input (form input) element.

    :param children: The children nested within this element
    :type children: None | str | list[trame.html.*] | trame.html.*
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("input", children, **kwargs)
        self._attr_names += [
            "type",
            "value",
            "name",
            "size",
            "min",
            "max",
            "step",
            "maxlength",
            "disabled",
            "readonly",
            "multiple",
            "pattern",
            "placeholder",
            "required",
            "autofocus",
            "src",
            "width",
            "height",
            "alt",
            "list",
            "autocomplete",
        ]


class Template(AbstractElement):
    """
    The standard html content template element.

    :param children: The children nested within this element
    :type children: None | str | list[trame.html.*] | trame.html.*
    """

    slot_names = set()

    def __init__(self, children=None, **kwargs):
        super().__init__("template", children, **kwargs)
        self._attr_names += ["v_slot"]
        for slot_name in Template.slot_names:
            safe_name = slot_name.replace("-", "_").replace(".", "_")
            if "<name>" in safe_name:
                safe_header, safe_tail = safe_name.split("<name>")
                header, tail = slot_name.split("<name>")
                for key in kwargs:
                    if key.startswith(header):
                        dyna_name = key[len(header) : -len(tail)]
                        self._attr_names.append(
                            (
                                f"v_slot_{safe_header}{dyna_name}{safe_tail}",
                                f"v-slot:{header}{dyna_name}{tail}",
                            )
                        )
            else:
                self._attr_names.append((f"v_slot_{safe_name}", f"v-slot:{slot_name}"))


class StateUpdate(AbstractElement):
    """
    Component to display part of the state

    :param name: Which part of the state to display.
    :type name: str

    Events

    :param change: Function to run if state changes
    :type change: function
    """

    def __init__(self, name, **kwargs):
        super().__init__("py-state-update", **kwargs)
        self._attributes["value"] = f':value="{name}"'
        self._event_names += [
            "change",
        ]


class Triggers(AbstractElement):
    """
    Component to trigger JS actions from Python.

    :param ref:
    :param triggers:
    :type triggers: dict[str, str]
    """

    def __init__(self, ref, triggers={}, **kwargs):
        super().__init__("py-trigger", **kwargs)
        self._ref = ref
        self._attributes["ref"] = f'ref="{ref}"'
        for key, value in triggers.items():
            self._attributes[f"_{key}"] = f'@{key}="{value}"'

    def add(self, name, call):
        """
        Add a trigger which can call JS from Python.

        :param name: Reference for this JS expression trigger
        :type name: str
        :param call: JS expression to call when triggered
        :type call: str
        """
        self._attributes[f"_{name}"] = f'@{name}="{call}"'

    def call(self, name, *args):
        _app = get_app_instance()
        _app.update(ref=self._ref, method="emit", args=[name, *args])
