import reflex as rx
import link_bio.utils as utils
import link_bio.constants as const
import link_bio.state.PageState as PageState # Importamos el estado de la página como 'PageState'
from link_bio.components.navbar import navbar # Importamos el componente de la barra de navegación
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.views.sponsors import sponsors
import link_bio.styles.styles as styles # Importamos el archivo de estilos como 'styles'
from link_bio.styles.styles import Size # Importamos la clase 'Size' como 'Size' y evitar escribir 'styles.Size' siempre
from link_bio.api.api import repo, live
from link_bio.state.PageState import PageState

@rx.page( # esto convierte todo el código siguiente en un página
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta,
    on_load=PageState.check_live # cuando la página esté cargada, se ejecutará el método 'check_live'
)

def index() -> rx.Component:
    return rx.box( # 'box' es un contenedor genérico para agrupar otros componentes        
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(                
                header(
                    live=PageState.is_live
                ),
                index_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH, # uso la constante 'MAX_WIDTH' del archivo de styles.py
                width="100%",
                margin_y=Size.BIG.value, # Ya no es necesario usar 'styles.Size'
                padding=Size.BIG.value
            )
        ),
        footer(),
    )