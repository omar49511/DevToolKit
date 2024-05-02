import reflex as rx
from DevToolKit.states import State, RegisterState
from DevToolKit.components.input_field import render_input_field
from DevToolKit.styles.styles import auth_pages_stylesheet
from DevToolKit.components.button import render_submit_button


@rx.page(route="/register")
def register():
    return rx.vstack(
        rx.spacer(),
        rx.heading(
            "Registro",
            size="8",
            transition="all 550ms ease",
        ),
        rx.text("Crea una cuenta para comenzar"),
        rx.divider(width="15%"),
        render_input_field(
            title="Nombre de usuario",
            is_password=False,
            value= RegisterState.username,
            update= RegisterState.update_username
        ),
        render_input_field(
            title="Correo",
            is_password=False,
            value= RegisterState.email,
            update= RegisterState.update_email
        ),
        render_input_field(
            title="Contraseña",
            is_password=False,
            value= RegisterState.password,
            update= RegisterState.update_password
        ),
        render_submit_button(name="Login", event=State.void_event),
        rx.text(
            "Ya tienes una cuenta? Click ",
            rx.link("Aquí.", href="/login"),
        ),
        rx.spacer(),
        style=auth_pages_stylesheet
    )