

from ..utils import Object


class LoginUrlInfoOpen(Object):
    """
    An HTTP url needs to be open 

    Attributes:
        ID (:obj:`str`): ``LoginUrlInfoOpen``

    Args:
        url (:obj:`str`):
            The URL to open 
        skip_confirm (:obj:`bool`):
            True, if there is no need to show an ordinary open URL confirm

    Returns:
        LoginUrlInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "loginUrlInfoOpen"

    def __init__(self, url, skip_confirm, **kwargs):
        
        self.url = url  # str
        self.skip_confirm = skip_confirm  # bool

    @staticmethod
    def read(q: dict, *args) -> "LoginUrlInfoOpen":
        url = q.get('url')
        skip_confirm = q.get('skip_confirm')
        return LoginUrlInfoOpen(url, skip_confirm)
