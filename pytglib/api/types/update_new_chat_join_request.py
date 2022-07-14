

from ..utils import Object


class UpdateNewChatJoinRequest(Object):
    """
    A user sent a join request to a chat; for bots only 

    Attributes:
        ID (:obj:`str`): ``UpdateNewChatJoinRequest``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        request (:class:`telegram.api.types.chatJoinRequest`):
            Join request 
        invite_link (:class:`telegram.api.types.chatInviteLink`):
            The invite link, which was used to send join request; may be null

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateNewChatJoinRequest"

    def __init__(self, chat_id, request, invite_link, **kwargs):
        
        self.chat_id = chat_id  # int
        self.request = request  # ChatJoinRequest
        self.invite_link = invite_link  # ChatInviteLink

    @staticmethod
    def read(q: dict, *args) -> "UpdateNewChatJoinRequest":
        chat_id = q.get('chat_id')
        request = Object.read(q.get('request'))
        invite_link = Object.read(q.get('invite_link'))
        return UpdateNewChatJoinRequest(chat_id, request, invite_link)
