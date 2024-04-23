"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from DevToolKit.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from DevToolKit.pages.tools import tools
from DevToolKit.pages.team import team
from DevToolKit.pages.index import index
from DevToolKit.pages.register import register

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(tools, route="/tools")
app.add_page(team, route="/team")
app.add_page(register, route="/register")
