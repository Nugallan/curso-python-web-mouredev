# Botón especial para nuestra app
import reflex as rx
import link_bio.styles.styles as styles # Importamos el archivo de estilos
from link_bio.styles.colors import Color
from link_bio.styles.styles import Size as Size

def link_button(title: str, body: str, image: str, url: str, is_external=True, highlight_color=None) -> rx.Component: # los argumentos 'title' y 'body' para personalizar cada button (Uno contendrá texto "Twitch", otro "YouTube", etc)
    return rx.link( # 'link' para enlaces web
        rx.button(
           rx.hstack(
               rx.image(
                   src=image,
                   width=Size.LARGE.value,
                   height=Size.LARGE.value,
                   margin=Size.MEDIUM.value,
                   alt=title
               ),
               rx.vstack(
                rx.text(title, style=styles.button_title_style), # 'text' para escribir el texto del botón y 'style' para personalizarlo
                rx.text(body, style=styles.button_body_style),
                align_items="start",
                spacing="0",
                padding_y=Size.SMALL.value,
                padding_right=Size.SMALL.value
               ),
               align="center",
               width="100%"
           ),
           border_color=highlight_color,
           border_width="2px" if highlight_color != None else None
        ),
        background_color=Color.PRIMARY.value,
        href=url, # link para enlace y tiene como propiedad 'url
        is_external=is_external, # abre el enlace en una pestaña nueva
        width="100%",
        text_decoration="none"
    )