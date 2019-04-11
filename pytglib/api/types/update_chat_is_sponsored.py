

from ..utils import Object


class UpdateChatIsSponsored(Object):
    """
    A chat's is_sponsored field has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatIsSponsored``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        is_sponsored (:obj:`bool`):
            New value of is_sponsored 
        order (:obj:`int`):
            New value of chat order

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatIsSponsored"

    def __init__(self, chat_id, is_sponsored, order, **kwargs):
        
        self.chat_id = chat_id  # int
        self.is_sponsored = is_sponsored  # bool
        self.order = order  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatIsSponsored":
        chat_id = q.get('chat_id')
        is_sponsored = q.get('is_sponsored')
        order = q.get('order')
        return UpdateChatIsSponsored(chat_id, is_sponsored, order)
