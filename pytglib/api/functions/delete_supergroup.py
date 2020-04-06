

from ..utils import Object


class DeleteSupergroup(Object):
    """
    Deletes a supergroup or channel along with all messages in the corresponding chat. This will release the supergroup or channel username and remove all members; requires owner privileges in the supergroup or channel. Chats with more than 1000 members can't be deleted using this method 

    Attributes:
        ID (:obj:`str`): ``DeleteSupergroup``

    Args:
        supergroup_id (:obj:`int`):
            Identifier of the supergroup or channel

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteSupergroup"

    def __init__(self, supergroup_id, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int

    @staticmethod
    def read(q: dict, *args) -> "DeleteSupergroup":
        supergroup_id = q.get('supergroup_id')
        return DeleteSupergroup(supergroup_id)
