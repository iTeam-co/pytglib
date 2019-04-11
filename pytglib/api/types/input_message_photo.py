

from ..utils import Object


class InputMessagePhoto(Object):
    """
    A photo message 

    Attributes:
        ID (:obj:`str`): ``InputMessagePhoto``

    Args:
        photo (:class:`telegram.api.types.InputFile`):
            Photo to send 
        thumbnail (:class:`telegram.api.types.inputThumbnail`):
            Photo thumbnail to be sent, this is sent to the other party in secret chats only 
        added_sticker_file_ids (List of :obj:`int`):
            File identifiers of the stickers added to the photo, if applicable 
        width (:obj:`int`):
            Photo width 
        height (:obj:`int`):
            Photo height 
        caption (:class:`telegram.api.types.formattedText`):
            Photo caption; 0-GetOption("message_caption_length_max") characters
        ttl (:obj:`int`):
            Photo TTL (Time To Live), in seconds (0-60)A non-zero TTL can be specified only in private chats

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessagePhoto"

    def __init__(self, photo, thumbnail, added_sticker_file_ids, width, height, caption, ttl, **kwargs):
        
        self.photo = photo  # InputFile
        self.thumbnail = thumbnail  # InputThumbnail
        self.added_sticker_file_ids = added_sticker_file_ids  # list of int
        self.width = width  # int
        self.height = height  # int
        self.caption = caption  # FormattedText
        self.ttl = ttl  # int

    @staticmethod
    def read(q: dict, *args) -> "InputMessagePhoto":
        photo = Object.read(q.get('photo'))
        thumbnail = Object.read(q.get('thumbnail'))
        added_sticker_file_ids = q.get('added_sticker_file_ids')
        width = q.get('width')
        height = q.get('height')
        caption = Object.read(q.get('caption'))
        ttl = q.get('ttl')
        return InputMessagePhoto(photo, thumbnail, added_sticker_file_ids, width, height, caption, ttl)
