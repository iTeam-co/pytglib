

from ..utils import Object


class EditMessageLiveLocation(Object):
    """
    Edits the message content of a live location. Messages can be edited for a limited period of time specified in the live location. Returns the edited message after the edit is completed on the server side

    Attributes:
        ID (:obj:`str`): ``EditMessageLiveLocation``

    Args:
        chat_id (:obj:`int`):
            The chat the message belongs to
        message_id (:obj:`int`):
            Identifier of the message
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The new message reply markup; pass null if none; for bots only
        location (:class:`telegram.api.types.location`):
            New location content of the message; pass null to stop sharing the live location
        heading (:obj:`int`):
            The new direction in which the location moves, in degrees; 1-360Pass 0 if unknown
        proximity_alert_radius (:obj:`int`):
            The new maximum distance for proximity alerts, in meters (0-100000)Pass 0 if the notification is disabled

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "editMessageLiveLocation"

    def __init__(self, chat_id, message_id, reply_markup, location, heading, proximity_alert_radius, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.location = location  # Location
        self.heading = heading  # int
        self.proximity_alert_radius = proximity_alert_radius  # int

    @staticmethod
    def read(q: dict, *args) -> "EditMessageLiveLocation":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        reply_markup = Object.read(q.get('reply_markup'))
        location = Object.read(q.get('location'))
        heading = q.get('heading')
        proximity_alert_radius = q.get('proximity_alert_radius')
        return EditMessageLiveLocation(chat_id, message_id, reply_markup, location, heading, proximity_alert_radius)
