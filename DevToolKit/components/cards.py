import reflex as rx

def card():
    return rx.box(
        rx.vstack(
            rx.box(
                rx.image(src="bookmark.svg", width="20em", height="auto"),
            ),
            rx.box(
                rx.text("Guarda y Organiza tus Herramientas Favoritas de Desarrollo en un Único Lugar."),
            ),
        )
    )