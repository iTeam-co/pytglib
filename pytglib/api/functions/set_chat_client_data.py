

from ..utils import Object


class SetChatClientData(Object):
    """
    Changes client data associated with a chat 

    Attributes:
        ID (:obj:`str`): ``SetChatClientData``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        client_data (:obj:`str`):
            New value of client_data

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatClientData"

    def __init__(self, chat_id, client_data, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.client_data = client_data  # str

    @staticmethod
    def read(q: dict, *args) -> "SetChatClientData":
        chat_id = q.get('chat_id')
        client_data = q.get('client_data')
        return SetChatClientData(chat_id, client_data)
