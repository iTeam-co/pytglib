

from ..utils import Object


class InputFileId(Object):
    """
    A file defined by its unique ID 

    Attributes:
        ID (:obj:`str`): ``InputFileId``

    Args:
        id (:obj:`int`):
            Unique file identifier

    Returns:
        InputFile

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputFileId"

    def __init__(self, id, **kwargs):
        
        self.id = id  # int

    @staticmethod
    def read(q: dict, *args) -> "InputFileId":
        id = q.get('id')
        return InputFileId(id)
