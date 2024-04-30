import reflex as rx

def overview():
    return rx.section(
        rx.vstack(
            rx.heading("Herramientas para Todos los Aspectos del Desarrollo", as_="h2"),
            rx.hstack( 
                rx.text(
                    "¡Descubre y comparte nuestras herramientas seleccionadas! ¡Eleva tu desarrollo y maximiza tu potencial!",
                    as_="p",
                ),
                rx.video(
                    url="https://www.youtube.com/embed/9bZkp7q19f0",
                    width="400px",
                    height="auto",
                ),
            )
        )
    )