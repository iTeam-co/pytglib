

from ..utils import Object


class SetChatPhoto(Object):
    """
    Changes the photo of a chat. Supported only for basic groups, supergroups and channels. Requires can_change_info administrator right

    Attributes:
        ID (:obj:`str`): ``SetChatPhoto``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        photo (:class:`telegram.api.types.InputChatPhoto`):
            New chat photo; pass null to delete the chat photo

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatPhoto"

    def __init__(self, chat_id, photo, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.photo = photo  # InputChatPhoto

    @staticmethod
    def read(q: dict, *args) -> "SetChatPhoto":
        chat_id = q.get('chat_id')
        photo = Object.read(q.get('photo'))
        return SetChatPhoto(chat_id, photo)
