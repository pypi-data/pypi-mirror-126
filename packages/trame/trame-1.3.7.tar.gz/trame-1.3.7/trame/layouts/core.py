from genericpath import exists
import os
from pywebvue.utils import read_file_as_base64_url
from trame.html import Span, vuetify
from trame import base_directory, get_app_instance

import pywebvue
import trame

LOGO_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../html/assets/logo.svg")
)


class FullScreenPage:
    def __init__(self, name, favicon=None, on_ready=None):
        self.name = name
        self.favicon = None
        if os.path.exists(LOGO_PATH):
            self.favicon = read_file_as_base64_url(LOGO_PATH)
        self.on_ready = on_ready
        self._app = vuetify.VApp(id="app")
        self.children = self._app.children
        self._current_root = self._app

        if favicon:
            file_path = os.path.join(base_directory(), favicon)
            if os.path.exists(file_path):
                self.favicon = file_path
            else:
                print(f"Invalid path to favicon: {file_path}")

    @property
    def root(self):
        return self._current_root

    @root.setter
    def root(self, new_root):
        if new_root and self._current_root != new_root:
            new_root.children += [self._current_root]
            self._current_root = new_root

    @property
    def html(self):
        return self.root.html

    @property
    def state(self):
        return get_app_instance().state

    @state.setter
    def state(self, value):
        get_app_instance().state.update(value)


class SinglePage(FullScreenPage):
    def __init__(self, name):
        super().__init__(name)
        self.toolbar = vuetify.VAppBar(app=True)
        if os.path.exists(LOGO_PATH):
            self.logo = Span(
                f'<img height="32px" width="32px" src="{read_file_as_base64_url(LOGO_PATH)}" />',
                classes="mr-2",
                style="display: flex; align-content: center;",
            )
        else:
            self.logo = vuetify.VIcon("mdi-menu", classes="mr-4")
        self.title = Span("Trame App", classes="title")
        self.content = vuetify.VMain()
        self.toolbar.children += [self.logo, self.title]
        self.footer = vuetify.VFooter(
            app=True,
            classes="my-0 py-0",
            children=[
                vuetify.VProgressCircular(
                    indeterminate=("busy",),
                    background_opacity=1,
                    bg_color="#01549b",
                    color="#04a94d",
                    size=16,
                    width=3,
                    classes="ml-n3 mr-1",
                ),
                f'<a href="https://kitware.github.io/trame/" class="grey--text lighten-1--text text-caption text-decoration-none" target="_blank">Powered by Trame {trame.__version__}/{pywebvue.__version__}</a>',
                vuetify.VSpacer(),
                '<a href="https://www.kitware.com/" class="grey--text lighten-1--text text-caption text-decoration-none" target="_blank">© 2021 Kitware Inc.</a>',
                # vuetify.VProgressLinear(
                #     active=("busy",),
                #     indeterminate=True,
                #     absolute=True,
                #     bottom=True,
                #     striped=True,
                #     background_opacity=1,
                #     color="#01549b",
                #     background_color="#04a94d",
                #     height=4,
                # ),
            ],
        )
        self._app.children += [self.toolbar, self.content, self.footer]


class SinglePageWithDrawer(SinglePage):
    def __init__(
        self, name, show_drawer=True, width=200, show_drawer_name="drawerOpen"
    ):
        super().__init__(name)
        self.drawer = vuetify.VNavigationDrawer(
            app=True,
            clipped=True,
            stateless=True,
            v_model=(show_drawer_name, show_drawer),
            width=width,
        )
        self.toolbar.clipped_left = True
        self._app.children += [self.drawer]
        self.logo.click = f"{show_drawer_name} = !{show_drawer_name}"
