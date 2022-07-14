

from ..utils import Object


class MessageVideoChatStarted(Object):
    """
    A newly created video chat 

    Attributes:
        ID (:obj:`str`): ``MessageVideoChatStarted``

    Args:
        group_call_id (:obj:`int`):
            Identifier of the video chatThe video chat can be received through the method getGroupCall

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageVideoChatStarted"

    def __init__(self, group_call_id, **kwargs):
        
        self.group_call_id = group_call_id  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageVideoChatStarted":
        group_call_id = q.get('group_call_id')
        return MessageVideoChatStarted(group_call_id)
