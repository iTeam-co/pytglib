

from ..utils import Object


class OptionValueEmpty(Object):
    """
    Represents an unknown option or an option which has a default value

    Attributes:
        ID (:obj:`str`): ``OptionValueEmpty``

    No parameters required.

    Returns:
        OptionValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "optionValueEmpty"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "OptionValueEmpty":
        
        return OptionValueEmpty()
