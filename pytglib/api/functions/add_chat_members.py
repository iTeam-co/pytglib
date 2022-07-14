

from ..utils import Object


class AddChatMembers(Object):
    """
    Adds multiple new members to a chat. Currently, this method is only available for supergroups and channels. This method can't be used to join a chat. Members can't be added to a channel if it has more than 200 members

    Attributes:
        ID (:obj:`str`): ``AddChatMembers``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        user_ids (List of :obj:`int`):
            Identifiers of the users to be added to the chatThe maximum number of added users is 20 for supergroups and 100 for channels

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "addChatMembers"

    def __init__(self, chat_id, user_ids, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.user_ids = user_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "AddChatMembers":
        chat_id = q.get('chat_id')
        user_ids = q.get('user_ids')
        return AddChatMembers(chat_id, user_ids)
