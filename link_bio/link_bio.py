import reflex as rx # type: ignore
from link_bio.pages.index import index # Importamos la página 'index' de index.py
import link_bio.styles.styles as styles
import link_bio.constants as const

# 'app': componente que va a generar una aplicación con Reflex
app = rx.App(
    stylesheets=styles.STYLESHEETS, # cargamos las fuentes que queremos
    style=styles.BASE_STYLE, # uso la constante 'BASE_STYLE' del archivo de styles.py
    head_components=[
        rx.script(
            # Todo esto para Google analytics
            src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
        rx.script(
            f"""
                window.dataLayer = window.dataLayer || [];
                function gtag(){{dataLayer.push(arguments);}}
                gtag('js', new Date());
                gtag('config', '{const.G_TAG}');
            """
        ),
    ],
)