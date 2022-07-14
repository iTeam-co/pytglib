

from ..utils import Object


class MessageProximityAlertTriggered(Object):
    """
    A user in the chat came within proximity alert range 

    Attributes:
        ID (:obj:`str`): ``MessageProximityAlertTriggered``

    Args:
        traveler_id (:class:`telegram.api.types.MessageSender`):
            The identifier of a user or chat that triggered the proximity alert 
        watcher_id (:class:`telegram.api.types.MessageSender`):
            The identifier of a user or chat that subscribed for the proximity alert 
        distance (:obj:`int`):
            The distance between the users

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageProximityAlertTriggered"

    def __init__(self, traveler_id, watcher_id, distance, **kwargs):
        
        self.traveler_id = traveler_id  # MessageSender
        self.watcher_id = watcher_id  # MessageSender
        self.distance = distance  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageProximityAlertTriggered":
        traveler_id = Object.read(q.get('traveler_id'))
        watcher_id = Object.read(q.get('watcher_id'))
        distance = q.get('distance')
        return MessageProximityAlertTriggered(traveler_id, watcher_id, distance)
