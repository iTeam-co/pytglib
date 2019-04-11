

from ..utils import Object


class Ok(Object):
    """
    An object of this type is returned on a successful function call for certain functions

    Attributes:
        ID (:obj:`str`): ``Ok``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "ok"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "Ok":
        
        return Ok()
