import reflex as rx

from DevToolKit.navigation import navbar
from DevToolKit.template import template

@template
def register() -> rx.Component:
    return rx.box(
            navbar(heading="register"),
            rx.box(
                rx.text("esta es la pagina del registro"),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        )
