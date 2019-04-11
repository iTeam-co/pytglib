

from ..utils import Object


class AnswerCustomQuery(Object):
    """
    Answers a custom query; for bots only 

    Attributes:
        ID (:obj:`str`): ``AnswerCustomQuery``

    Args:
        custom_query_id (:obj:`int`):
            Identifier of a custom query 
        data (:obj:`str`):
            JSON-serialized answer to the query

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "answerCustomQuery"

    def __init__(self, custom_query_id, data, extra=None, **kwargs):
        self.extra = extra
        self.custom_query_id = custom_query_id  # int
        self.data = data  # str

    @staticmethod
    def read(q: dict, *args) -> "AnswerCustomQuery":
        custom_query_id = q.get('custom_query_id')
        data = q.get('data')
        return AnswerCustomQuery(custom_query_id, data)
