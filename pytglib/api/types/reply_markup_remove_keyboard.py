

from ..utils import Object


class ReplyMarkupRemoveKeyboard(Object):
    """
    Instructs clients to remove the keyboard once this message has been received. This kind of keyboard can't be received in an incoming message; instead, UpdateChatReplyMarkup with message_id == 0 will be sent

    Attributes:
        ID (:obj:`str`): ``ReplyMarkupRemoveKeyboard``

    Args:
        is_personal (:obj:`bool`):
            True, if the keyboard is removed only for the mentioned users or the target user of a reply

    Returns:
        ReplyMarkup

    Raises:
        :class:`telegram.Error`
    """
    ID = "replyMarkupRemoveKeyboard"

    def __init__(self, is_personal, **kwargs):
        
        self.is_personal = is_personal  # bool

    @staticmethod
    def read(q: dict, *args) -> "ReplyMarkupRemoveKeyboard":
        is_personal = q.get('is_personal')
        return ReplyMarkupRemoveKeyboard(is_personal)
