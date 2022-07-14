

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
            Document thumbnail; pass null to skip thumbnail uploading 
        disable_content_type_detection (:obj:`bool`):
            If true, automatic file type detection will be disabled and the document will be always sent as fileAlways true for files sent to secret chats 
        caption (:class:`telegram.api.types.formattedText`):
            Document caption; pass null to use an empty caption; 0-GetOption("message_caption_length_max") characters

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageDocument"

    def __init__(self, document, thumbnail, disable_content_type_detection, caption, **kwargs):
        
        self.document = document  # InputFile
        self.thumbnail = thumbnail  # InputThumbnail
        self.disable_content_type_detection = disable_content_type_detection  # bool
        self.caption = caption  # FormattedText

    @staticmethod
    def read(q: dict, *args) -> "InputMessageDocument":
        document = Object.read(q.get('document'))
        thumbnail = Object.read(q.get('thumbnail'))
        disable_content_type_detection = q.get('disable_content_type_detection')
        caption = Object.read(q.get('caption'))
        return InputMessageDocument(document, thumbnail, disable_content_type_detection, caption)
