

from ..utils import Object


class GetBasicGroupFullInfo(Object):
    """
    Returns full information about a basic group by its identifier 

    Attributes:
        ID (:obj:`str`): ``GetBasicGroupFullInfo``

    Args:
        basic_group_id (:obj:`int`):
            Basic group identifier

    Returns:
        BasicGroupFullInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "getBasicGroupFullInfo"

    def __init__(self, basic_group_id, extra=None, **kwargs):
        self.extra = extra
        self.basic_group_id = basic_group_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetBasicGroupFullInfo":
        basic_group_id = q.get('basic_group_id')
        return GetBasicGroupFullInfo(basic_group_id)
