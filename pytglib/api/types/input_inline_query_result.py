

from ..utils import Object


class InputInlineQueryResult(Object):
    """
    Represents a single result of an inline query; for bots only

    No parameters required.
    """
    ID = "inputInlineQueryResult"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InputInlineQueryResultVideo or InputInlineQueryResultGame or InputInlineQueryResultAudio or InputInlineQueryResultVoiceNote or InputInlineQueryResultAnimation or InputInlineQueryResultPhoto or InputInlineQueryResultContact or InputInlineQueryResultSticker or InputInlineQueryResultLocation or InputInlineQueryResultDocument or InputInlineQueryResultArticle or InputInlineQueryResultVenue":
        if q.get("@type"):
            return Object.read(q)
        return InputInlineQueryResult()
