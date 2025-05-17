import reflex as rx
from link_bio.styles.styles import Size as Size, Spacing
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.link_button import link_button
from link_bio.styles.colors import Color, TextColor
import link_bio.constants as const
import datetime

def header(details = True, live=False, live_title="") -> rx.Component: # Añadimos 'details = True' para que por defecto aparezcan los detalles
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                rx.cond(
                    live, # si live es True entonces se muestra el badge
                    rx.link(
                        rx.badge(
                            rx.image(
                                src="/icons/twitch.svg"
                            ),
                            bg= Color.PURPLE.value,
                            border_color=Color.PURPLE.value,
                            class_name="blink" # para que el badge parpadee
                        ),
                        href=const.TWITCH_URL,
                        is_external=True
                    ),
                ),
                
                name="Brais Moure",
                size="8", #'size' sólo acepta numeración, nada de tallas 'xl' y demás
                src="/avatar.webp",
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
                    spacing=Spacing.DEFAULT.value
                ),
                rx.cond( # 'Cond' nos sirve para definir condiciones en Reflex
                details, # Si 'details' es verdadero, entonces muestra el contenido
                # lo que va después de la coma de 'details' es un else
                rx.flex(
                    info_text("13+", " años de experiencia"),
                    rx.spacer(),
                    info_text("100+", " aplicaciones creadas"),
                    rx.spacer(),
                    info_text("1M+", " seguidores"),
                    width="100%",
                ),
                rx.cond(  # Condicional anidado correctamente
                    live,
                    link_button(
                        "En directo",
                        live_title,
                        "/icons/twitch.svg",
                        const.TWITCH_URL,
                        highlight_color=Color.PURPLE.value  
                    ),
                    rx.text(
                        f""" Soy ingeniero de software freelance
                        fullstack especializado en desarrollo mobile, divulgador y creador de contenido formativo sobre programación.
                        Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!
                        """,
                        font_size=Size.DEFAULT.value,
                        color=TextColor.BODY.value
                    )
                )
            ),
                align_items="start",
                spacing="4",
            )
        ),
        
        width="100%",
        spacing=Spacing.BIG.value,
        align_items="start",
    )