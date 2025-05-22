import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size, Spacing
from link_bio.styles.colors import Color, TextColor
# from link_bio.components.ant_components import float_button


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo_symbol.svg",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Logotipo de MoureDev. Una \"eme\" entre llaves."
        ),
        rx.link(
            rx.box(
                f"© 2014-{datetime.date.today().year} ",
                rx.text(
                    "MoureDev by Brais Moure",
                    as_="span",
                    color=Color.PRIMARY.value
                ),
                " v5.",
                padding_top=Size.DEFAULT.value
            ),
            href=const.MOUREDEV_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value,
                    alt="Logo GitHub"
                ),
                rx.text(
                    "Building software with ♥ from Galicia to the world.",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                )
            ),
            href=const.REPO_URL,
            is_external=True
        ),
        rx.text(
            "Con el apoyo de",
            rx.image(
                src=f"/raiola_networks.svg",
                on_click=rx.redirect(
                    const.RAIOLA_NETWORKS_URL,
                    is_external=True
                ),
                width="200px",
                height="100%",
                cursor="pointer",
                padding_x=Size.MEDIUM.value,
                alt="Logo Raiola Networks"
            ),
            font_size=Size.MEDIUM.value,
            display="flex",
            align_items="center"
        ),
        # Se deja de utilizar hasta que se actualice la versión de next.js
        # float_button(
        #     icon=rx.image(src="/icons/donate.svg"),
        #     href=const.COFFEE_URL
        # ),
        align="center",
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        color=TextColor.FOOTER.value
    )