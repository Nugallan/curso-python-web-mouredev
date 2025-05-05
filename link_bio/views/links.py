import reflex as rx
import link_bio.constants as const
from link_bio.components.link_button import link_button # Importamos el componente 'link_button'
from link_bio.components.title import title 
from link_bio.styles.colors import Color

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Twitch",
         "Directos de lunes a viernes",
         "icons/twitch.svg",
         const.TWITCH_URL),
        link_button("YouTube",
         "Tutoriales semanales",
         "icons/twitch.svg",
         const.YOUTUBE_URL),
        link_button("YouTube (canal secundario)",
         "Tutoriales semanales",
         "icons/twitch.svg",
         const.YOUTUBE_SECONDARY_URL),
        link_button("Discord",
         "El chat de la comunidad",
         "icons/twitch.svg",
         const.DISCORD_URL),

        link_button(
         "MoureDev",
         "¿Mi sitio web?",
         "icons/twitch.svg",
         const.MOUREDEV_URL
        ),
        link_button(
         "Invítame a un café",
         "¿Quieres ayudarme a que siga creando contenido?",
         "icons/twitch.svg",
         const.COFFEE_URL
        ),

        title("Contacto"),
        link_button(
         "MyPublicInbox",
         "Respuesta rápida y con preferencia",
         "icons/twitch.svg",
         const.MYPUBLICINBOX_URL
        ),
        link_button(
         "Email",
         const.EMAIL,
         "icons/twitch.svg",
         f"mailto:{const.EMAIL}"
        ),
        
        width="100%",
        spacing="3"
    )