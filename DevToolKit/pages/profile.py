import reflex as rx

@rx.page(route="/profile")
def profile():
    return rx.vstack(
        "hola profile"
    )