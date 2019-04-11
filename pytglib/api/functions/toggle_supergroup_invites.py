

from ..utils import Object


class ToggleSupergroupInvites(Object):
    """
    Toggles whether all members of a supergroup can add new members; requires appropriate administrator rights in the supergroup. 

    Attributes:
        ID (:obj:`str`): ``ToggleSupergroupInvites``

    Args:
        supergroup_id (:obj:`int`):
            Identifier of the supergroup 
        anyone_can_invite (:obj:`bool`):
            New value of anyone_can_invite

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleSupergroupInvites"

    def __init__(self, supergroup_id, anyone_can_invite, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int
        self.anyone_can_invite = anyone_can_invite  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleSupergroupInvites":
        supergroup_id = q.get('supergroup_id')
        anyone_can_invite = q.get('anyone_can_invite')
        return ToggleSupergroupInvites(supergroup_id, anyone_can_invite)
