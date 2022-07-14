

from ..utils import Object


class ChatActionWatchingAnimations(Object):
    """
    The user is watching animations sent by the other party by clicking on an animated emoji 

    Attributes:
        ID (:obj:`str`): ``ChatActionWatchingAnimations``

    Args:
        emoji (:obj:`str`):
            The animated emoji

    Returns:
        ChatAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionWatchingAnimations"

    def __init__(self, emoji, **kwargs):
        
        self.emoji = emoji  # str

    @staticmethod
    def read(q: dict, *args) -> "ChatActionWatchingAnimations":
        emoji = q.get('emoji')
        return ChatActionWatchingAnimations(emoji)
