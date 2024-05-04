import reflex as rx

@rx.page(route="/home")
def home():
    return rx.vstack(
        rx.box(rx.input())
    )