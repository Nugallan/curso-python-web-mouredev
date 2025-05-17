import os
import reflex as rx # type: ignore
import link_bio.styles.styles as styles
import link_bio.constants as const
from link_bio.pages.index import index # Importamos la página 'index' de index.py
from link_bio.pages.courses import courses
from fastapi import FastAPI # Importamos la API de FastAPI para trabajar con APIs
from link_bio.api.api import repo, live
from fastapi.middleware.cors import CORSMiddleware # Importamos el middleware de CORS para permitir peticiones desde otros dominios

os.environ["REFLEX_ALLOWED_ORIGINS"] = "http://localhost:3000"

# Creación de instancia de FastAPI
fastapi_app = FastAPI()
fastapi_app.add_middleware(
    CORSMiddleware, # permite peticiones desde otros dominios
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)

fastapi_app.add_api_route("/repo", repo) # añade la ruta '/repo' a la API
fastapi_app.add_api_route("/live/{user}", live)

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
            """),
    ],
    api_transformer=fastapi_app # Asignamos la instancia de la API a nuestra app
    
)

# app.api.add_api_route("/hello", hello) # Deprecated (obsoleto)