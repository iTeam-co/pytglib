

from ..utils import Object


class PassportElementsWithErrors(Object):
    """
    Contains information about a Telegram Passport elements and corresponding errors 

    Attributes:
        ID (:obj:`str`): ``PassportElementsWithErrors``

    Args:
        elements (List of :class:`telegram.api.types.PassportElement`):
            Telegram Passport elements 
        errors (List of :class:`telegram.api.types.passportElementError`):
            Errors in the elements that are already available

    Returns:
        PassportElementsWithErrors

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementsWithErrors"

    def __init__(self, elements, errors, **kwargs):
        
        self.elements = elements  # list of PassportElement
        self.errors = errors  # list of passportElementError

    @staticmethod
    def read(q: dict, *args) -> "PassportElementsWithErrors":
        elements = [Object.read(i) for i in q.get('elements', [])]
        errors = [Object.read(i) for i in q.get('errors', [])]
        return PassportElementsWithErrors(elements, errors)
