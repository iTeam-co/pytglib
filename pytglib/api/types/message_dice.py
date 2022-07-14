

from ..utils import Object


class MessageDice(Object):
    """
    A dice message. The dice value is randomly generated by the server

    Attributes:
        ID (:obj:`str`): ``MessageDice``

    Args:
        initial_state (:class:`telegram.api.types.DiceStickers`):
            The animated stickers with the initial dice animation; may be null if unknownupdateMessageContent will be sent when the sticker became known
        final_state (:class:`telegram.api.types.DiceStickers`):
            The animated stickers with the final dice animation; may be null if unknownupdateMessageContent will be sent when the sticker became known
        emoji (:obj:`str`):
            Emoji on which the dice throw animation is based
        value (:obj:`int`):
            The dice valueIf the value is 0, the dice don't have final state yet
        success_animation_frame_number (:obj:`int`):
            Number of frame after which a success animation like a shower of confetti needs to be shown on updateMessageSendSucceeded

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageDice"

    def __init__(self, initial_state, final_state, emoji, value, success_animation_frame_number, **kwargs):
        
        self.initial_state = initial_state  # DiceStickers
        self.final_state = final_state  # DiceStickers
        self.emoji = emoji  # str
        self.value = value  # int
        self.success_animation_frame_number = success_animation_frame_number  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageDice":
        initial_state = Object.read(q.get('initial_state'))
        final_state = Object.read(q.get('final_state'))
        emoji = q.get('emoji')
        value = q.get('value')
        success_animation_frame_number = q.get('success_animation_frame_number')
        return MessageDice(initial_state, final_state, emoji, value, success_animation_frame_number)
