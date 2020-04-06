

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
    def read(q: dict, *args) -> "RichTextIcon or RichTexts or RichTextFixed or RichTextSubscript or RichTextPlain or RichTextAnchor or RichTextEmailAddress or RichTextUnderline or RichTextMarked or RichTextReference or RichTextSuperscript or RichTextStrikethrough or RichTextPhoneNumber or RichTextBold or RichTextUrl or RichTextAnchorLink or RichTextItalic":
        if q.get("@type"):
            return Object.read(q)
        return RichText()
