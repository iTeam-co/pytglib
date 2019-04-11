

from ..utils import Object


class ConnectedWebsite(Object):
    """
    Contains information about one website the current user is logged in with Telegram

    Attributes:
        ID (:obj:`str`): ``ConnectedWebsite``

    Args:
        id (:obj:`int`):
            Website identifier
        domain_name (:obj:`str`):
            The domain name of the website
        bot_user_id (:obj:`int`):
            User identifier of a bot linked with the website
        browser (:obj:`str`):
            The version of a browser used to log in
        platform (:obj:`str`):
            Operating system the browser is running on
        log_in_date (:obj:`int`):
            Point in time (Unix timestamp) when the user was logged in
        last_active_date (:obj:`int`):
            Point in time (Unix timestamp) when obtained authorization was last used
        ip (:obj:`str`):
            IP address from which the user was logged in, in human-readable format
        location (:obj:`str`):
            Human-readable description of a country and a region, from which the user was logged in, based on the IP address

    Returns:
        ConnectedWebsite

    Raises:
        :class:`telegram.Error`
    """
    ID = "connectedWebsite"

    def __init__(self, id, domain_name, bot_user_id, browser, platform, log_in_date, last_active_date, ip, location, **kwargs):
        
        self.id = id  # int
        self.domain_name = domain_name  # str
        self.bot_user_id = bot_user_id  # int
        self.browser = browser  # str
        self.platform = platform  # str
        self.log_in_date = log_in_date  # int
        self.last_active_date = last_active_date  # int
        self.ip = ip  # str
        self.location = location  # str

    @staticmethod
    def read(q: dict, *args) -> "ConnectedWebsite":
        id = q.get('id')
        domain_name = q.get('domain_name')
        bot_user_id = q.get('bot_user_id')
        browser = q.get('browser')
        platform = q.get('platform')
        log_in_date = q.get('log_in_date')
        last_active_date = q.get('last_active_date')
        ip = q.get('ip')
        location = q.get('location')
        return ConnectedWebsite(id, domain_name, bot_user_id, browser, platform, log_in_date, last_active_date, ip, location)
