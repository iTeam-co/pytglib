

from ..utils import Object


class UpdateAnimatedEmojiMessageClicked(Object):
    """
    Some animated emoji message was clicked and a big animated sticker must be played if the message is visible on the screen. chatActionWatchingAnimations with the text of the message needs to be sent if the sticker is played

    Attributes:
        ID (:obj:`str`): ``UpdateAnimatedEmojiMessageClicked``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_id (:obj:`int`):
            Message identifier 
        sticker (:class:`telegram.api.types.sticker`):
            The animated sticker to be played

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateAnimatedEmojiMessageClicked"

    def __init__(self, chat_id, message_id, sticker, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.sticker = sticker  # Sticker

    @staticmethod
    def read(q: dict, *args) -> "UpdateAnimatedEmojiMessageClicked":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        sticker = Object.read(q.get('sticker'))
        return UpdateAnimatedEmojiMessageClicked(chat_id, message_id, sticker)
