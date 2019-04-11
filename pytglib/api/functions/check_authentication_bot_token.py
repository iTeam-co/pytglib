

from ..utils import Object


class CheckAuthenticationBotToken(Object):
    """
    Checks the authentication token of a bot; to log in as a bot. Works only when the current authorization state is authorizationStateWaitPhoneNumber. Can be used instead of setAuthenticationPhoneNumber and checkAuthenticationCode to log in 

    Attributes:
        ID (:obj:`str`): ``CheckAuthenticationBotToken``

    Args:
        token (:obj:`str`):
            The bot token

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkAuthenticationBotToken"

    def __init__(self, token, extra=None, **kwargs):
        self.extra = extra
        self.token = token  # str

    @staticmethod
    def read(q: dict, *args) -> "CheckAuthenticationBotToken":
        token = q.get('token')
        return CheckAuthenticationBotToken(token)
