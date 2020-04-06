

from ..utils import Object


class ToggleSupergroupSignMessages(Object):
    """
    Toggles sender signatures messages sent in a channel; requires can_change_info rights 

    Attributes:
        ID (:obj:`str`): ``ToggleSupergroupSignMessages``

    Args:
        supergroup_id (:obj:`int`):
            Identifier of the channel 
        sign_messages (:obj:`bool`):
            New value of sign_messages

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleSupergroupSignMessages"

    def __init__(self, supergroup_id, sign_messages, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int
        self.sign_messages = sign_messages  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleSupergroupSignMessages":
        supergroup_id = q.get('supergroup_id')
        sign_messages = q.get('sign_messages')
        return ToggleSupergroupSignMessages(supergroup_id, sign_messages)
