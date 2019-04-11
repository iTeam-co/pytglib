

from ..utils import Object


class ChatEventLogFilters(Object):
    """
    Represents a set of filters used to obtain a chat event log

    Attributes:
        ID (:obj:`str`): ``ChatEventLogFilters``

    Args:
        message_edits (:obj:`bool`):
            True, if message edits should be returned
        message_deletions (:obj:`bool`):
            True, if message deletions should be returned
        message_pins (:obj:`bool`):
            True, if pin/unpin events should be returned
        member_joins (:obj:`bool`):
            True, if members joining events should be returned
        member_leaves (:obj:`bool`):
            True, if members leaving events should be returned
        member_invites (:obj:`bool`):
            True, if invited member events should be returned
        member_promotions (:obj:`bool`):
            True, if member promotion/demotion events should be returned
        member_restrictions (:obj:`bool`):
            True, if member restricted/unrestricted/banned/unbanned events should be returned
        info_changes (:obj:`bool`):
            True, if changes in chat information should be returned
        setting_changes (:obj:`bool`):
            True, if changes in chat settings should be returned

    Returns:
        ChatEventLogFilters

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventLogFilters"

    def __init__(self, message_edits, message_deletions, message_pins, member_joins, member_leaves, member_invites, member_promotions, member_restrictions, info_changes, setting_changes, **kwargs):
        
        self.message_edits = message_edits  # bool
        self.message_deletions = message_deletions  # bool
        self.message_pins = message_pins  # bool
        self.member_joins = member_joins  # bool
        self.member_leaves = member_leaves  # bool
        self.member_invites = member_invites  # bool
        self.member_promotions = member_promotions  # bool
        self.member_restrictions = member_restrictions  # bool
        self.info_changes = info_changes  # bool
        self.setting_changes = setting_changes  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatEventLogFilters":
        message_edits = q.get('message_edits')
        message_deletions = q.get('message_deletions')
        message_pins = q.get('message_pins')
        member_joins = q.get('member_joins')
        member_leaves = q.get('member_leaves')
        member_invites = q.get('member_invites')
        member_promotions = q.get('member_promotions')
        member_restrictions = q.get('member_restrictions')
        info_changes = q.get('info_changes')
        setting_changes = q.get('setting_changes')
        return ChatEventLogFilters(message_edits, message_deletions, message_pins, member_joins, member_leaves, member_invites, member_promotions, member_restrictions, info_changes, setting_changes)
