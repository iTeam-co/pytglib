

from ..utils import Object


class UpdatePollAnswer(Object):
    """
    A user changed the answer to a poll; for bots only 

    Attributes:
        ID (:obj:`str`): ``UpdatePollAnswer``

    Args:
        poll_id (:obj:`int`):
            Unique poll identifier 
        user_id (:obj:`int`):
            The user, who changed the answer to the poll 
        option_ids (List of :obj:`int`):
            0-based identifiers of answer options, chosen by the user

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updatePollAnswer"

    def __init__(self, poll_id, user_id, option_ids, **kwargs):
        
        self.poll_id = poll_id  # int
        self.user_id = user_id  # int
        self.option_ids = option_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "UpdatePollAnswer":
        poll_id = q.get('poll_id')
        user_id = q.get('user_id')
        option_ids = q.get('option_ids')
        return UpdatePollAnswer(poll_id, user_id, option_ids)
