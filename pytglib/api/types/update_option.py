

from ..utils import Object


class UpdateOption(Object):
    """
    An option changed its value 

    Attributes:
        ID (:obj:`str`): ``UpdateOption``

    Args:
        name (:obj:`str`):
            The option name 
        value (:class:`telegram.api.types.OptionValue`):
            The new option value

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateOption"

    def __init__(self, name, value, **kwargs):
        
        self.name = name  # str
        self.value = value  # OptionValue

    @staticmethod
    def read(q: dict, *args) -> "UpdateOption":
        name = q.get('name')
        value = Object.read(q.get('value'))
        return UpdateOption(name, value)
