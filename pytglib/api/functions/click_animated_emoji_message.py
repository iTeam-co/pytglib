

from ..utils import Object


class ClickAnimatedEmojiMessage(Object):
    """
    Informs TDLib that a message with an animated emoji was clicked by the user. Returns a big animated sticker to be played or a 404 error if usual animation needs to be played 

    Attributes:
        ID (:obj:`str`): ``ClickAnimatedEmojiMessage``

    Args:
        chat_id (:obj:`int`):
            Chat identifier of the message 
        message_id (:obj:`int`):
            Identifier of the clicked message

    Returns:
        Sticker

    Raises:
        :class:`telegram.Error`
    """
    ID = "clickAnimatedEmojiMessage"

    def __init__(self, chat_id, message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ClickAnimatedEmojiMessage":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return ClickAnimatedEmojiMessage(chat_id, message_id)
