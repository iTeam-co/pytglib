

from ..utils import Object


class PassportElementAddress(Object):
    """
    A Telegram Passport element containing the user's address 

    Attributes:
        ID (:obj:`str`): ``PassportElementAddress``

    Args:
        address (:class:`telegram.api.types.address`):
            Address

    Returns:
        PassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementAddress"

    def __init__(self, address, **kwargs):
        
        self.address = address  # Address

    @staticmethod
    def read(q: dict, *args) -> "PassportElementAddress":
        address = Object.read(q.get('address'))
        return PassportElementAddress(address)
