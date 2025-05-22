import reflex as rx
import link_bio.constants as const
import datetime
from link_bio.styles.styles import Size, Spacing
from link_bio.styles.fonts import FontWeight
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.link_button import link_button
from link_bio.state.PageState import PageState
from link_bio.styles.colors import Color, TextColor

def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.cond(
                    PageState.live_status.live,
                    rx.link(
                        rx.image(
                            src="/icons/twitch.svg",
                            height=Size.DEFAULT.value,
                            width=Size.DEFAULT.value
                        ),
                        href=const.TWITCH_URL,
                        is_external=True,
                        class_name="blink",
                        border_radius="50%",
                        padding=Size.SMALL.value,
                        bg=Color.PURPLE.value,
                        position="absolute",
                        top=f"-{Size.DEFAULT.value}",
                        right=f"-{Size.DEFAULT.value}",
                        z_index="2"
                    )
                ),
                rx.avatar(
                    name="Brais Moure",
                    size=Spacing.MEDIUM_BIG.value,
                    src="/avatar.webp",
                    radius="none",
                    color=TextColor.HEADER.value,
                    bg=Color.CONTENT.value,
                    # style=styles.image_style,
                    alt="Avatar MoureDev"
                ),
                position="relative"
            ),
            rx.vstack(
                rx.heading(
                    "Brais Moure",
                    font_weight=FontWeight.BOLD.value,
                    size=Spacing.BIG.value
                ),
                rx.text(
                    "@mouredev",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "/icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "/icons/x.svg",
                        const.TWITTER_X_URL,
                        "Twitter/X"
                    ),
                    link_icon(
                        "/icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"
                    ),
                    link_icon(
                        "/icons/tiktok.svg",
                        const.TIKTOK_URL,
                        "TikTok"
                    ),
                    link_icon(
                        "/icons/facebook.svg",
                        const.FACEBOOK_URL,
                        "Facebook"
                    ),
                    # link_icon(
                    #     "/icons/spotify.svg",
                    #     const.SPOTIFY_URL,
                    #     "Spotify"
                    # ),
                    link_icon(
                        "/icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    spacing=Spacing.DEFAULT.value,
                    padding_top=Size.SMALL.value
                ),
                spacing=Spacing.ZERO.value,
                align_items="start"
            ),
            align="end",
            spacing=Spacing.DEFAULT.value
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text(
                        f"{experience()}+",
                        "años de experiencia"
                    ),
                    rx.spacer(),
                    info_text(
                        "150+", "aplicaciones creadas"
                    ),
                    rx.spacer(),
                    info_text(
                        "2.5M+", "seguidores"
                    ),
                    width="100%"
                ),
                rx.cond(
                    PageState.live_status.live,
                    link_button(
                        "En directo",
                        PageState.live_status.title,
                        "/icons/twitch.svg",
                        const.TWITCH_URL,
                        highlight_color=Color.PURPLE.value,
                        animated=True
                    ),
                    # rx.box(
                    #     rx.cond(
                    #         PageState.next_live,
                    #         link_button(
                    #             "Próximo directo",
                    #             PageState.next_live,
                    #             "/icons/twitch.svg",
                    #             const.TWITCH_URL,
                    #             highlight_color=Color.PURPLE.value,
                    #             animated=True
                    #         ),
                    #     ),
                    #     width="100%",
                    #     on_mount=PageState.check_schedule
                    # )
                ),
                rx.text(
                    f"""
                    Soy ingeniero de software freelance
                    fullstack especializado en desarrollo mobile, divulgador y creador de contenido formativo sobre programación.
                    Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!
                    """,
                    font_size=Size.DEFAULT.value,
                    color=TextColor.BODY.value
                ),
                width="100%",
                spacing=Spacing.BIG.value
            )
        ),
        width="100%",
        spacing=Spacing.BIG.value,
        align_items="start",
        on_mount=PageState.check_live # cuando la página esté cargada, se ejecutará el método 'check_live'
    )


def experience() -> int:
    return datetime.date.today().year - 2010