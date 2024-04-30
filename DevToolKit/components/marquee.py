import reflex as rx
from typing import List

class Categories(rx.State):
    tags: List[str] = [
        "Iconos",
        "Imágenes",
        "Fuentes",
        "Artículos",
        "UI",
        "Desafíos",
        "Api`s",
        "Editores",
        "Gestión",
        "Documentación",
        "Colaboración",
        "Optimización de imágenes",
        "Creación de wireframes",
        "Extensiones de navegador",
        "Diseño web",
        "Desarrollo front-end",
        "Desarrollo back-end",
        "IA",
        "Herramientas de CSS",
        "Colores",
    ]

def tag(tags: str):
    return rx.text(tags, color="#fff", 
            as_="span", 
            bg="#121212",
            padding="1rem 2rem",
            borderRadius="10px",
            box_shadow="0px 5px 5px 0px rgb(0,0,0,0.5);",
        )
        
    

def marquee():
    return  rx.flex(
        rx.foreach(Categories.tags, tag),
        spacing="2",
        flex_wrap="wrap",
        width="100%",
    )