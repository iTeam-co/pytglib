

from ..utils import Object


class SetName(Object):
    """
    Changes the first and last name of the current user. If something changes, updateUser will be sent 

    Attributes:
        ID (:obj:`str`): ``SetName``

    Args:
        first_name (:obj:`str`):
            The new value of the first name for the user; 1-64 characters 
        last_name (:obj:`str`):
            The new value of the optional last name for the user; 0-64 characters

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setName"

    def __init__(self, first_name, last_name, extra=None, **kwargs):
        self.extra = extra
        self.first_name = first_name  # str
        self.last_name = last_name  # str

    @staticmethod
    def read(q: dict, *args) -> "SetName":
        first_name = q.get('first_name')
        last_name = q.get('last_name')
        return SetName(first_name, last_name)
