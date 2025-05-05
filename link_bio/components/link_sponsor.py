import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def link_sponsor(imagen: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            height="3.5em",
            width="auto", # para que las imágenes guarden la proporción en resopnsive
            alt=alt
        ),
        href=url,
        is_external=True
    )