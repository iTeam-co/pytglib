

from ..utils import Object


class GetInviteText(Object):
    """
    Returns the default text for invitation messages to be used as a placeholder when the current user invites friends to Telegram

    Attributes:
        ID (:obj:`str`): ``GetInviteText``

    No parameters required.

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "getInviteText"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetInviteText":
        
        return GetInviteText()
