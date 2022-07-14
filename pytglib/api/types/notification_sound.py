

from ..utils import Object


class NotificationSound(Object):
    """
    Describes a notification sound in MP3 format

    Attributes:
        ID (:obj:`str`): ``NotificationSound``

    Args:
        id (:obj:`int`):
            Unique identifier of the notification sound
        duration (:obj:`int`):
            Duration of the sound, in seconds
        date (:obj:`int`):
            Point in time (Unix timestamp) when the sound was created
        title (:obj:`str`):
            Title of the notification sound
        data (:obj:`str`):
            Arbitrary data, defined while the sound was uploaded
        sound (:class:`telegram.api.types.file`):
            File containing the sound

    Returns:
        NotificationSound

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationSound"

    def __init__(self, id, duration, date, title, data, sound, **kwargs):
        
        self.id = id  # int
        self.duration = duration  # int
        self.date = date  # int
        self.title = title  # str
        self.data = data  # str
        self.sound = sound  # File

    @staticmethod
    def read(q: dict, *args) -> "NotificationSound":
        id = q.get('id')
        duration = q.get('duration')
        date = q.get('date')
        title = q.get('title')
        data = q.get('data')
        sound = Object.read(q.get('sound'))
        return NotificationSound(id, duration, date, title, data, sound)
