"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from DevToolKit.styles.styles import  BASE_STYLE

from DevToolKit.pages.tools import tools
from DevToolKit.pages.team import team
from DevToolKit.pages.register import register

# Create app instance and add index page.
app = rx.App(
    style = BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="teal",
    )
)

app.add_page(tools, route="/tools")
app.add_page(team, route="/team")
app.add_page(register, route="/register")
