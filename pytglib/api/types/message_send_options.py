

from ..utils import Object


class MessageSendOptions(Object):
    """
    Options to be used when a message is sent

    Attributes:
        ID (:obj:`str`): ``MessageSendOptions``

    Args:
        disable_notification (:obj:`bool`):
            Pass true to disable notification for the message
        from_background (:obj:`bool`):
            Pass true if the message is sent from the background
        protect_content (:obj:`bool`):
            Pass true if the content of the message must be protected from forwarding and saving; for bots only
        scheduling_state (:class:`telegram.api.types.MessageSchedulingState`):
            Message scheduling state; pass null to send message immediatelyMessages sent to a secret chat, live location messages and self-destructing messages can't be scheduled

    Returns:
        MessageSendOptions

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageSendOptions"

    def __init__(self, disable_notification, from_background, protect_content, scheduling_state, **kwargs):
        
        self.disable_notification = disable_notification  # bool
        self.from_background = from_background  # bool
        self.protect_content = protect_content  # bool
        self.scheduling_state = scheduling_state  # MessageSchedulingState

    @staticmethod
    def read(q: dict, *args) -> "MessageSendOptions":
        disable_notification = q.get('disable_notification')
        from_background = q.get('from_background')
        protect_content = q.get('protect_content')
        scheduling_state = Object.read(q.get('scheduling_state'))
        return MessageSendOptions(disable_notification, from_background, protect_content, scheduling_state)
