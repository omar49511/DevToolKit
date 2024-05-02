import reflex as rx
from DevToolKit.styles.styles import input_stylesheet

def render_input_field(
    title: str,
    is_password: bool,
    value: rx.Var,
    update: rx.State,
):
    return rx.vstack(
        rx.text(title),
        rx.chakra.input(
            value=value,
            on_change=update,
            type="password" if is_password else "text",
            width="100%",
            size='lg',
            height="2.5rem",
            box_shadow="0px 4px 4px 0px rgb(0,0,0,0.3);",
            background_color="#18181B",
            padding="1rem",
        ),
        style=input_stylesheet,
        spacing="2"
    )
# pasar estos estilos a el archivo de estilos