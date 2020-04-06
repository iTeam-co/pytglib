

from ..utils import Object


class LoginUrlInfoRequestConfirmation(Object):
    """
    An authorization confirmation dialog needs to be shown to the user 

    Attributes:
        ID (:obj:`str`): ``LoginUrlInfoRequestConfirmation``

    Args:
        url (:obj:`str`):
            An HTTP URL to be opened 
        domain (:obj:`str`):
            A domain of the URL
        bot_user_id (:obj:`int`):
            User identifier of a bot linked with the website 
        request_write_access (:obj:`bool`):
            True, if the user needs to be requested to give the permission to the bot to send them messages

    Returns:
        LoginUrlInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "loginUrlInfoRequestConfirmation"

    def __init__(self, url, domain, bot_user_id, request_write_access, **kwargs):
        
        self.url = url  # str
        self.domain = domain  # str
        self.bot_user_id = bot_user_id  # int
        self.request_write_access = request_write_access  # bool

    @staticmethod
    def read(q: dict, *args) -> "LoginUrlInfoRequestConfirmation":
        url = q.get('url')
        domain = q.get('domain')
        bot_user_id = q.get('bot_user_id')
        request_write_access = q.get('request_write_access')
        return LoginUrlInfoRequestConfirmation(url, domain, bot_user_id, request_write_access)
