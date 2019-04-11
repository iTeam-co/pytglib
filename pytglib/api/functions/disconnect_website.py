

from ..utils import Object


class DisconnectWebsite(Object):
    """
    Disconnects website from the current user's Telegram account 

    Attributes:
        ID (:obj:`str`): ``DisconnectWebsite``

    Args:
        website_id (:obj:`int`):
            Website identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "disconnectWebsite"

    def __init__(self, website_id, extra=None, **kwargs):
        self.extra = extra
        self.website_id = website_id  # int

    @staticmethod
    def read(q: dict, *args) -> "DisconnectWebsite":
        website_id = q.get('website_id')
        return DisconnectWebsite(website_id)
