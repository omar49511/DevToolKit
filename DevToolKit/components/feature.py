import reflex as rx
from DevToolKit.components.cards import card

def feature():
    return rx.section(
        rx.vstack(
            rx.heading("¿Por Qué Elegir DevHub?", as_="h2", margin_bottom="5rem"),
            rx.grid(
                card("bookmark.svg","Guarda y Organiza tus Herramientas Favoritas de Desarrollo en un Único Lugar."),
                card("current-location.svg","Accede Rápidamente a Tus Herramientas desde una Sola Página Web.","#1D161F"),
                card("trekking.svg", "Mejora Tu Productividad y Eficiencia en Tu Trabajo Diario de Programación."),
                columns="3",
                spacing="9",
                width="100%",
            ),
            gap="2rem"
        )
    )