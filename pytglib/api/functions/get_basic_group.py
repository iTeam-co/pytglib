

from ..utils import Object


class GetBasicGroup(Object):
    """
    Returns information about a basic group by its identifier. This is an offline request if the current user is not a bot 

    Attributes:
        ID (:obj:`str`): ``GetBasicGroup``

    Args:
        basic_group_id (:obj:`int`):
            Basic group identifier

    Returns:
        BasicGroup

    Raises:
        :class:`telegram.Error`
    """
    ID = "getBasicGroup"

    def __init__(self, basic_group_id, extra=None, **kwargs):
        self.extra = extra
        self.basic_group_id = basic_group_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetBasicGroup":
        basic_group_id = q.get('basic_group_id')
        return GetBasicGroup(basic_group_id)
