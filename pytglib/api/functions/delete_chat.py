

from ..utils import Object


class DeleteChat(Object):
    """
    Deletes a chat along with all messages in the corresponding chat for all chat members. For group chats this will release the username and remove all members. Use the field chat.can_be_deleted_for_all_users to find whether the method can be applied to the chat 

    Attributes:
        ID (:obj:`str`): ``DeleteChat``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteChat"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "DeleteChat":
        chat_id = q.get('chat_id')
        return DeleteChat(chat_id)
