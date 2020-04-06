

from ..utils import Object


class RichTextIcon(Object):
    """
    A small image inside the text 

    Attributes:
        ID (:obj:`str`): ``RichTextIcon``

    Args:
        document (:class:`telegram.api.types.document`):
            The image represented as a documentThe image can be in GIF, JPEG or PNG format
        width (:obj:`int`):
            Width of a bounding box in which the image should be shown; 0 if unknown
        height (:obj:`int`):
            Height of a bounding box in which the image should be shown; 0 if unknown

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextIcon"

    def __init__(self, document, width, height, **kwargs):
        
        self.document = document  # Document
        self.width = width  # int
        self.height = height  # int

    @staticmethod
    def read(q: dict, *args) -> "RichTextIcon":
        document = Object.read(q.get('document'))
        width = q.get('width')
        height = q.get('height')
        return RichTextIcon(document, width, height)
