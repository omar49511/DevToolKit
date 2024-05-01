import reflex as rx
from DevToolKit.styles.styles import auth_pages_stylesheet
from DevToolKit.components.input_field import render_input_field
from DevToolKit.states import LoginState
@rx.page(route="/login")
def login():
    return rx.vstack(
        rx.spacer(),
        rx.heading(
            "Inicia sesión 👍",
            size="3",
            transition="all 550ms ease",
        ),
        rx.text("inicia sesión abajo para acceder a tu cuenta"),
        rx.divider(width="15%"),
        render_input_field(
            title="Email",
            is_password=False,
            value= LoginState.email,
            update= LoginState.update_email
        ),
        render_input_field(
            title="Email",
            is_password=False,
            value= LoginState.password,
            update= LoginState.update_password
        ),
        style=auth_pages_stylesheet
    )