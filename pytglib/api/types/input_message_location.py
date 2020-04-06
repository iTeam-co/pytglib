

from ..utils import Object


class InputMessageLocation(Object):
    """
    A message with a location 

    Attributes:
        ID (:obj:`str`): ``InputMessageLocation``

    Args:
        location (:class:`telegram.api.types.location`):
            Location to be sent 
        live_period (:obj:`int`):
            Period for which the location can be updated, in seconds; should be between 60 and 86400 for a live location and 0 otherwise

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageLocation"

    def __init__(self, location, live_period, **kwargs):
        
        self.location = location  # Location
        self.live_period = live_period  # int

    @staticmethod
    def read(q: dict, *args) -> "InputMessageLocation":
        location = Object.read(q.get('location'))
        live_period = q.get('live_period')
        return InputMessageLocation(location, live_period)
