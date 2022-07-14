

from ..utils import Object


class BanChatMember(Object):
    """
    Bans a member in a chat. Members can't be banned in private or secret chats. In supergroups and channels, the user will not be able to return to the group on their own using invite links, etc., unless unbanned first

    Attributes:
        ID (:obj:`str`): ``BanChatMember``

    Args:
        chat_id (:obj:`int`):
            Chat identifier
        member_id (:class:`telegram.api.types.MessageSender`):
            Member identifier
        banned_until_date (:obj:`int`):
            Point in time (Unix timestamp) when the user will be unbanned; 0 if neverIf the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned foreverIgnored in basic groups and if a chat is banned
        revoke_messages (:obj:`bool`):
            Pass true to delete all messages in the chat for the user that is being removedAlways true for supergroups and channels

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "banChatMember"

    def __init__(self, chat_id, member_id, banned_until_date, revoke_messages, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.member_id = member_id  # MessageSender
        self.banned_until_date = banned_until_date  # int
        self.revoke_messages = revoke_messages  # bool

    @staticmethod
    def read(q: dict, *args) -> "BanChatMember":
        chat_id = q.get('chat_id')
        member_id = Object.read(q.get('member_id'))
        banned_until_date = q.get('banned_until_date')
        revoke_messages = q.get('revoke_messages')
        return BanChatMember(chat_id, member_id, banned_until_date, revoke_messages)
