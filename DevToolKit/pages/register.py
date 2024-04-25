import reflex as rx

from DevToolKit.template import template

@template
def register() -> rx.Component:
    return rx.box(
            rx.box(
                rx.text("esta es la pagina del registro", background="#f00", padding="1em 2em", as_="span",),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
            background="radial-gradient(circle, rgba(0,0,0,0.80) 1px, transparent 1px)",
            background_size="25px 25px",
        )
