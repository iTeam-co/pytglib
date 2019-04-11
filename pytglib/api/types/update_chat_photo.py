

from ..utils import Object


class UpdateChatPhoto(Object):
    """
    A chat photo was changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatPhoto``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        photo (:class:`telegram.api.types.chatPhoto`):
            The new chat photo; may be null

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatPhoto"

    def __init__(self, chat_id, photo, **kwargs):
        
        self.chat_id = chat_id  # int
        self.photo = photo  # ChatPhoto

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatPhoto":
        chat_id = q.get('chat_id')
        photo = Object.read(q.get('photo'))
        return UpdateChatPhoto(chat_id, photo)
