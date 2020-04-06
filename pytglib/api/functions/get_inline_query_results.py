

from ..utils import Object


class GetInlineQueryResults(Object):
    """
    Sends an inline query to a bot and returns its results. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires 

    Attributes:
        ID (:obj:`str`): ``GetInlineQueryResults``

    Args:
        bot_user_id (:obj:`int`):
            The identifier of the target bot
        chat_id (:obj:`int`):
            Identifier of the chat where the query was sent 
        user_location (:class:`telegram.api.types.location`):
            Location of the user, only if needed 
        query (:obj:`str`):
            Text of the query 
        offset (:obj:`str`):
            Offset of the first entry to return

    Returns:
        InlineQueryResults

    Raises:
        :class:`telegram.Error`
    """
    ID = "getInlineQueryResults"

    def __init__(self, bot_user_id, chat_id, user_location, query, offset, extra=None, **kwargs):
        self.extra = extra
        self.bot_user_id = bot_user_id  # int
        self.chat_id = chat_id  # int
        self.user_location = user_location  # Location
        self.query = query  # str
        self.offset = offset  # str

    @staticmethod
    def read(q: dict, *args) -> "GetInlineQueryResults":
        bot_user_id = q.get('bot_user_id')
        chat_id = q.get('chat_id')
        user_location = Object.read(q.get('user_location'))
        query = q.get('query')
        offset = q.get('offset')
        return GetInlineQueryResults(bot_user_id, chat_id, user_location, query, offset)
