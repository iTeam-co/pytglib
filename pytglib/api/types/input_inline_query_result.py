

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
    def read(q: dict, *args) -> "InputInlineQueryResultPhoto or InputInlineQueryResultDocument or InputInlineQueryResultVideo or InputInlineQueryResultGame or InputInlineQueryResultVoiceNote or InputInlineQueryResultArticle or InputInlineQueryResultContact or InputInlineQueryResultAnimatedMpeg4 or InputInlineQueryResultVenue or InputInlineQueryResultLocation or InputInlineQueryResultSticker or InputInlineQueryResultAnimatedGif or InputInlineQueryResultAudio":
        if q.get("@type"):
            return Object.read(q)
        return InputInlineQueryResult()
