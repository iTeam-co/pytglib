

from ..utils import Object


class DeleteMessages(Object):
    """
    Deletes messages 

    Attributes:
        ID (:obj:`str`): ``DeleteMessages``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_ids (List of :obj:`int`):
            Identifiers of the messages to be deleted 
        revoke (:obj:`bool`):
            Pass true to try to delete messages for all chat membersAlways true for supergroups, channels and secret chats

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteMessages"

    def __init__(self, chat_id, message_ids, revoke, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_ids = message_ids  # list of int
        self.revoke = revoke  # bool

    @staticmethod
    def read(q: dict, *args) -> "DeleteMessages":
        chat_id = q.get('chat_id')
        message_ids = q.get('message_ids')
        revoke = q.get('revoke')
        return DeleteMessages(chat_id, message_ids, revoke)
