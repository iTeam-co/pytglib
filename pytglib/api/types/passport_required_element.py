

from ..utils import Object


class PassportRequiredElement(Object):
    """
    Contains a description of the required Telegram Passport element that was requested by a service 

    Attributes:
        ID (:obj:`str`): ``PassportRequiredElement``

    Args:
        suitable_elements (List of :class:`telegram.api.types.passportSuitableElement`):
            List of Telegram Passport elements any of which is enough to provide

    Returns:
        PassportRequiredElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportRequiredElement"

    def __init__(self, suitable_elements, **kwargs):
        
        self.suitable_elements = suitable_elements  # list of passportSuitableElement

    @staticmethod
    def read(q: dict, *args) -> "PassportRequiredElement":
        suitable_elements = [Object.read(i) for i in q.get('suitable_elements', [])]
        return PassportRequiredElement(suitable_elements)
