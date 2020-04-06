

from ..utils import Object


class SupergroupFullInfo(Object):
    """
    Contains full information about a supergroup or channel

    Attributes:
        ID (:obj:`str`): ``SupergroupFullInfo``

    Args:
        description (:obj:`str`):
            Supergroup or channel description
        member_count (:obj:`int`):
            Number of members in the supergroup or channel; 0 if unknown
        administrator_count (:obj:`int`):
            Number of privileged users in the supergroup or channel; 0 if unknown
        restricted_count (:obj:`int`):
            Number of restricted users in the supergroup; 0 if unknown
        banned_count (:obj:`int`):
            Number of users banned from chat; 0 if unknown
        linked_chat_id (:obj:`int`):
            Chat identifier of a discussion group for the channel, or a channel, for which the supergroup is the designated discussion group; 0 if none or unknown
        slow_mode_delay (:obj:`int`):
            Delay between consecutive sent messages for non-administrator supergroup members, in seconds
        slow_mode_delay_expires_in (:obj:`float`):
            Time left before next message can be sent in the supergroup, in secondsAn updateSupergroupFullInfo update is not triggered when value of this field changes, but both new and old values are non-zero
        can_get_members (:obj:`bool`):
            True, if members of the chat can be retrieved
        can_set_username (:obj:`bool`):
            True, if the chat username can be changed
        can_set_sticker_set (:obj:`bool`):
            True, if the supergroup sticker set can be changed
        can_set_location (:obj:`bool`):
            True, if the supergroup location can be changed
        can_view_statistics (:obj:`bool`):
            True, if the channel statistics is available
        is_all_history_available (:obj:`bool`):
            True, if new chat members will have access to old messagesIn public or discussion groups and both public and private channels, old messages are always available, so this option affects only private supergroups without a linked chatThe value of this field is only available for chat administrators
        sticker_set_id (:obj:`int`):
            Identifier of the supergroup sticker set; 0 if none
        location (:class:`telegram.api.types.chatLocation`):
            Location to which the supergroup is connected; may be null
        invite_link (:obj:`str`):
            Invite link for this chat
        upgraded_from_basic_group_id (:obj:`int`):
            Identifier of the basic group from which supergroup was upgraded; 0 if none
        upgraded_from_max_message_id (:obj:`int`):
            Identifier of the last message in the basic group from which supergroup was upgraded; 0 if none

    Returns:
        SupergroupFullInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "supergroupFullInfo"

    def __init__(self, description, member_count, administrator_count, restricted_count, banned_count, linked_chat_id, slow_mode_delay, slow_mode_delay_expires_in, can_get_members, can_set_username, can_set_sticker_set, can_set_location, can_view_statistics, is_all_history_available, sticker_set_id, location, invite_link, upgraded_from_basic_group_id, upgraded_from_max_message_id, **kwargs):
        
        self.description = description  # str
        self.member_count = member_count  # int
        self.administrator_count = administrator_count  # int
        self.restricted_count = restricted_count  # int
        self.banned_count = banned_count  # int
        self.linked_chat_id = linked_chat_id  # int
        self.slow_mode_delay = slow_mode_delay  # int
        self.slow_mode_delay_expires_in = slow_mode_delay_expires_in  # float
        self.can_get_members = can_get_members  # bool
        self.can_set_username = can_set_username  # bool
        self.can_set_sticker_set = can_set_sticker_set  # bool
        self.can_set_location = can_set_location  # bool
        self.can_view_statistics = can_view_statistics  # bool
        self.is_all_history_available = is_all_history_available  # bool
        self.sticker_set_id = sticker_set_id  # int
        self.location = location  # ChatLocation
        self.invite_link = invite_link  # str
        self.upgraded_from_basic_group_id = upgraded_from_basic_group_id  # int
        self.upgraded_from_max_message_id = upgraded_from_max_message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "SupergroupFullInfo":
        description = q.get('description')
        member_count = q.get('member_count')
        administrator_count = q.get('administrator_count')
        restricted_count = q.get('restricted_count')
        banned_count = q.get('banned_count')
        linked_chat_id = q.get('linked_chat_id')
        slow_mode_delay = q.get('slow_mode_delay')
        slow_mode_delay_expires_in = q.get('slow_mode_delay_expires_in')
        can_get_members = q.get('can_get_members')
        can_set_username = q.get('can_set_username')
        can_set_sticker_set = q.get('can_set_sticker_set')
        can_set_location = q.get('can_set_location')
        can_view_statistics = q.get('can_view_statistics')
        is_all_history_available = q.get('is_all_history_available')
        sticker_set_id = q.get('sticker_set_id')
        location = Object.read(q.get('location'))
        invite_link = q.get('invite_link')
        upgraded_from_basic_group_id = q.get('upgraded_from_basic_group_id')
        upgraded_from_max_message_id = q.get('upgraded_from_max_message_id')
        return SupergroupFullInfo(description, member_count, administrator_count, restricted_count, banned_count, linked_chat_id, slow_mode_delay, slow_mode_delay_expires_in, can_get_members, can_set_username, can_set_sticker_set, can_set_location, can_view_statistics, is_all_history_available, sticker_set_id, location, invite_link, upgraded_from_basic_group_id, upgraded_from_max_message_id)
