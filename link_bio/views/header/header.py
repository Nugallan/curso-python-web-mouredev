import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.colors import Color, TextColor
import link_bio.constants as const
import datetime

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Brais Moure",
                size="8", #'size' sólo acepta numeración, nada de tallas 'xl' y demás
                src="avatar.webp",
                color=TextColor.HEADER.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px solid",
                border_color=Color.PRIMARY.value
            ), 
            rx.vstack(
                rx.heading(
                    "Brais Moure",
                    size="8",
                ),
                rx.text(
                    "@mouredev",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "icons/twitch.svg",
                        const.GITHUB_URL,
                        "Twitch",
                    ),
                    link_icon(
                        "icons/twitch.svg",
                        const.TWITTER_X_URL,
                        "Twitter",
                    ),
                    link_icon(
                        "icons/twitch.svg",
                        const.INSTAGRAM_URL,
                        "Instagram",
                    ),
                    link_icon(
                        "icons/twitch.svg",
                        const.TIKTOK_URL,
                        "TikTok",
                    ),
                    link_icon(
                        "icons/twitch.svg",
                        const.FACEBOOK_URL,
                        "Facebook",
                    ),
                    link_icon(
                        "icons/twitch.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn",
                    ),
                    spacing="5"
                ),
                align_items="start",
                spacing="4",
            )
        ),
        rx.flex(
            info_text("13+", " años de experiencia"),
            rx.spacer(),
            info_text("100+", " aplicaciones creadas"),
            rx.spacer(),
            info_text("1M+", " seguidores"),
            width="100%",
            align_items="center"
        ),
        
        rx.text(
                f""" Soy ingeniero de software freelance
                fullstack especializado en desarrollo mobile, divulgador y creador de contenido formativo sobre programación.
                Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!
                """,
                font_size=Size.MEDIUM.value,
                color=TextColor.BODY.value
        ),
        spacing="6",
        align_items="start",
    )