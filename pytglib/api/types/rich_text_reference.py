

from ..utils import Object


class RichTextReference(Object):
    """
    A reference to a richTexts object on the same web page 

    Attributes:
        ID (:obj:`str`): ``RichTextReference``

    Args:
        text (:class:`telegram.api.types.RichText`):
            The text 
        anchor_name (:obj:`str`):
            The name of a richTextAnchor object, which is the first element of the target richTexts object 
        url (:obj:`str`):
            An HTTP URL, opening the reference

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextReference"

    def __init__(self, text, anchor_name, url, **kwargs):
        
        self.text = text  # RichText
        self.anchor_name = anchor_name  # str
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "RichTextReference":
        text = Object.read(q.get('text'))
        anchor_name = q.get('anchor_name')
        url = q.get('url')
        return RichTextReference(text, anchor_name, url)
