

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
            True, if a game message is being shared from a launched game; applies only to game messages
        copy_options (:class:`telegram.api.types.messageCopyOptions`):
            Options to be used to copy content of the message without reference to the original sender; pass null to forward the message as usual

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageForwarded"

    def __init__(self, from_chat_id, message_id, in_game_share, copy_options, **kwargs):
        
        self.from_chat_id = from_chat_id  # int
        self.message_id = message_id  # int
        self.in_game_share = in_game_share  # bool
        self.copy_options = copy_options  # MessageCopyOptions

    @staticmethod
    def read(q: dict, *args) -> "InputMessageForwarded":
        from_chat_id = q.get('from_chat_id')
        message_id = q.get('message_id')
        in_game_share = q.get('in_game_share')
        copy_options = Object.read(q.get('copy_options'))
        return InputMessageForwarded(from_chat_id, message_id, in_game_share, copy_options)
