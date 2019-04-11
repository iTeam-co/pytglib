

from ..utils import Object


class ToggleBasicGroupAdministrators(Object):
    """
    Toggles the "All members are admins" setting in basic groups; requires creator privileges in the group 

    Attributes:
        ID (:obj:`str`): ``ToggleBasicGroupAdministrators``

    Args:
        basic_group_id (:obj:`int`):
            Identifier of the basic group 
        everyone_is_administrator (:obj:`bool`):
            New value of everyone_is_administrator

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleBasicGroupAdministrators"

    def __init__(self, basic_group_id, everyone_is_administrator, extra=None, **kwargs):
        self.extra = extra
        self.basic_group_id = basic_group_id  # int
        self.everyone_is_administrator = everyone_is_administrator  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleBasicGroupAdministrators":
        basic_group_id = q.get('basic_group_id')
        everyone_is_administrator = q.get('everyone_is_administrator')
        return ToggleBasicGroupAdministrators(basic_group_id, everyone_is_administrator)
