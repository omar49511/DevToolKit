import reflex as rx
from DevToolKit.styles.styles import button_stylesheet

def render_submit_button(name: str, event: rx.State):
    return rx.hstack(
        rx.button(
            rx.text(name),
            color_scheme="purple",
            on_click=event,
            width="100%",
            height="100%"
        ),
        style=button_stylesheet,
        padding= "1rem 0rem",
    )