

from ..utils import Object


class InputPassportElementAddress(Object):
    """
    A Telegram Passport element to be saved containing the user's address 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementAddress``

    Args:
        address (:class:`telegram.api.types.address`):
            The address to be saved

    Returns:
        InputPassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementAddress"

    def __init__(self, address, **kwargs):
        
        self.address = address  # Address

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementAddress":
        address = Object.read(q.get('address'))
        return InputPassportElementAddress(address)
