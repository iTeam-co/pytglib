

from ..utils import Object


class GroupCallStreams(Object):
    """
    Represents a list of group call streams 

    Attributes:
        ID (:obj:`str`): ``GroupCallStreams``

    Args:
        streams (List of :class:`telegram.api.types.groupCallStream`):
            A list of group call streams

    Returns:
        GroupCallStreams

    Raises:
        :class:`telegram.Error`
    """
    ID = "groupCallStreams"

    def __init__(self, streams, **kwargs):
        
        self.streams = streams  # list of groupCallStream

    @staticmethod
    def read(q: dict, *args) -> "GroupCallStreams":
        streams = [Object.read(i) for i in q.get('streams', [])]
        return GroupCallStreams(streams)
