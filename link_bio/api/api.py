import link_bio.constants as const
from link_bio.model.Featured import Featured
from link_bio.model.Live import Live
from .TwitchAPI import TwitchAPI # importamos el fichero de TwitchAPI
from .SupabaseAPI import SupabaseAPI
from .ConfigCatAPI import ConfigCatAPI

TWITCH_API = TwitchAPI()
SUPABASE_API = SupabaseAPI()
CONFIGCAT_API = ConfigCatAPI()

async def repo() -> str: # recomendable introducir siempre 'async'
    return const.REPO_URL

async def live(user: str) -> Live: # Devuelve el objeto 'Live'
    return TWITCH_API.live(user)

async def featured() -> list[Featured]:
    return SUPABASE_API.featured() # llamamos a la función de featured() de SupabaseAPI

async def schedule() -> dict: # Devuelve el schedule de la app de ConfigCat
    return CONFIGCAT_API.schedule()