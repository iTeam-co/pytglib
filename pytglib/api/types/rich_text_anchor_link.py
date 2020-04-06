

from ..utils import Object


class RichTextAnchorLink(Object):
    """
    A link to an anchor on the same web page 

    Attributes:
        ID (:obj:`str`): ``RichTextAnchorLink``

    Args:
        text (:class:`telegram.api.types.RichText`):
            The link text 
        name (:obj:`str`):
            The anchor nameIf the name is empty, the link should bring back to top 
        url (:obj:`str`):
            An HTTP URL, opening the anchor

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextAnchorLink"

    def __init__(self, text, name, url, **kwargs):
        
        self.text = text  # RichText
        self.name = name  # str
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "RichTextAnchorLink":
        text = Object.read(q.get('text'))
        name = q.get('name')
        url = q.get('url')
        return RichTextAnchorLink(text, name, url)
