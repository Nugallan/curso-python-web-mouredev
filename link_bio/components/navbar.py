import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color

def navbar() -> rx.Component:
    # Componente de barra de navegación con 'hstack' (Horizontal Stack)
    return rx.hstack( # Hay que introducir 'return' para que funcione
        rx.hstack(
            rx.text("moure", color=Color.PRIMARY.value),
            rx.text("dev", color=Color.SECONDARY.value),
            font_family="Comfortaa-Medium",
            spacing="0"
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0" # Indica que el tamaño de la parte superior es 0
    )