

from ..utils import Object


class EditInlineMessageLiveLocation(Object):
    """
    Edits the content of a live location in an inline message sent via a bot; for bots only 

    Attributes:
        ID (:obj:`str`): ``EditInlineMessageLiveLocation``

    Args:
        inline_message_id (:obj:`str`):
            Inline message identifier 
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The new message reply markup 
        location (:class:`telegram.api.types.location`):
            New location content of the message; may be nullPass null to stop sharing the live location

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "editInlineMessageLiveLocation"

    def __init__(self, inline_message_id, reply_markup, location, extra=None, **kwargs):
        self.extra = extra
        self.inline_message_id = inline_message_id  # str
        self.reply_markup = reply_markup  # ReplyMarkup
        self.location = location  # Location

    @staticmethod
    def read(q: dict, *args) -> "EditInlineMessageLiveLocation":
        inline_message_id = q.get('inline_message_id')
        reply_markup = Object.read(q.get('reply_markup'))
        location = Object.read(q.get('location'))
        return EditInlineMessageLiveLocation(inline_message_id, reply_markup, location)
