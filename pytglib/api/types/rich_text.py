

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
    def read(q: dict, *args) -> "RichTextUnderline or RichTextFixed or RichTextPlain or RichTextMarked or RichTextStrikethrough or RichTexts or RichTextAnchor or RichTextUrl or RichTextPhoneNumber or RichTextAnchorLink or RichTextItalic or RichTextIcon or RichTextSuperscript or RichTextReference or RichTextBold or RichTextSubscript or RichTextEmailAddress":
        if q.get("@type"):
            return Object.read(q)
        return RichText()
