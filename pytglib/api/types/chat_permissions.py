

from ..utils import Object


class ChatPermissions(Object):
    """
    Describes actions that a user is allowed to take in a chat

    Attributes:
        ID (:obj:`str`): ``ChatPermissions``

    Args:
        can_send_messages (:obj:`bool`):
            True, if the user can send text messages, contacts, locations, and venues
        can_send_media_messages (:obj:`bool`):
            True, if the user can send audio files, documents, photos, videos, video notes, and voice notesImplies can_send_messages permissions
        can_send_polls (:obj:`bool`):
            True, if the user can send pollsImplies can_send_messages permissions
        can_send_other_messages (:obj:`bool`):
            True, if the user can send animations, games, and stickers and use inline botsImplies can_send_messages permissions
        can_add_web_page_previews (:obj:`bool`):
            True, if the user may add a web page preview to their messagesImplies can_send_messages permissions
        can_change_info (:obj:`bool`):
            True, if the user can change the chat title, photo, and other settings
        can_invite_users (:obj:`bool`):
            True, if the user can invite new users to the chat
        can_pin_messages (:obj:`bool`):
            True, if the user can pin messages

    Returns:
        ChatPermissions

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatPermissions"

    def __init__(self, can_send_messages, can_send_media_messages, can_send_polls, can_send_other_messages, can_add_web_page_previews, can_change_info, can_invite_users, can_pin_messages, **kwargs):
        
        self.can_send_messages = can_send_messages  # bool
        self.can_send_media_messages = can_send_media_messages  # bool
        self.can_send_polls = can_send_polls  # bool
        self.can_send_other_messages = can_send_other_messages  # bool
        self.can_add_web_page_previews = can_add_web_page_previews  # bool
        self.can_change_info = can_change_info  # bool
        self.can_invite_users = can_invite_users  # bool
        self.can_pin_messages = can_pin_messages  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatPermissions":
        can_send_messages = q.get('can_send_messages')
        can_send_media_messages = q.get('can_send_media_messages')
        can_send_polls = q.get('can_send_polls')
        can_send_other_messages = q.get('can_send_other_messages')
        can_add_web_page_previews = q.get('can_add_web_page_previews')
        can_change_info = q.get('can_change_info')
        can_invite_users = q.get('can_invite_users')
        can_pin_messages = q.get('can_pin_messages')
        return ChatPermissions(can_send_messages, can_send_media_messages, can_send_polls, can_send_other_messages, can_add_web_page_previews, can_change_info, can_invite_users, can_pin_messages)
