

from ..utils import Object


class GetOption(Object):
    """
    Returns the value of an option by its name. (Check the list of available options on https://core.telegram.org/tdlib/options.) Can be called before authorization

    Attributes:
        ID (:obj:`str`): ``GetOption``

    Args:
        name (:obj:`str`):
            The name of the option

    Returns:
        OptionValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "getOption"

    def __init__(self, name, extra=None, **kwargs):
        self.extra = extra
        self.name = name  # str

    @staticmethod
    def read(q: dict, *args) -> "GetOption":
        name = q.get('name')
        return GetOption(name)
