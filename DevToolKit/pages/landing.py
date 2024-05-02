import reflex as rx
from DevToolKit.components.hero import hero 
from DevToolKit.components.feature import feature
from DevToolKit.components.overview import overview
from DevToolKit.components.TagStream import TagStream

@rx.page(route="/")
def landing():
    return rx.vstack(
            hero(),
            feature(),
            overview(),
            TagStream()
    ),