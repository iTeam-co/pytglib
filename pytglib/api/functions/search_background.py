

from ..utils import Object


class SearchBackground(Object):
    """
    Searches for a background by its name 

    Attributes:
        ID (:obj:`str`): ``SearchBackground``

    Args:
        name (:obj:`str`):
            The name of the background

    Returns:
        Background

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchBackground"

    def __init__(self, name, extra=None, **kwargs):
        self.extra = extra
        self.name = name  # str

    @staticmethod
    def read(q: dict, *args) -> "SearchBackground":
        name = q.get('name')
        return SearchBackground(name)
