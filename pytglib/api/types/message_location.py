

from ..utils import Object


class MessageLocation(Object):
    """
    A message with a location 

    Attributes:
        ID (:obj:`str`): ``MessageLocation``

    Args:
        location (:class:`telegram.api.types.location`):
            The location description 
        live_period (:obj:`int`):
            Time relative to the message sent date until which the location can be updated, in seconds
        expires_in (:obj:`int`):
            Left time for which the location can be updated, in secondsupdateMessageContent is not sent when this field changes

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageLocation"

    def __init__(self, location, live_period, expires_in, **kwargs):
        
        self.location = location  # Location
        self.live_period = live_period  # int
        self.expires_in = expires_in  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageLocation":
        location = Object.read(q.get('location'))
        live_period = q.get('live_period')
        expires_in = q.get('expires_in')
        return MessageLocation(location, live_period, expires_in)
