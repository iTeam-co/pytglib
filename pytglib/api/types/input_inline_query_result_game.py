

from ..utils import Object


class InputInlineQueryResultGame(Object):
    """
    Represents a game 

    Attributes:
        ID (:obj:`str`): ``InputInlineQueryResultGame``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        game_short_name (:obj:`str`):
            Short name of the game 
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            Message reply markupMust be of type replyMarkupInlineKeyboard or null

    Returns:
        InputInlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputInlineQueryResultGame"

    def __init__(self, id, game_short_name, reply_markup, **kwargs):
        
        self.id = id  # str
        self.game_short_name = game_short_name  # str
        self.reply_markup = reply_markup  # ReplyMarkup

    @staticmethod
    def read(q: dict, *args) -> "InputInlineQueryResultGame":
        id = q.get('id')
        game_short_name = q.get('game_short_name')
        reply_markup = Object.read(q.get('reply_markup'))
        return InputInlineQueryResultGame(id, game_short_name, reply_markup)
