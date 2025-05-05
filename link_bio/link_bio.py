import reflex as rx # type: ignore
from link_bio.components.navbar import navbar # Importamos el componente de la barra de navegación
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.views.sponsors import sponsors
import link_bio.styles.styles as styles # Importamos el archivo de estilos como 'styles'
from link_bio.styles.styles import Size as Size # Importamos la clase 'Size' como 'Size' y evitar escribir 'styles.Size' siempre

# Obligatorio un class que sea un State, encargada de manejar los estados
class State(rx.State):
    pass
  
def index() -> rx.Component:
    return rx.box( # 'box' es un contenedor genérico para agrupar otros componentes
        navbar(),
        rx.center(
            rx.vstack(        
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH, # uso la constante 'MAX_WIDTH' del archivo de styles.py
                width="100%",
                margin_y=Size.BIG.value, # Ya no es necesario usar 'styles.Size'
                padding=Size.BIG.value
            )
        ),
        footer(),
    )

# 'app': componente que va a generar una aplicación con Reflex
app = rx.App(
    stylesheets=styles.STYLESHEETS, # cargamos las fuentes que queremos
    style=styles.BASE_STYLE, # uso la constante 'BASE_STYLE' del archivo de styles.py
)

app.add_page(
    index, # Añadimos la página
    title="MoureDev | Te enseño programación y desarrollo de Software",
    description="Hola, mi nombre es Brais Moure. Soy ingeniero de software, desarrollador freelance full-stack y divulgador.",
    image="avatar.webp"

) 

# app.compile() # DEPRECATED: ya no se usa el 'compile'