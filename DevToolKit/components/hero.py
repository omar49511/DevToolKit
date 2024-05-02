import reflex as rx



def hero():
    return rx.section(
        rx.grid(
            rx.center(
                rx.vstack(
                    rx.heading("Dev Tools Central", as_="h1", font_family="Jolly Lodger", size="9", color="#D59650"), 
                    rx.text("Organiza y accede fácilmente a tus herramientas de desarrollo favoritas", font_size="2rem", color="#fff",)
                ),
            ),
            rx.box(
                rx.center(
                    rx.image(src="fox.png", width="20em", height="auto"),
                ),
            ),
            columns="2",
            padding="0 5rem",
        ),
        background = "linear-gradient(0deg, rgb(16, 18, 17) 10%, rgba(58,58,62,1) 90%)"

    )
