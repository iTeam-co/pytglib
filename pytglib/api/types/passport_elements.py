

from ..utils import Object


class PassportElements(Object):
    """
    Contains information about saved Telegram Passport elements 

    Attributes:
        ID (:obj:`str`): ``PassportElements``

    Args:
        elements (List of :class:`telegram.api.types.PassportElement`):
            Telegram Passport elements

    Returns:
        PassportElements

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElements"

    def __init__(self, elements, **kwargs):
        
        self.elements = elements  # list of PassportElement

    @staticmethod
    def read(q: dict, *args) -> "PassportElements":
        elements = [Object.read(i) for i in q.get('elements', [])]
        return PassportElements(elements)
