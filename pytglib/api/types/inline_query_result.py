

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
    def read(q: dict, *args) -> "InlineQueryResultAudio or InlineQueryResultArticle or InlineQueryResultDocument or InlineQueryResultVideo or InlineQueryResultAnimation or InlineQueryResultContact or InlineQueryResultVoiceNote or InlineQueryResultGame or InlineQueryResultPhoto or InlineQueryResultSticker or InlineQueryResultLocation or InlineQueryResultVenue":
        if q.get("@type"):
            return Object.read(q)
        return InlineQueryResult()
