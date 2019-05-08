

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
    def read(q: dict, *args) -> "RichTextBold or RichTextUrl or RichTextSubscript or RichTextAnchor or RichTextEmailAddress or RichTextPhoneNumber or RichTextIcon or RichTexts or RichTextItalic or RichTextPlain or RichTextFixed or RichTextStrikethrough or RichTextUnderline or RichTextMarked or RichTextSuperscript":
        if q.get("@type"):
            return Object.read(q)
        return RichText()
