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
