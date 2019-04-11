

from ..utils import Object


class InlineQueryResults(Object):
    """
    Represents the results of the inline query. Use sendInlineQueryResultMessage to send the result of the query 

    Attributes:
        ID (:obj:`str`): ``InlineQueryResults``

    Args:
        inline_query_id (:obj:`int`):
            Unique identifier of the inline query 
        next_offset (:obj:`str`):
            The offset for the next requestIf empty, there are no more results 
        results (List of :class:`telegram.api.types.InlineQueryResult`):
            Results of the query
        switch_pm_text (:obj:`str`):
            If non-empty, this text should be shown on the button, which opens a private chat with the bot and sends the bot a start message with the switch_pm_parameter 
        switch_pm_parameter (:obj:`str`):
            Parameter for the bot start message

    Returns:
        InlineQueryResults

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineQueryResults"

    def __init__(self, inline_query_id, next_offset, results, switch_pm_text, switch_pm_parameter, **kwargs):
        
        self.inline_query_id = inline_query_id  # int
        self.next_offset = next_offset  # str
        self.results = results  # list of InlineQueryResult
        self.switch_pm_text = switch_pm_text  # str
        self.switch_pm_parameter = switch_pm_parameter  # str

    @staticmethod
    def read(q: dict, *args) -> "InlineQueryResults":
        inline_query_id = q.get('inline_query_id')
        next_offset = q.get('next_offset')
        results = [Object.read(i) for i in q.get('results', [])]
        switch_pm_text = q.get('switch_pm_text')
        switch_pm_parameter = q.get('switch_pm_parameter')
        return InlineQueryResults(inline_query_id, next_offset, results, switch_pm_text, switch_pm_parameter)
