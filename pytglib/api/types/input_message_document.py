

from ..utils import Object


class InputMessageDocument(Object):
    """
    A document message (general file) 

    Attributes:
        ID (:obj:`str`): ``InputMessageDocument``

    Args:
        document (:class:`telegram.api.types.InputFile`):
            Document to be sent 
        thumbnail (:class:`telegram.api.types.inputThumbnail`):
            Document thumbnail, if available 
        caption (:class:`telegram.api.types.formattedText`):
            Document caption; 0-GetOption("message_caption_length_max") characters

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageDocument"

    def __init__(self, document, thumbnail, caption, **kwargs):
        
        self.document = document  # InputFile
        self.thumbnail = thumbnail  # InputThumbnail
        self.caption = caption  # FormattedText

    @staticmethod
    def read(q: dict, *args) -> "InputMessageDocument":
        document = Object.read(q.get('document'))
        thumbnail = Object.read(q.get('thumbnail'))
        caption = Object.read(q.get('caption'))
        return InputMessageDocument(document, thumbnail, caption)
