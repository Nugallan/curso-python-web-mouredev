import reflex as rx
from enum import Enum # Importamos la clase 'Enum' de python
from .colors import Color as Color # Importamos la clase 'Color' y lo nombramos como 'Color'
from .colors import TextColor as TextColor
from .fonts import Font, FontWeight # Importamos la clase 'Font' y lo nombramos como 'Font'

# Constantes
MAX_WIDTH = "560px"

STYLESHEETS = {
    # Buscando en google "load google font in css" en la API de Google fonts nos indica la URL para las fuentes
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap", # cargamos las 2 fuentes que queremos por 'wght@300;500&display=swap'
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
}

# Sizes (tamaños)
class Size(Enum): # encapsulamos los espaciadores de la página
    ZERO = "0px !important"
    SMALL="0.5em" # 'em' tamaño relativo para diseño responsive
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em",
    VERY_BIG="4em"
    
# Styles
BASE_STYLE = {
    "font-family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_weight": FontWeight.MEDIUM.value,
        "font_family": Font.TITLE.value
    },
    rx.button: { # Definimos un mapa de propiedades comunes para el botón
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "_background_color": Color.CONTENT.value,
        "white_space": "normal", # Hace truncado de textos y salta a nueva línea
        "text_align": "start",
        "hover": {
            "_background_color": Color.SECONDARY.value
        }
    },
    rx.link: { # Redefino los estilos genéricos de los enlaces
        "text_decoration": "none",
        "_hover": {} # Para eliminar el subrayado de enlaces
    }

}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    width="100%",
    size="8",
    padding_top=Size.DEFAULT.value,
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.BODY.value
)