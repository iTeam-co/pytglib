

from ..utils import Object


class RemoveBackground(Object):
    """
    Removes background from the list of installed backgrounds 

    Attributes:
        ID (:obj:`str`): ``RemoveBackground``

    Args:
        background_id (:obj:`int`):
            The background identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeBackground"

    def __init__(self, background_id, extra=None, **kwargs):
        self.extra = extra
        self.background_id = background_id  # int

    @staticmethod
    def read(q: dict, *args) -> "RemoveBackground":
        background_id = q.get('background_id')
        return RemoveBackground(background_id)
