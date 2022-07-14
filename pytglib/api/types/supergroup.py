

from ..utils import Object


class Supergroup(Object):
    """
    Represents a supergroup or channel with zero or more members (subscribers in the case of channels). From the point of view of the system, a channel is a special kind of a supergroup: only administrators can post and see the list of members, and posts from all administrators use the name and photo of the channel instead of individual names and profile photos. Unlike supergroups, channels can have an unlimited number of subscribers

    Attributes:
        ID (:obj:`str`): ``Supergroup``

    Args:
        id (:obj:`int`):
            Supergroup or channel identifier
        username (:obj:`str`):
            Username of the supergroup or channel; empty for private supergroups or channels
        date (:obj:`int`):
            Point in time (Unix timestamp) when the current user joined, or the point in time when the supergroup or channel was created, in case the user is not a member
        status (:class:`telegram.api.types.ChatMemberStatus`):
            Status of the current user in the supergroup or channel; custom title will be always empty
        member_count (:obj:`int`):
            Number of members in the supergroup or channel; 0 if unknownCurrently, it is guaranteed to be known only if the supergroup or channel was received through searchPublicChats, searchChatsNearby, getInactiveSupergroupChats, getSuitableDiscussionChats, getGroupsInCommon, or getUserPrivacySettingRules
        has_linked_chat (:obj:`bool`):
            True, if the channel has a discussion group, or the supergroup is the designated discussion group for a channel
        has_location (:obj:`bool`):
            True, if the supergroup is connected to a location, iethe supergroup is a location-based supergroup
        sign_messages (:obj:`bool`):
            True, if messages sent to the channel need to contain information about the senderThis field is only applicable to channels
        join_to_send_messages (:obj:`bool`):
            True, if users need to join the supergroup before they can send messagesAlways true for channels and non-discussion supergroups
        join_by_request (:obj:`bool`):
            True, if all users directly joining the supergroup need to be approved by supergroup administratorsAlways false for channels and supergroups without username, location, or a linked chat
        is_slow_mode_enabled (:obj:`bool`):
            True, if the slow mode is enabled in the supergroup
        is_channel (:obj:`bool`):
            True, if the supergroup is a channel
        is_broadcast_group (:obj:`bool`):
            True, if the supergroup is a broadcast group, ieonly administrators can send messages and there is no limit on the number of members
        is_verified (:obj:`bool`):
            True, if the supergroup or channel is verified
        restriction_reason (:obj:`str`):
            If non-empty, contains a human-readable description of the reason why access to this supergroup or channel must be restricted
        is_scam (:obj:`bool`):
            True, if many users reported this supergroup or channel as a scam
        is_fake (:obj:`bool`):
            True, if many users reported this supergroup or channel as a fake account

    Returns:
        Supergroup

    Raises:
        :class:`telegram.Error`
    """
    ID = "supergroup"

    def __init__(self, id, username, date, status, member_count, has_linked_chat, has_location, sign_messages, join_to_send_messages, join_by_request, is_slow_mode_enabled, is_channel, is_broadcast_group, is_verified, restriction_reason, is_scam, is_fake, **kwargs):
        
        self.id = id  # int
        self.username = username  # str
        self.date = date  # int
        self.status = status  # ChatMemberStatus
        self.member_count = member_count  # int
        self.has_linked_chat = has_linked_chat  # bool
        self.has_location = has_location  # bool
        self.sign_messages = sign_messages  # bool
        self.join_to_send_messages = join_to_send_messages  # bool
        self.join_by_request = join_by_request  # bool
        self.is_slow_mode_enabled = is_slow_mode_enabled  # bool
        self.is_channel = is_channel  # bool
        self.is_broadcast_group = is_broadcast_group  # bool
        self.is_verified = is_verified  # bool
        self.restriction_reason = restriction_reason  # str
        self.is_scam = is_scam  # bool
        self.is_fake = is_fake  # bool

    @staticmethod
    def read(q: dict, *args) -> "Supergroup":
        id = q.get('id')
        username = q.get('username')
        date = q.get('date')
        status = Object.read(q.get('status'))
        member_count = q.get('member_count')
        has_linked_chat = q.get('has_linked_chat')
        has_location = q.get('has_location')
        sign_messages = q.get('sign_messages')
        join_to_send_messages = q.get('join_to_send_messages')
        join_by_request = q.get('join_by_request')
        is_slow_mode_enabled = q.get('is_slow_mode_enabled')
        is_channel = q.get('is_channel')
        is_broadcast_group = q.get('is_broadcast_group')
        is_verified = q.get('is_verified')
        restriction_reason = q.get('restriction_reason')
        is_scam = q.get('is_scam')
        is_fake = q.get('is_fake')
        return Supergroup(id, username, date, status, member_count, has_linked_chat, has_location, sign_messages, join_to_send_messages, join_by_request, is_slow_mode_enabled, is_channel, is_broadcast_group, is_verified, restriction_reason, is_scam, is_fake)
