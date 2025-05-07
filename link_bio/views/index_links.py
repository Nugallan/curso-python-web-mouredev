import reflex as rx
import link_bio.constants as const
from link_bio.routes import Route
from link_bio.components.link_button import link_button # Importamos el componente 'link_button'
from link_bio.components.title import title 
from link_bio.styles.colors import Color

def index_links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
         "Cursos gratis",
         "Consulta mis tutoriales ppara aprender programación",
         "/icons/code.svg",
         Route.COURSES.value,
         is_external=False
        ),
        link_button("Twitch",
         "Directos de lunes a viernes",
         "/icons/twitch.svg",
         const.TWITCH_URL),
        link_button("Discord",
         "El chat de la comunidad",
         "/icons/discord.svg",
         const.DISCORD_URL),        
        link_button("YouTube",
         "Tutoriales semanales",
         "/icons/youtube.svg",
         const.YOUTUBE_URL),
        link_button("YouTube [canal secundario]",
         "Tutoriales semanales",
         "/icons/youtube.svg",
         const.YOUTUBE_SECONDARY_URL),

        link_button(
         "MoureDev",
         "Mi sitio web",
         "/icons/logo_symbol.svg",
         const.MOUREDEV_URL
        ),
        link_button(
         "Invítame a un café",
         "¿Quieres ayudarme a que siga creando contenido?",
         "/icons/coffee.svg",
         const.COFFEE_URL
        ),

        title("Contacto"),
        link_button(
         "MyPublicInbox",
         "Respuesta rápida y con preferencia",
         "/icons/checkmail.svg",
         const.MYPUBLICINBOX_URL
        ),
        link_button(
         "Email",
         const.EMAIL,
         "/icons/email.svg",
         f"mailto:{const.EMAIL}"
        ),
        
        width="100%",
        spacing="3"
    )