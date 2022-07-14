

from ..utils import Object


class LoadGroupCallParticipants(Object):
    """
    Loads more participants of a group call. The loaded participants will be received through updates. Use the field groupCall.loaded_all_participants to check whether all participants have already been loaded

    Attributes:
        ID (:obj:`str`): ``LoadGroupCallParticipants``

    Args:
        group_call_id (:obj:`int`):
            Group call identifierThe group call must be previously received through getGroupCall and must be joined or being joined
        limit (:obj:`int`):
            The maximum number of participants to load; up to 100

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "loadGroupCallParticipants"

    def __init__(self, group_call_id, limit, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "LoadGroupCallParticipants":
        group_call_id = q.get('group_call_id')
        limit = q.get('limit')
        return LoadGroupCallParticipants(group_call_id, limit)
