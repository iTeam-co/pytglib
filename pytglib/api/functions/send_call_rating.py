

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

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendCallRating"

    def __init__(self, call_id, rating, comment, extra=None, **kwargs):
        self.extra = extra
        self.call_id = call_id  # int
        self.rating = rating  # int
        self.comment = comment  # str

    @staticmethod
    def read(q: dict, *args) -> "SendCallRating":
        call_id = q.get('call_id')
        rating = q.get('rating')
        comment = q.get('comment')
        return SendCallRating(call_id, rating, comment)
