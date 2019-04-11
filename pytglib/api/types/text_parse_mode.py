

from ..utils import Object


class TextParseMode(Object):
    """
    Describes the way the text should be parsed for TextEntities

    No parameters required.
    """
    ID = "textParseMode"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextParseModeMarkdown or TextParseModeHTML":
        if q.get("@type"):
            return Object.read(q)
        return TextParseMode()
