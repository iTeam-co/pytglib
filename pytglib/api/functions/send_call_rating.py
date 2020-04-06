

from ..utils import Object


class SendCallRating(Object):
    """
    Sends a call rating 

    Attributes:
        ID (:obj:`str`): ``SendCallRating``

    Args:
        call_id (:obj:`int`):
            Call identifier 
        rating (:obj:`int`):
            Call rating; 1-5 
        comment (:obj:`str`):
            An optional user comment if the rating is less than 5 
        problems (List of :class:`telegram.api.types.CallProblem`):
            List of the exact types of problems with the call, specified by the user

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendCallRating"

    def __init__(self, call_id, rating, comment, problems, extra=None, **kwargs):
        self.extra = extra
        self.call_id = call_id  # int
        self.rating = rating  # int
        self.comment = comment  # str
        self.problems = problems  # list of CallProblem

    @staticmethod
    def read(q: dict, *args) -> "SendCallRating":
        call_id = q.get('call_id')
        rating = q.get('rating')
        comment = q.get('comment')
        problems = [Object.read(i) for i in q.get('problems', [])]
        return SendCallRating(call_id, rating, comment, problems)
