

from ..utils import Object


class AnswerWebAppQuery(Object):
    """
    Sets the result of interaction with a Web App and sends corresponding message on behalf of the user to the chat from which the query originated; for bots only

    Attributes:
        ID (:obj:`str`): ``AnswerWebAppQuery``

    Args:
        web_app_query_id (:obj:`str`):
            Identifier of the Web App query
        result (:class:`telegram.api.types.InputInlineQueryResult`):
            The result of the query

    Returns:
        SentWebAppMessage

    Raises:
        :class:`telegram.Error`
    """
    ID = "answerWebAppQuery"

    def __init__(self, web_app_query_id, result, extra=None, **kwargs):
        self.extra = extra
        self.web_app_query_id = web_app_query_id  # str
        self.result = result  # InputInlineQueryResult

    @staticmethod
    def read(q: dict, *args) -> "AnswerWebAppQuery":
        web_app_query_id = q.get('web_app_query_id')
        result = Object.read(q.get('result'))
        return AnswerWebAppQuery(web_app_query_id, result)
