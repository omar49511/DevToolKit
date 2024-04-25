import reflex as rx
from DevToolKit.components.hero import hero 

@rx.page(route="/")
def landing():
    return rx.vstack(
        rx.box(
            rx.center(
                hero(),
            ),
            width="100%",
        ),
    )