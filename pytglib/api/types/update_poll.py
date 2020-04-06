

from ..utils import Object


class UpdatePoll(Object):
    """
    A poll was updated; for bots only 

    Attributes:
        ID (:obj:`str`): ``UpdatePoll``

    Args:
        poll (:class:`telegram.api.types.poll`):
            New data about the poll

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updatePoll"

    def __init__(self, poll, **kwargs):
        
        self.poll = poll  # Poll

    @staticmethod
    def read(q: dict, *args) -> "UpdatePoll":
        poll = Object.read(q.get('poll'))
        return UpdatePoll(poll)
