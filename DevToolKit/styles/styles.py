"""The style classes and constants for the Dashboard App."""

from reflex.components.radix import themes as rx
from .colors import  TextColors

BASE_STYLE = {
    "color": TextColors.TEXT.value,
    "width":"100%",
    "display": "flex",
    "flex_direction": "column",
    "align_items": "center",
    "justify_content": "center",
}

STYLESHEETS = ["https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap"]

FONT_FAMILY = "Share Tech Mono"
BACKGROUND_COLOR = "#000000"


general_stylesheet: dict={
    "width": ["100%", "100%", "70%", "50%", "35%"],
    "padding": ["0rem 2rem"],
    "transition": "all 550ms ease",
    "display": "flex",
    "justify_content": "center",
    "align_items": "start",
}

input_stylesheet: dict={
    **general_stylesheet,
}

button_stylesheet: dict={
    **general_stylesheet,
    "height": "45px"
}

auth_pages_stylesheet: dict={
    "width": "100%",
    "height": "100vh",
    "display": "flex",
    "justify_content": "start",
    "align_items": "center",
}