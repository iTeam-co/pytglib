

from ..utils import Object


class ChatActionBarSharePhoneNumber(Object):
    """
    The chat is a private or secret chat with a mutual contact and the user's phone number can be shared with the other user using the method sharePhoneNumber

    Attributes:
        ID (:obj:`str`): ``ChatActionBarSharePhoneNumber``

    No parameters required.

    Returns:
        ChatActionBar

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionBarSharePhoneNumber"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionBarSharePhoneNumber":
        
        return ChatActionBarSharePhoneNumber()
