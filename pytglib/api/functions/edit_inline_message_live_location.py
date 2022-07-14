

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
            The new message reply markup; pass null if none
        location (:class:`telegram.api.types.location`):
            New location content of the message; pass null to stop sharing the live location
        heading (:obj:`int`):
            The new direction in which the location moves, in degrees; 1-360Pass 0 if unknown
        proximity_alert_radius (:obj:`int`):
            The new maximum distance for proximity alerts, in meters (0-100000)Pass 0 if the notification is disabled

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "editInlineMessageLiveLocation"

    def __init__(self, inline_message_id, reply_markup, location, heading, proximity_alert_radius, extra=None, **kwargs):
        self.extra = extra
        self.inline_message_id = inline_message_id  # str
        self.reply_markup = reply_markup  # ReplyMarkup
        self.location = location  # Location
        self.heading = heading  # int
        self.proximity_alert_radius = proximity_alert_radius  # int

    @staticmethod
    def read(q: dict, *args) -> "EditInlineMessageLiveLocation":
        inline_message_id = q.get('inline_message_id')
        reply_markup = Object.read(q.get('reply_markup'))
        location = Object.read(q.get('location'))
        heading = q.get('heading')
        proximity_alert_radius = q.get('proximity_alert_radius')
        return EditInlineMessageLiveLocation(inline_message_id, reply_markup, location, heading, proximity_alert_radius)
