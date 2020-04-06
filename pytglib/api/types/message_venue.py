

from ..utils import Object


class MessageVenue(Object):
    """
    A message with information about a venue 

    Attributes:
        ID (:obj:`str`): ``MessageVenue``

    Args:
        venue (:class:`telegram.api.types.venue`):
            The venue description

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageVenue"

    def __init__(self, venue, **kwargs):
        
        self.venue = venue  # Venue

    @staticmethod
    def read(q: dict, *args) -> "MessageVenue":
        venue = Object.read(q.get('venue'))
        return MessageVenue(venue)
