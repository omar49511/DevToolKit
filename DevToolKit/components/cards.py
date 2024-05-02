import reflex as rx

def card(image: str, text: str, color: str = "#16171C" ):
    return rx.box(
        rx.box(
            rx.image(src=image, width="5rem", height="auto", filter="invert(100%)"),
            background=color,
            border_radius="50%",
            padding="1rem",
            position="absolute",
            top="-3.5rem",
            box_shadow="0px 10px 10px 0px rgb(0,0,0,0.3);",
        ),
        rx.text(text, font_size="1.2rem"),
        display="flex",
        align_items="center",
        justify_content="center",
        background = "linear-gradient(0deg, #342B3F 10%, #151415 90%)",
        border_radius="0.5rem",
        box_shadow="0px 10px 10px 0px rgb(0,0,0,0.3);",
        height="15rem",
        padding="3rem",
        position="relative"
    )