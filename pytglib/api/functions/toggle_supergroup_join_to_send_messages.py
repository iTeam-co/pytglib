

from ..utils import Object


class ToggleSupergroupJoinToSendMessages(Object):
    """
    Toggles whether joining is mandatory to send messages to a discussion supergroup; requires can_restrict_members administrator right 

    Attributes:
        ID (:obj:`str`): ``ToggleSupergroupJoinToSendMessages``

    Args:
        supergroup_id (:obj:`int`):
            Identifier of the supergroup 
        join_to_send_messages (:obj:`bool`):
            New value of join_to_send_messages

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleSupergroupJoinToSendMessages"

    def __init__(self, supergroup_id, join_to_send_messages, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int
        self.join_to_send_messages = join_to_send_messages  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleSupergroupJoinToSendMessages":
        supergroup_id = q.get('supergroup_id')
        join_to_send_messages = q.get('join_to_send_messages')
        return ToggleSupergroupJoinToSendMessages(supergroup_id, join_to_send_messages)
