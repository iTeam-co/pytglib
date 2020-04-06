

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
    def read(q: dict, *args) -> "InputInlineQueryResultVideo or InputInlineQueryResultAudio or InputInlineQueryResultAnimatedGif or InputInlineQueryResultAnimatedMpeg4 or InputInlineQueryResultDocument or InputInlineQueryResultVoiceNote or InputInlineQueryResultContact or InputInlineQueryResultGame or InputInlineQueryResultLocation or InputInlineQueryResultSticker or InputInlineQueryResultArticle or InputInlineQueryResultPhoto or InputInlineQueryResultVenue":
        if q.get("@type"):
            return Object.read(q)
        return InputInlineQueryResult()
