

from ..utils import Object


class UpdateChatMember(Object):
    """
    User rights changed in a chat; for bots only 

    Attributes:
        ID (:obj:`str`): ``UpdateChatMember``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        actor_user_id (:obj:`int`):
            Identifier of the user, changing the rights
        date (:obj:`int`):
            Point in time (Unix timestamp) when the user rights was changed 
        invite_link (:class:`telegram.api.types.chatInviteLink`):
            If user has joined the chat using an invite link, the invite link; may be null
        old_chat_member (:class:`telegram.api.types.chatMember`):
            Previous chat member 
        new_chat_member (:class:`telegram.api.types.chatMember`):
            New chat member

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatMember"

    def __init__(self, chat_id, actor_user_id, date, invite_link, old_chat_member, new_chat_member, **kwargs):
        
        self.chat_id = chat_id  # int
        self.actor_user_id = actor_user_id  # int
        self.date = date  # int
        self.invite_link = invite_link  # ChatInviteLink
        self.old_chat_member = old_chat_member  # ChatMember
        self.new_chat_member = new_chat_member  # ChatMember

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatMember":
        chat_id = q.get('chat_id')
        actor_user_id = q.get('actor_user_id')
        date = q.get('date')
        invite_link = Object.read(q.get('invite_link'))
        old_chat_member = Object.read(q.get('old_chat_member'))
        new_chat_member = Object.read(q.get('new_chat_member'))
        return UpdateChatMember(chat_id, actor_user_id, date, invite_link, old_chat_member, new_chat_member)
