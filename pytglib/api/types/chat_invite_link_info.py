

from ..utils import Object


class ChatInviteLinkInfo(Object):
    """
    Contains information about a chat invite link

    Attributes:
        ID (:obj:`str`): ``ChatInviteLinkInfo``

    Args:
        chat_id (:obj:`int`):
            Chat identifier of the invite link; 0 if the user is not a member of this chat
        type (:class:`telegram.api.types.ChatType`):
            Contains information about the type of the chat
        title (:obj:`str`):
            Title of the chat
        photo (:class:`telegram.api.types.chatPhoto`):
            Chat photo; may be null
        member_count (:obj:`int`):
            Number of members in the chat
        member_user_ids (List of :obj:`int`):
            User identifiers of some chat members that may be known to the current user
        is_public (:obj:`bool`):
            True, if the chat is a public supergroup or channel, ieit has a username or it is a location-based supergroup

    Returns:
        ChatInviteLinkInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatInviteLinkInfo"

    def __init__(self, chat_id, type, title, photo, member_count, member_user_ids, is_public, **kwargs):
        
        self.chat_id = chat_id  # int
        self.type = type  # ChatType
        self.title = title  # str
        self.photo = photo  # ChatPhoto
        self.member_count = member_count  # int
        self.member_user_ids = member_user_ids  # list of int
        self.is_public = is_public  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatInviteLinkInfo":
        chat_id = q.get('chat_id')
        type = Object.read(q.get('type'))
        title = q.get('title')
        photo = Object.read(q.get('photo'))
        member_count = q.get('member_count')
        member_user_ids = q.get('member_user_ids')
        is_public = q.get('is_public')
        return ChatInviteLinkInfo(chat_id, type, title, photo, member_count, member_user_ids, is_public)
