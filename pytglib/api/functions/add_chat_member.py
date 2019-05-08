

from ..utils import Object


class AddChatMember(Object):
    """
    Adds a new member to a chat. Members can't be added to private or secret chats. Members will not be added until the chat state has been synchronized with the server

    Attributes:
        ID (:obj:`str`): ``AddChatMember``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        user_id (:obj:`int`):
            Identifier of the user 
        forward_limit (:obj:`int`):
            The number of earlier messages from the chat to be forwarded to the new member; up to 100Ignored for supergroups and channels

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "addChatMember"

    def __init__(self, chat_id, user_id, forward_limit, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.user_id = user_id  # int
        self.forward_limit = forward_limit  # int

    @staticmethod
    def read(q: dict, *args) -> "AddChatMember":
        chat_id = q.get('chat_id')
        user_id = q.get('user_id')
        forward_limit = q.get('forward_limit')
        return AddChatMember(chat_id, user_id, forward_limit)
