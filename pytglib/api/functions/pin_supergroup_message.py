

from ..utils import Object


class PinSupergroupMessage(Object):
    """
    Pins a message in a supergroup or channel; requires appropriate administrator rights in the supergroup or channel 

    Attributes:
        ID (:obj:`str`): ``PinSupergroupMessage``

    Args:
        supergroup_id (:obj:`int`):
            Identifier of the supergroup or channel 
        message_id (:obj:`int`):
            Identifier of the new pinned message 
        disable_notification (:obj:`bool`):
            True, if there should be no notification about the pinned message

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "pinSupergroupMessage"

    def __init__(self, supergroup_id, message_id, disable_notification, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int
        self.message_id = message_id  # int
        self.disable_notification = disable_notification  # bool

    @staticmethod
    def read(q: dict, *args) -> "PinSupergroupMessage":
        supergroup_id = q.get('supergroup_id')
        message_id = q.get('message_id')
        disable_notification = q.get('disable_notification')
        return PinSupergroupMessage(supergroup_id, message_id, disable_notification)
