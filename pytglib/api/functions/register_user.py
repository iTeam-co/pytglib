

from ..utils import Object


class RegisterUser(Object):
    """
    Finishes user registration. Works only when the current authorization state is authorizationStateWaitRegistration

    Attributes:
        ID (:obj:`str`): ``RegisterUser``

    Args:
        first_name (:obj:`str`):
            The first name of the user; 1-64 characters 
        last_name (:obj:`str`):
            The last name of the user; 0-64 characters

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "registerUser"

    def __init__(self, first_name, last_name, extra=None, **kwargs):
        self.extra = extra
        self.first_name = first_name  # str
        self.last_name = last_name  # str

    @staticmethod
    def read(q: dict, *args) -> "RegisterUser":
        first_name = q.get('first_name')
        last_name = q.get('last_name')
        return RegisterUser(first_name, last_name)
