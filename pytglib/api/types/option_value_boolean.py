

from ..utils import Object


class OptionValueBoolean(Object):
    """
    Represents a boolean option 

    Attributes:
        ID (:obj:`str`): ``OptionValueBoolean``

    Args:
        value (:obj:`bool`):
            The value of the option

    Returns:
        OptionValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "optionValueBoolean"

    def __init__(self, value, **kwargs):
        
        self.value = value  # bool

    @staticmethod
    def read(q: dict, *args) -> "OptionValueBoolean":
        value = q.get('value')
        return OptionValueBoolean(value)
