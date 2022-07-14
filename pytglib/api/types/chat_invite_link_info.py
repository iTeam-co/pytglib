

from ..utils import Object


class ChatInviteLinkInfo(Object):
    """
    Contains information about a chat invite link

    Attributes:
        ID (:obj:`str`): ``ChatInviteLinkInfo``

    Args:
        chat_id (:obj:`int`):
            Chat identifier of the invite link; 0 if the user has no access to the chat before joining
        accessible_for (:obj:`int`):
            If non-zero, the amount of time for which read access to the chat will remain available, in seconds
        type (:class:`telegram.api.types.ChatType`):
            Type of the chat
        title (:obj:`str`):
            Title of the chat
        photo (:class:`telegram.api.types.chatPhotoInfo`):
            Chat photo; may be null
        description (:obj:`str`):
            Chat description
        member_count (:obj:`int`):
            Number of members in the chat
        member_user_ids (List of :obj:`int`):
            User identifiers of some chat members that may be known to the current user
        creates_join_request (:obj:`bool`):
            True, if the link only creates join request
        is_public (:obj:`bool`):
            True, if the chat is a public supergroup or channel, ieit has a username or it is a location-based supergroup

    Returns:
        ChatInviteLinkInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatInviteLinkInfo"

    def __init__(self, chat_id, accessible_for, type, title, photo, description, member_count, member_user_ids, creates_join_request, is_public, **kwargs):
        
        self.chat_id = chat_id  # int
        self.accessible_for = accessible_for  # int
        self.type = type  # ChatType
        self.title = title  # str
        self.photo = photo  # ChatPhotoInfo
        self.description = description  # str
        self.member_count = member_count  # int
        self.member_user_ids = member_user_ids  # list of int
        self.creates_join_request = creates_join_request  # bool
        self.is_public = is_public  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatInviteLinkInfo":
        chat_id = q.get('chat_id')
        accessible_for = q.get('accessible_for')
        type = Object.read(q.get('type'))
        title = q.get('title')
        photo = Object.read(q.get('photo'))
        description = q.get('description')
        member_count = q.get('member_count')
        member_user_ids = q.get('member_user_ids')
        creates_join_request = q.get('creates_join_request')
        is_public = q.get('is_public')
        return ChatInviteLinkInfo(chat_id, accessible_for, type, title, photo, description, member_count, member_user_ids, creates_join_request, is_public)
