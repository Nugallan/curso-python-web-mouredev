import reflex as rx
from link_bio.api.api import live

USER = "mouredev"

class PageState(rx.State): 
    
    is_live: bool
    
    async def check_live(self): # buena práctica usar 'self' para tener contexto
        # self.is_live = await live(USER) # await para esperar a que se complete la función 'live'
        self.is_live = await live(USER)