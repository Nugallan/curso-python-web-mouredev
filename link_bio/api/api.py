import link_bio.constants as const
from .TwitchAPI import TwitchAPI # importamos el fichero de TwitchAPI
from .SupabaseAPI import SupabaseAPI

TWITCH_API = TwitchAPI()
SUPABASE_API = SupabaseAPI()

async def repo() -> str: # recomendable introducir siempre 'async'
    return const.REPO_URL

async def live(user: str) -> dict:
    return TWITCH_API.live(user)

async def featured() -> list:
    return SUPABASE_API.featured() # llamamos a la función de featured() de SupabaseAPI