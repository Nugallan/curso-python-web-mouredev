import reflex as rx
import link_bio.constants as const
from link_bio.routes import Route
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color
# from link_bio.components.ant_components import float_button # importamos el FloatButton de 'ant_components.py'

def navbar() -> rx.Component:
    # Componente de barra de navegación con 'hstack' (Horizontal Stack)
    return rx.hstack( # Hay que introducir 'return' para que funcione
        rx.link(
            rx.hstack(
                rx.text("moure", color=Color.PRIMARY.value),
                rx.text("dev", color=Color.SECONDARY.value),
            ),
            href=Route.INDEX.value      
        ),
#     float_button(
#             icon = rx.image(src="/icons/donate.svg"),
#             href = const.COFFEE_URL
#        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0" # Indica que el tamaño de la parte superior es 0
    )