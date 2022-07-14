

from ..utils import Object


class TMeUrlType(Object):
    """
    Describes the type of a URL linking to an internal Telegram entity

    No parameters required.
    """
    ID = "tMeUrlType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TMeUrlTypeStickerSet or TMeUrlTypeSupergroup or TMeUrlTypeChatInvite or TMeUrlTypeUser":
        if q.get("@type"):
            return Object.read(q)
        return TMeUrlType()
