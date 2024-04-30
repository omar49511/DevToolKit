import reflex as rx

from DevToolKit.styles.styles import FONT_FAMILY


def hero():
    return rx.section(
        rx.hstack(
            rx.center(
                rx.vstack(
                    rx.heading("Dev Tools Central", as_="h1"), 
                    rx.text("Organiza y accede fácilmente a tus herramientas de desarrollo favoritas", font_family=FONT_FAMILY, font_size=20, color="#fff")
                ),
                align="center",
                justify="center",
            ),
            rx.image(src="fox.png", width="20em", height="auto"),
        ),
        background = "linear-gradient(0deg, rgb(16, 18, 17) 10%, rgba(58,58,62,1) 90%)"

    )