import reflex as rx
from link_bio.api.api import live, featured

USER = "mouredev"

class PageState(rx.State): 
    
    is_live: bool
    live_title: str
    featured_info: list
    
    async def check_live(self): # buena práctica usar 'self' para tener contexto
        # self.is_live = await live(USER) # await para esperar a que se complete la función 'live'
        live_data = await live(USER)
        self.is_live = live_data["live"]
        self.live_live = live_data["title"]
        
    async def featured_links(self):
        self.featured_info = await featured()