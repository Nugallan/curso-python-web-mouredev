""" import reflex as rx
from link_bio.styles.colors import Color

# Botón flotante tomado de la librería ant design https://ant.design/components/float-button
class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton"
    icon = rx.Var[rx.el.Img] # creamos una variable anónima de tipo Imagen para usar en varias páginas
    href = rx.Var[str] # creamos una variable anónima de tipo String
    target = "_blank" # Abre el enlace en una pestaña nueva
    badge = {"dot": True, "color": Color.PRIMARY.value}

float_button = FloatButton.create # Crea un botón flotante """