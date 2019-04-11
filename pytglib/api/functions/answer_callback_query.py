

from ..utils import Object


class AnswerCallbackQuery(Object):
    """
    Sets the result of a callback query; for bots only 

    Attributes:
        ID (:obj:`str`): ``AnswerCallbackQuery``

    Args:
        callback_query_id (:obj:`int`):
            Identifier of the callback query 
        text (:obj:`str`):
            Text of the answer 
        show_alert (:obj:`bool`):
            If true, an alert should be shown to the user instead of a toast notification 
        url (:obj:`str`):
            URL to be opened 
        cache_time (:obj:`int`):
            Time during which the result of the query can be cached, in seconds

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "answerCallbackQuery"

    def __init__(self, callback_query_id, text, show_alert, url, cache_time, extra=None, **kwargs):
        self.extra = extra
        self.callback_query_id = callback_query_id  # int
        self.text = text  # str
        self.show_alert = show_alert  # bool
        self.url = url  # str
        self.cache_time = cache_time  # int

    @staticmethod
    def read(q: dict, *args) -> "AnswerCallbackQuery":
        callback_query_id = q.get('callback_query_id')
        text = q.get('text')
        show_alert = q.get('show_alert')
        url = q.get('url')
        cache_time = q.get('cache_time')
        return AnswerCallbackQuery(callback_query_id, text, show_alert, url, cache_time)
