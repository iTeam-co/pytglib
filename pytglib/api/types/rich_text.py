

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
    def read(q: dict, *args) -> "RichTextSubscript or RichTextAnchor or RichTextIcon or RichTextFixed or RichTextBold or RichTextSuperscript or RichTextPhoneNumber or RichTextMarked or RichTexts or RichTextPlain or RichTextEmailAddress or RichTextUrl or RichTextUnderline or RichTextStrikethrough or RichTextItalic":
        if q.get("@type"):
            return Object.read(q)
        return RichText()
