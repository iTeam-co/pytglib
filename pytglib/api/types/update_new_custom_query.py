

from ..utils import Object


class UpdateNewCustomQuery(Object):
    """
    A new incoming query; for bots only 

    Attributes:
        ID (:obj:`str`): ``UpdateNewCustomQuery``

    Args:
        id (:obj:`int`):
            The query identifier 
        data (:obj:`str`):
            JSON-serialized query data 
        timeout (:obj:`int`):
            Query timeout

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateNewCustomQuery"

    def __init__(self, id, data, timeout, **kwargs):
        
        self.id = id  # int
        self.data = data  # str
        self.timeout = timeout  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateNewCustomQuery":
        id = q.get('id')
        data = q.get('data')
        timeout = q.get('timeout')
        return UpdateNewCustomQuery(id, data, timeout)
