

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
    def read(q: dict, *args) -> "InputInlineQueryResultVoiceNote or InputInlineQueryResultGame or InputInlineQueryResultPhoto or InputInlineQueryResultDocument or InputInlineQueryResultVideo or InputInlineQueryResultAnimatedGif or InputInlineQueryResultArticle or InputInlineQueryResultContact or InputInlineQueryResultVenue or InputInlineQueryResultSticker or InputInlineQueryResultAnimatedMpeg4 or InputInlineQueryResultAudio or InputInlineQueryResultLocation":
        if q.get("@type"):
            return Object.read(q)
        return InputInlineQueryResult()
