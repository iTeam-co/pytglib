

from ..utils import Object


class RichTextReference(Object):
    """
    A rich text reference of a text on the same web page 

    Attributes:
        ID (:obj:`str`): ``RichTextReference``

    Args:
        text (:class:`telegram.api.types.RichText`):
            The text 
        reference_text (:class:`telegram.api.types.RichText`):
            The text to show on click 
        url (:obj:`str`):
            An HTTP URL, opening the reference

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextReference"

    def __init__(self, text, reference_text, url, **kwargs):
        
        self.text = text  # RichText
        self.reference_text = reference_text  # RichText
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "RichTextReference":
        text = Object.read(q.get('text'))
        reference_text = Object.read(q.get('reference_text'))
        url = q.get('url')
        return RichTextReference(text, reference_text, url)
