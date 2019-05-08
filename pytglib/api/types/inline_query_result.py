

from ..utils import Object


class InlineQueryResult(Object):
    """
    Represents a single result of an inline query

    No parameters required.
    """
    ID = "inlineQueryResult"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InlineQueryResultArticle or InlineQueryResultVoiceNote or InlineQueryResultLocation or InlineQueryResultVideo or InlineQueryResultDocument or InlineQueryResultGame or InlineQueryResultAudio or InlineQueryResultPhoto or InlineQueryResultContact or InlineQueryResultAnimation or InlineQueryResultSticker or InlineQueryResultVenue":
        if q.get("@type"):
            return Object.read(q)
        return InlineQueryResult()
