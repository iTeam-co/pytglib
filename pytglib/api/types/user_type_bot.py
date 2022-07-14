

from ..utils import Object


class UserTypeBot(Object):
    """
    A bot (see https://core.telegram.org/bots)

    Attributes:
        ID (:obj:`str`): ``UserTypeBot``

    Args:
        can_join_groups (:obj:`bool`):
            True, if the bot can be invited to basic group and supergroup chats
        can_read_all_group_messages (:obj:`bool`):
            True, if the bot can read all messages in basic group or supergroup chats and not just those addressed to the botIn private and channel chats a bot can always read all messages
        is_inline (:obj:`bool`):
            True, if the bot supports inline queries
        inline_query_placeholder (:obj:`str`):
            Placeholder for inline queries (displayed on the application input field)
        need_location (:obj:`bool`):
            True, if the location of the user is expected to be sent with every inline query to this bot
        can_be_added_to_attachment_menu (:obj:`bool`):
            True, if the bot can be added to attachment menu

    Returns:
        UserType

    Raises:
        :class:`telegram.Error`
    """
    ID = "userTypeBot"

    def __init__(self, can_join_groups, can_read_all_group_messages, is_inline, inline_query_placeholder, need_location, can_be_added_to_attachment_menu, **kwargs):
        
        self.can_join_groups = can_join_groups  # bool
        self.can_read_all_group_messages = can_read_all_group_messages  # bool
        self.is_inline = is_inline  # bool
        self.inline_query_placeholder = inline_query_placeholder  # str
        self.need_location = need_location  # bool
        self.can_be_added_to_attachment_menu = can_be_added_to_attachment_menu  # bool

    @staticmethod
    def read(q: dict, *args) -> "UserTypeBot":
        can_join_groups = q.get('can_join_groups')
        can_read_all_group_messages = q.get('can_read_all_group_messages')
        is_inline = q.get('is_inline')
        inline_query_placeholder = q.get('inline_query_placeholder')
        need_location = q.get('need_location')
        can_be_added_to_attachment_menu = q.get('can_be_added_to_attachment_menu')
        return UserTypeBot(can_join_groups, can_read_all_group_messages, is_inline, inline_query_placeholder, need_location, can_be_added_to_attachment_menu)
