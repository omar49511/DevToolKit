import reflex as rx
from DevToolKit.styles.styles import auth_pages_stylesheet
from DevToolKit.components.input_field import render_input_field
from DevToolKit.components.button import render_submit_button
from DevToolKit.states import State, LoginState
@rx.page(route="/login")
def login():
    return rx.vstack(
        rx.spacer(),
        rx.heading(
            "Inicia sesión 👍",
            size="8",
            transition="all 550ms ease",
        ),
        rx.text("inicia sesión abajo para acceder a tu cuenta"),
        rx.divider(width="15%"),
        render_input_field(
            title="Correo",
            is_password=False,
            value= LoginState.email,
            update= LoginState.update_email
        ),
        render_input_field(
            title="Contraseña",
            is_password=False,
            value= LoginState.password,
            update= LoginState.update_password
        ),
        render_submit_button(name="Login", event=State.void_event),
        rx.text(
            "No tienes una cuenta? Click ",
            rx.link("Aquí.", href="/register"),
        ),
        rx.spacer(),
        style=auth_pages_stylesheet
    )