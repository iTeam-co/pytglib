

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
            Status of the current user in the supergroup or channel
        member_count (:obj:`int`):
            Member count; 0 if unknownCurrently it is guaranteed to be known only if the supergroup or channel was found through SearchPublicChats
        anyone_can_invite (:obj:`bool`):
            True, if any member of the supergroup can invite other membersThis field has no meaning for channels
        sign_messages (:obj:`bool`):
            True, if messages sent to the channel should contain information about the senderThis field is only applicable to channels
        is_channel (:obj:`bool`):
            True, if the supergroup is a channel
        is_verified (:obj:`bool`):
            True, if the supergroup or channel is verified
        restriction_reason (:obj:`str`):
            If non-empty, contains the reason why access to this supergroup or channel must be restrictedFormat of the string is "{type}: {description}"{type} Contains the type of the restriction and at least one of the suffixes "-all", "-ios", "-android", or "-wp", which describe the platforms on which access should be restricted(For example, "terms-ios-android"{description} contains a human-readable description of the restriction, which can be shown to the user)

    Returns:
        Supergroup

    Raises:
        :class:`telegram.Error`
    """
    ID = "supergroup"

    def __init__(self, id, username, date, status, member_count, anyone_can_invite, sign_messages, is_channel, is_verified, restriction_reason, **kwargs):
        
        self.id = id  # int
        self.username = username  # str
        self.date = date  # int
        self.status = status  # ChatMemberStatus
        self.member_count = member_count  # int
        self.anyone_can_invite = anyone_can_invite  # bool
        self.sign_messages = sign_messages  # bool
        self.is_channel = is_channel  # bool
        self.is_verified = is_verified  # bool
        self.restriction_reason = restriction_reason  # str

    @staticmethod
    def read(q: dict, *args) -> "Supergroup":
        id = q.get('id')
        username = q.get('username')
        date = q.get('date')
        status = Object.read(q.get('status'))
        member_count = q.get('member_count')
        anyone_can_invite = q.get('anyone_can_invite')
        sign_messages = q.get('sign_messages')
        is_channel = q.get('is_channel')
        is_verified = q.get('is_verified')
        restriction_reason = q.get('restriction_reason')
        return Supergroup(id, username, date, status, member_count, anyone_can_invite, sign_messages, is_channel, is_verified, restriction_reason)
