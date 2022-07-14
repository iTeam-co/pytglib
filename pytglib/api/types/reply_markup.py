

from ..utils import Object


class ReplyMarkup(Object):
    """
    Contains a description of a custom keyboard and actions that can be done with it to quickly reply to bots

    No parameters required.
    """
    ID = "replyMarkup"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ReplyMarkupShowKeyboard or ReplyMarkupRemoveKeyboard or ReplyMarkupInlineKeyboard or ReplyMarkupForceReply":
        if q.get("@type"):
            return Object.read(q)
        return ReplyMarkup()
