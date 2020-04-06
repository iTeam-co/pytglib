

from ..utils import Object


class InputBackgroundRemote(Object):
    """
    A background from the server 

    Attributes:
        ID (:obj:`str`): ``InputBackgroundRemote``

    Args:
        background_id (:obj:`int`):
            The background identifier

    Returns:
        InputBackground

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputBackgroundRemote"

    def __init__(self, background_id, **kwargs):
        
        self.background_id = background_id  # int

    @staticmethod
    def read(q: dict, *args) -> "InputBackgroundRemote":
        background_id = q.get('background_id')
        return InputBackgroundRemote(background_id)
