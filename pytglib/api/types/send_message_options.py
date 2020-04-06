

from ..utils import Object


class SendMessageOptions(Object):
    """
    Options to be used when a message is send

    Attributes:
        ID (:obj:`str`): ``SendMessageOptions``

    Args:
        disable_notification (:obj:`bool`):
            Pass true to disable notification for the messageMust be false if the message is sent to a secret chat
        from_background (:obj:`bool`):
            Pass true if the message is sent from the background
        scheduling_state (:class:`telegram.api.types.MessageSchedulingState`):
            Message scheduling stateMessages sent to a secret chat, live location messages and self-destructing messages can't be scheduled

    Returns:
        SendMessageOptions

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendMessageOptions"

    def __init__(self, disable_notification, from_background, scheduling_state, **kwargs):
        
        self.disable_notification = disable_notification  # bool
        self.from_background = from_background  # bool
        self.scheduling_state = scheduling_state  # MessageSchedulingState

    @staticmethod
    def read(q: dict, *args) -> "SendMessageOptions":
        disable_notification = q.get('disable_notification')
        from_background = q.get('from_background')
        scheduling_state = Object.read(q.get('scheduling_state'))
        return SendMessageOptions(disable_notification, from_background, scheduling_state)
