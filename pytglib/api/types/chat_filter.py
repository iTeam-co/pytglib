

from ..utils import Object


class ChatFilter(Object):
    """
    Represents a filter of user chats

    Attributes:
        ID (:obj:`str`): ``ChatFilter``

    Args:
        title (:obj:`str`):
            The title of the filter; 1-12 characters without line feeds
        icon_name (:obj:`str`):
            The chosen icon name for short filter representationIf non-empty, must be one of "All", "Unread", "Unmuted", "Bots", "Channels", "Groups", "Private", "Custom", "Setup", "Cat", "Crown", "Favorite", "Flower", "Game", "Home", "Love", "Mask", "Party", "Sport", "Study", "Trade", "Travel", "Work", "Airplane", "Book", "Light", "Like", "Money", "Note", "Palette"If empty, use getChatFilterDefaultIconName to get default icon name for the filter
        pinned_chat_ids (List of :obj:`int`):
            The chat identifiers of pinned chats in the filtered chat listThere can be up to GetOption("chat_filter_chosen_chat_count_max") pinned and always included non-secret chats and the same number of secret chats, but the limit can be increased with Telegram Premium
        included_chat_ids (List of :obj:`int`):
            The chat identifiers of always included chats in the filtered chat listThere can be up to GetOption("chat_filter_chosen_chat_count_max") pinned and always included non-secret chats and the same number of secret chats, but the limit can be increased with Telegram Premium
        excluded_chat_ids (List of :obj:`int`):
            The chat identifiers of always excluded chats in the filtered chat listThere can be up to GetOption("chat_filter_chosen_chat_count_max") always excluded non-secret chats and the same number of secret chats, but the limit can be increased with Telegram Premium
        exclude_muted (:obj:`bool`):
            True, if muted chats need to be excluded
        exclude_read (:obj:`bool`):
            True, if read chats need to be excluded
        exclude_archived (:obj:`bool`):
            True, if archived chats need to be excluded
        include_contacts (:obj:`bool`):
            True, if contacts need to be included
        include_non_contacts (:obj:`bool`):
            True, if non-contact users need to be included
        include_bots (:obj:`bool`):
            True, if bots need to be included
        include_groups (:obj:`bool`):
            True, if basic groups and supergroups need to be included
        include_channels (:obj:`bool`):
            True, if channels need to be included

    Returns:
        ChatFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatFilter"

    def __init__(self, title, icon_name, pinned_chat_ids, included_chat_ids, excluded_chat_ids, exclude_muted, exclude_read, exclude_archived, include_contacts, include_non_contacts, include_bots, include_groups, include_channels, **kwargs):
        
        self.title = title  # str
        self.icon_name = icon_name  # str
        self.pinned_chat_ids = pinned_chat_ids  # list of int
        self.included_chat_ids = included_chat_ids  # list of int
        self.excluded_chat_ids = excluded_chat_ids  # list of int
        self.exclude_muted = exclude_muted  # bool
        self.exclude_read = exclude_read  # bool
        self.exclude_archived = exclude_archived  # bool
        self.include_contacts = include_contacts  # bool
        self.include_non_contacts = include_non_contacts  # bool
        self.include_bots = include_bots  # bool
        self.include_groups = include_groups  # bool
        self.include_channels = include_channels  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatFilter":
        title = q.get('title')
        icon_name = q.get('icon_name')
        pinned_chat_ids = q.get('pinned_chat_ids')
        included_chat_ids = q.get('included_chat_ids')
        excluded_chat_ids = q.get('excluded_chat_ids')
        exclude_muted = q.get('exclude_muted')
        exclude_read = q.get('exclude_read')
        exclude_archived = q.get('exclude_archived')
        include_contacts = q.get('include_contacts')
        include_non_contacts = q.get('include_non_contacts')
        include_bots = q.get('include_bots')
        include_groups = q.get('include_groups')
        include_channels = q.get('include_channels')
        return ChatFilter(title, icon_name, pinned_chat_ids, included_chat_ids, excluded_chat_ids, exclude_muted, exclude_read, exclude_archived, include_contacts, include_non_contacts, include_bots, include_groups, include_channels)
