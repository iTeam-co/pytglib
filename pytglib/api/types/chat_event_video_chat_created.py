

from ..utils import Object


class ChatEventVideoChatCreated(Object):
    """
    A video chat was created 

    Attributes:
        ID (:obj:`str`): ``ChatEventVideoChatCreated``

    Args:
        group_call_id (:obj:`int`):
            Identifier of the video chatThe video chat can be received through the method getGroupCall

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventVideoChatCreated"

    def __init__(self, group_call_id, **kwargs):
        
        self.group_call_id = group_call_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatEventVideoChatCreated":
        group_call_id = q.get('group_call_id')
        return ChatEventVideoChatCreated(group_call_id)
