

from ..utils import Object


class ChatEventVideoChatEnded(Object):
    """
    A video chat was ended 

    Attributes:
        ID (:obj:`str`): ``ChatEventVideoChatEnded``

    Args:
        group_call_id (:obj:`int`):
            Identifier of the video chatThe video chat can be received through the method getGroupCall

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventVideoChatEnded"

    def __init__(self, group_call_id, **kwargs):
        
        self.group_call_id = group_call_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatEventVideoChatEnded":
        group_call_id = q.get('group_call_id')
        return ChatEventVideoChatEnded(group_call_id)
