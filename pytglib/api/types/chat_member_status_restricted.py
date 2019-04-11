

from ..utils import Object


class ChatMemberStatusRestricted(Object):
    """
    The user is under certain restrictions in the chat. Not supported in basic groups and channels

    Attributes:
        ID (:obj:`str`): ``ChatMemberStatusRestricted``

    Args:
        is_member (:obj:`bool`):
            True, if the user is a member of the chat
        restricted_until_date (:obj:`int`):
            Point in time (Unix timestamp) when restrictions will be lifted from the user; 0 if neverIf the user is restricted for more than 366 days or for less than 30 seconds from the current time, the user is considered to be restricted forever
        can_send_messages (:obj:`bool`):
            True, if the user can send text messages, contacts, locations, and venues
        can_send_media_messages (:obj:`bool`):
            True, if the user can send audio files, documents, photos, videos, video notes, and voice notesImplies can_send_messages permissions
        can_send_other_messages (:obj:`bool`):
            True, if the user can send animations, games, and stickers and use inline botsImplies can_send_media_messages permissions
        can_add_web_page_previews (:obj:`bool`):
            True, if the user may add a web page preview to his messagesImplies can_send_messages permissions

    Returns:
        ChatMemberStatus

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMemberStatusRestricted"

    def __init__(self, is_member, restricted_until_date, can_send_messages, can_send_media_messages, can_send_other_messages, can_add_web_page_previews, **kwargs):
        
        self.is_member = is_member  # bool
        self.restricted_until_date = restricted_until_date  # int
        self.can_send_messages = can_send_messages  # bool
        self.can_send_media_messages = can_send_media_messages  # bool
        self.can_send_other_messages = can_send_other_messages  # bool
        self.can_add_web_page_previews = can_add_web_page_previews  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatMemberStatusRestricted":
        is_member = q.get('is_member')
        restricted_until_date = q.get('restricted_until_date')
        can_send_messages = q.get('can_send_messages')
        can_send_media_messages = q.get('can_send_media_messages')
        can_send_other_messages = q.get('can_send_other_messages')
        can_add_web_page_previews = q.get('can_add_web_page_previews')
        return ChatMemberStatusRestricted(is_member, restricted_until_date, can_send_messages, can_send_media_messages, can_send_other_messages, can_add_web_page_previews)
