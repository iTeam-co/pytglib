

from ..utils import Object


class Poll(Object):
    """
    Describes a poll 

    Attributes:
        ID (:obj:`str`): ``Poll``

    Args:
        id (:obj:`int`):
            Unique poll identifier 
        question (:obj:`str`):
            Poll question, 1-255 characters 
        options (List of :class:`telegram.api.types.pollOption`):
            List of poll answer options 
        total_voter_count (:obj:`int`):
            Total number of voters, participating in the poll 
        is_closed (:obj:`bool`):
            True, if the poll is closed

    Returns:
        Poll

    Raises:
        :class:`telegram.Error`
    """
    ID = "poll"

    def __init__(self, id, question, options, total_voter_count, is_closed, **kwargs):
        
        self.id = id  # int
        self.question = question  # str
        self.options = options  # list of pollOption
        self.total_voter_count = total_voter_count  # int
        self.is_closed = is_closed  # bool

    @staticmethod
    def read(q: dict, *args) -> "Poll":
        id = q.get('id')
        question = q.get('question')
        options = [Object.read(i) for i in q.get('options', [])]
        total_voter_count = q.get('total_voter_count')
        is_closed = q.get('is_closed')
        return Poll(id, question, options, total_voter_count, is_closed)
