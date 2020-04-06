

from ..utils import Object


class SetLocation(Object):
    """
    Changes the location of the current user. Needs to be called if GetOption("is_location_visible") is true and location changes for more than 1 kilometer 

    Attributes:
        ID (:obj:`str`): ``SetLocation``

    Args:
        location (:class:`telegram.api.types.location`):
            The new location of the user

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setLocation"

    def __init__(self, location, extra=None, **kwargs):
        self.extra = extra
        self.location = location  # Location

    @staticmethod
    def read(q: dict, *args) -> "SetLocation":
        location = Object.read(q.get('location'))
        return SetLocation(location)
