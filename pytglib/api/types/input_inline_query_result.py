

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
    def read(q: dict, *args) -> "InputInlineQueryResultArticle or InputInlineQueryResultAudio or InputInlineQueryResultDocument or InputInlineQueryResultContact or InputInlineQueryResultPhoto or InputInlineQueryResultGame or InputInlineQueryResultLocation or InputInlineQueryResultAnimatedMpeg4 or InputInlineQueryResultVideo or InputInlineQueryResultVoiceNote or InputInlineQueryResultSticker or InputInlineQueryResultVenue or InputInlineQueryResultAnimatedGif":
        if q.get("@type"):
            return Object.read(q)
        return InputInlineQueryResult()
