

from ..utils import Object


class InputMessageVenue(Object):
    """
    A message with information about a venue 

    Attributes:
        ID (:obj:`str`): ``InputMessageVenue``

    Args:
        venue (:class:`telegram.api.types.venue`):
            Venue to send

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageVenue"

    def __init__(self, venue, **kwargs):
        
        self.venue = venue  # Venue

    @staticmethod
    def read(q: dict, *args) -> "InputMessageVenue":
        venue = Object.read(q.get('venue'))
        return InputMessageVenue(venue)
