import reflex as rx
from DevToolKit.components.cards import card

def feature():
    return rx.section(
        rx.vstack(
            rx.heading("¿Por Qué Elegir DevHub?", as_="h2"),
            rx.hstack(
                card(),
                card(),
                card()      
            )
        )
    )