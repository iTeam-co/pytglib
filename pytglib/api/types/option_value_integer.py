

from ..utils import Object


class OptionValueInteger(Object):
    """
    Represents an integer option 

    Attributes:
        ID (:obj:`str`): ``OptionValueInteger``

    Args:
        value (:obj:`int`):
            The value of the option

    Returns:
        OptionValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "optionValueInteger"

    def __init__(self, value, **kwargs):
        
        self.value = value  # int

    @staticmethod
    def read(q: dict, *args) -> "OptionValueInteger":
        value = q.get('value')
        return OptionValueInteger(value)
