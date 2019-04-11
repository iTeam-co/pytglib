

from ..utils import Object


class SetOption(Object):
    """
    Sets the value of an option. (Check the list of available options on https://core.telegram.org/tdlib/options.) Only writable options can be set. Can be called before authorization

    Attributes:
        ID (:obj:`str`): ``SetOption``

    Args:
        name (:obj:`str`):
            The name of the option 
        value (:class:`telegram.api.types.OptionValue`):
            The new value of the option

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setOption"

    def __init__(self, name, value, extra=None, **kwargs):
        self.extra = extra
        self.name = name  # str
        self.value = value  # OptionValue

    @staticmethod
    def read(q: dict, *args) -> "SetOption":
        name = q.get('name')
        value = Object.read(q.get('value'))
        return SetOption(name, value)
