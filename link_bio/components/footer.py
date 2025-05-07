import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo_symbol.svg",
            width=Size.VERY_BIG.value,
            height=Size.VERY_BIG.value,
            alt="Logotipo de MoureDev. Una \"eme \" entre llaves",
        ),
        rx.link(
            f"2014-{datetime.date.today().year} MoureDev by Brais Moure v3.",
            href="https://mouredev.com",
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value,
                    alt="Icono de GitHub"
                ),
                rx.text(
                    "BUILDING SOFTWARE WITH FROM GALICIA TO THE WORLD.",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href=const.REPO_URL,
            is_external=True,
        ),
        
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing="0",
        color=TextColor.FOOTER.value,
        align_items="center"
    )