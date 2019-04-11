

from ..utils import Object


class AnswerInlineQuery(Object):
    """
    Sets the result of an inline query; for bots only 

    Attributes:
        ID (:obj:`str`): ``AnswerInlineQuery``

    Args:
        inline_query_id (:obj:`int`):
            Identifier of the inline query 
        is_personal (:obj:`bool`):
            True, if the result of the query can be cached for the specified user
        results (List of :class:`telegram.api.types.InputInlineQueryResult`):
            The results of the query 
        cache_time (:obj:`int`):
            Allowed time to cache the results of the query, in seconds 
        next_offset (:obj:`str`):
            Offset for the next inline query; pass an empty string if there are no more results
        switch_pm_text (:obj:`str`):
            If non-empty, this text should be shown on the button that opens a private chat with the bot and sends a start message to the bot with the parameter switch_pm_parameter 
        switch_pm_parameter (:obj:`str`):
            The parameter for the bot start message

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "answerInlineQuery"

    def __init__(self, inline_query_id, is_personal, results, cache_time, next_offset, switch_pm_text, switch_pm_parameter, extra=None, **kwargs):
        self.extra = extra
        self.inline_query_id = inline_query_id  # int
        self.is_personal = is_personal  # bool
        self.results = results  # list of InputInlineQueryResult
        self.cache_time = cache_time  # int
        self.next_offset = next_offset  # str
        self.switch_pm_text = switch_pm_text  # str
        self.switch_pm_parameter = switch_pm_parameter  # str

    @staticmethod
    def read(q: dict, *args) -> "AnswerInlineQuery":
        inline_query_id = q.get('inline_query_id')
        is_personal = q.get('is_personal')
        results = [Object.read(i) for i in q.get('results', [])]
        cache_time = q.get('cache_time')
        next_offset = q.get('next_offset')
        switch_pm_text = q.get('switch_pm_text')
        switch_pm_parameter = q.get('switch_pm_parameter')
        return AnswerInlineQuery(inline_query_id, is_personal, results, cache_time, next_offset, switch_pm_text, switch_pm_parameter)
