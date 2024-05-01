import reflex as rx
from DevToolKit.styles.styles import button_stylesheet

def render_submit_button(name: str, event: rx.State):
    return rx.hstack(
        rx.button(
            rx.text(name),
            color_scheme="#864e75",
            on_click=event,
            width="100%"
        ),
        style=button_stylesheet,
        padding= "0.5rem 0rem",
    )