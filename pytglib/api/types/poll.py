

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
        recent_voter_user_ids (List of :obj:`int`):
            User identifiers of recent voters, if the poll is non-anonymous
        is_anonymous (:obj:`bool`):
            True, if the poll is anonymous 
        type (:class:`telegram.api.types.PollType`):
            Type of the poll 
        is_closed (:obj:`bool`):
            True, if the poll is closed

    Returns:
        Poll

    Raises:
        :class:`telegram.Error`
    """
    ID = "poll"

    def __init__(self, id, question, options, total_voter_count, recent_voter_user_ids, is_anonymous, type, is_closed, **kwargs):
        
        self.id = id  # int
        self.question = question  # str
        self.options = options  # list of pollOption
        self.total_voter_count = total_voter_count  # int
        self.recent_voter_user_ids = recent_voter_user_ids  # list of int
        self.is_anonymous = is_anonymous  # bool
        self.type = type  # PollType
        self.is_closed = is_closed  # bool

    @staticmethod
    def read(q: dict, *args) -> "Poll":
        id = q.get('id')
        question = q.get('question')
        options = [Object.read(i) for i in q.get('options', [])]
        total_voter_count = q.get('total_voter_count')
        recent_voter_user_ids = q.get('recent_voter_user_ids')
        is_anonymous = q.get('is_anonymous')
        type = Object.read(q.get('type'))
        is_closed = q.get('is_closed')
        return Poll(id, question, options, total_voter_count, recent_voter_user_ids, is_anonymous, type, is_closed)
