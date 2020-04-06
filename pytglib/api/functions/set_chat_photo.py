

from ..utils import Object


class SetChatPhoto(Object):
    """
    Changes the photo of a chat. Supported only for basic groups, supergroups and channels. Requires can_change_info rights. The photo will not be changed before request to the server has been completed

    Attributes:
        ID (:obj:`str`): ``SetChatPhoto``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        photo (:class:`telegram.api.types.InputFile`):
            New chat photoYou can use a zero InputFileId to delete the chat photoFiles that are accessible only by HTTP URL are not acceptable

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatPhoto"

    def __init__(self, chat_id, photo, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.photo = photo  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "SetChatPhoto":
        chat_id = q.get('chat_id')
        photo = Object.read(q.get('photo'))
        return SetChatPhoto(chat_id, photo)
