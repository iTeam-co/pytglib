

from ..utils import Object


class RichText(Object):
    """
    Describes a text object inside an instant-view web page

    No parameters required.
    """
    ID = "richText"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "RichTextPlain or RichTextItalic or RichTextEmailAddress or RichTexts or RichTextBold or RichTextStrikethrough or RichTextUrl or RichTextUnderline or RichTextFixed":
        if q.get("@type"):
            return Object.read(q)
        return RichText()
