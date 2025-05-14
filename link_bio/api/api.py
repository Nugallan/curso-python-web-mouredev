import link_bio.constants as const
from .TwitchAPI import TwitchAPI # importamos el fichero de TwitchAPI

TWITCH_API = TwitchAPI()

async def repo() -> str: # recomendable introducir siempre 'async'
    return const.REPO_URL

async def live(user: str) -> bool:
    return TWITCH_API.is_live(user)