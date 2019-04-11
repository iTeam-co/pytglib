

from ..utils import Object


class ReplyMarkupForceReply(Object):
    """
    Instructs clients to force a reply to this message

    Attributes:
        ID (:obj:`str`): ``ReplyMarkupForceReply``

    Args:
        is_personal (:obj:`bool`):
            True, if a forced reply must automatically be shown to the current userFor outgoing messages, specify true to show the forced reply only for the mentioned users and for the target user of a reply

    Returns:
        ReplyMarkup

    Raises:
        :class:`telegram.Error`
    """
    ID = "replyMarkupForceReply"

    def __init__(self, is_personal, **kwargs):
        
        self.is_personal = is_personal  # bool

    @staticmethod
    def read(q: dict, *args) -> "ReplyMarkupForceReply":
        is_personal = q.get('is_personal')
        return ReplyMarkupForceReply(is_personal)
