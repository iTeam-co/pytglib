

from ..utils import Object


class InputMessageForwarded(Object):
    """
    A forwarded message 

    Attributes:
        ID (:obj:`str`): ``InputMessageForwarded``

    Args:
        from_chat_id (:obj:`int`):
            Identifier for the chat this forwarded message came from 
        message_id (:obj:`int`):
            Identifier of the message to forward 
        in_game_share (:obj:`bool`):
            True, if a game message should be shared within a launched game; applies only to game messages

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageForwarded"

    def __init__(self, from_chat_id, message_id, in_game_share, **kwargs):
        
        self.from_chat_id = from_chat_id  # int
        self.message_id = message_id  # int
        self.in_game_share = in_game_share  # bool

    @staticmethod
    def read(q: dict, *args) -> "InputMessageForwarded":
        from_chat_id = q.get('from_chat_id')
        message_id = q.get('message_id')
        in_game_share = q.get('in_game_share')
        return InputMessageForwarded(from_chat_id, message_id, in_game_share)
