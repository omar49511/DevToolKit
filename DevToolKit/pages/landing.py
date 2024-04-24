import reflex as rx
from DevToolKit.navigation import navbar




@rx.page(route="/")
def landing():
    return rx.vstack(
        navbar(heading="main"),
        rx.box(
            rx.text("Welcome to Reflex"),
        )
    )