

from ..utils import Object


class EditMessageSchedulingState(Object):
    """
    Edits the time when a scheduled message will be sent. Scheduling state of all messages in the same album or forwarded together with the message will be also changed 

    Attributes:
        ID (:obj:`str`): ``EditMessageSchedulingState``

    Args:
        chat_id (:obj:`int`):
            The chat the message belongs to 
        message_id (:obj:`int`):
            Identifier of the message 
        scheduling_state (:class:`telegram.api.types.MessageSchedulingState`):
            The new message scheduling statePass null to send the message immediately

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "editMessageSchedulingState"

    def __init__(self, chat_id, message_id, scheduling_state, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.scheduling_state = scheduling_state  # MessageSchedulingState

    @staticmethod
    def read(q: dict, *args) -> "EditMessageSchedulingState":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        scheduling_state = Object.read(q.get('scheduling_state'))
        return EditMessageSchedulingState(chat_id, message_id, scheduling_state)
