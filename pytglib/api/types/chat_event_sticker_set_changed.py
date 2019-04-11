

from ..utils import Object


class ChatEventStickerSetChanged(Object):
    """
    The supergroup sticker set was changed 

    Attributes:
        ID (:obj:`str`): ``ChatEventStickerSetChanged``

    Args:
        old_sticker_set_id (:obj:`int`):
            Previous identifier of the chat sticker set; 0 if none 
        new_sticker_set_id (:obj:`int`):
            New identifier of the chat sticker set; 0 if none

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventStickerSetChanged"

    def __init__(self, old_sticker_set_id, new_sticker_set_id, **kwargs):
        
        self.old_sticker_set_id = old_sticker_set_id  # int
        self.new_sticker_set_id = new_sticker_set_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatEventStickerSetChanged":
        old_sticker_set_id = q.get('old_sticker_set_id')
        new_sticker_set_id = q.get('new_sticker_set_id')
        return ChatEventStickerSetChanged(old_sticker_set_id, new_sticker_set_id)
