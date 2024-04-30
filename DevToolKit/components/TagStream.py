import reflex as rx
from DevToolKit.components.marquee import marquee
def TagStream():
    return rx.section(
            rx.vstack(
                rx.heading("Explora Herramientas por Etiquetas", as_="h2"),
                marquee()
            )
        
        ),