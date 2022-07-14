

from ..utils import Object


class ChatMemberStatusCreator(Object):
    """
    The user is the owner of the chat and has all the administrator privileges

    Attributes:
        ID (:obj:`str`): ``ChatMemberStatusCreator``

    Args:
        custom_title (:obj:`str`):
            A custom title of the owner; 0-16 characters without emojis; applicable to supergroups only
        is_anonymous (:obj:`bool`):
            True, if the creator isn't shown in the chat member list and sends messages anonymously; applicable to supergroups only
        is_member (:obj:`bool`):
            True, if the user is a member of the chat

    Returns:
        ChatMemberStatus

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMemberStatusCreator"

    def __init__(self, custom_title, is_anonymous, is_member, **kwargs):
        
        self.custom_title = custom_title  # str
        self.is_anonymous = is_anonymous  # bool
        self.is_member = is_member  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatMemberStatusCreator":
        custom_title = q.get('custom_title')
        is_anonymous = q.get('is_anonymous')
        is_member = q.get('is_member')
        return ChatMemberStatusCreator(custom_title, is_anonymous, is_member)
