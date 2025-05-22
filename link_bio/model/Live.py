import reflex as rx
from pydantic import BaseModel

# Clase que se va a encargar de encapsular el modelo de una emisión en directo
class Live(BaseModel): # importante usar BaseModel que es una clase de pydantic V2 y no de reflex
    live: bool
    title: str