import reflex as rx

@rx.page(route="/home")
def home():
    return rx.vstack(
        "hola"
    )