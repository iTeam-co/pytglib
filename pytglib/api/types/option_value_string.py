

from ..utils import Object


class OptionValueString(Object):
    """
    Represents a string option 

    Attributes:
        ID (:obj:`str`): ``OptionValueString``

    Args:
        value (:obj:`str`):
            The value of the option

    Returns:
        OptionValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "optionValueString"

    def __init__(self, value, **kwargs):
        
        self.value = value  # str

    @staticmethod
    def read(q: dict, *args) -> "OptionValueString":
        value = q.get('value')
        return OptionValueString(value)
