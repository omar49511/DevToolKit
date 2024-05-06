import reflex as rx
from DevToolKit.components.hero import hero 
from DevToolKit.components.feature import feature
from DevToolKit.components.overview import overview
from DevToolKit.components.TagStream import TagStream
from DevToolKit.components.navbar.navbar import navbar
@rx.page(route="/")
def landing():
    return rx.vstack(
        navbar(sidebar=""),
        hero(),
        overview(),
        feature(),
        TagStream()
    ),