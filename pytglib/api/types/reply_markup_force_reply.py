

from ..utils import Object


class ReplyMarkupForceReply(Object):
    """
    Instructs application to force a reply to this message

    Attributes:
        ID (:obj:`str`): ``ReplyMarkupForceReply``

    Args:
        is_personal (:obj:`bool`):
            True, if a forced reply must automatically be shown to the current userFor outgoing messages, specify true to show the forced reply only for the mentioned users and for the target user of a reply
        input_field_placeholder (:obj:`str`):
            If non-empty, the placeholder to be shown in the input field when the reply is active; 0-64 characters

    Returns:
        ReplyMarkup

    Raises:
        :class:`telegram.Error`
    """
    ID = "replyMarkupForceReply"

    def __init__(self, is_personal, input_field_placeholder, **kwargs):
        
        self.is_personal = is_personal  # bool
        self.input_field_placeholder = input_field_placeholder  # str

    @staticmethod
    def read(q: dict, *args) -> "ReplyMarkupForceReply":
        is_personal = q.get('is_personal')
        input_field_placeholder = q.get('input_field_placeholder')
        return ReplyMarkupForceReply(is_personal, input_field_placeholder)
