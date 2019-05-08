

from ..utils import Object


class User(Object):
    """
    Represents a user 

    Attributes:
        ID (:obj:`str`): ``User``

    Args:
        id (:obj:`int`):
            User identifier 
        first_name (:obj:`str`):
            First name of the user 
        last_name (:obj:`str`):
            Last name of the user 
        username (:obj:`str`):
            Username of the user
        phone_number (:obj:`str`):
            Phone number of the user 
        status (:class:`telegram.api.types.UserStatus`):
            Current online status of the user 
        profile_photo (:class:`telegram.api.types.profilePhoto`):
            Profile photo of the user; may be null
        outgoing_link (:class:`telegram.api.types.LinkState`):
            Relationship from the current user to the other user 
        incoming_link (:class:`telegram.api.types.LinkState`):
            Relationship from the other user to the current user
        is_verified (:obj:`bool`):
            True, if the user is verified 
        is_support (:obj:`bool`):
            True, if the user is Telegram support account
        restriction_reason (:obj:`str`):
            If non-empty, it contains the reason why access to this user must be restrictedThe format of the string is "{type}: {description}"{type} contains the type of the restriction and at least one of the suffixes "-all", "-ios", "-android", or "-wp", which describe the platforms on which access should be restricted(For example, "terms-ios-android"{description} contains a human-readable description of the restriction, which can be shown to the user)
        have_access (:obj:`bool`):
            If false, the user is inaccessible, and the only information known about the user is inside this classIt can't be passed to any method except GetUser 
        type (:class:`telegram.api.types.UserType`):
            Type of the user 
        language_code (:obj:`str`):
            IETF language tag of the user's language; only available to bots

    Returns:
        User

    Raises:
        :class:`telegram.Error`
    """
    ID = "user"

    def __init__(self, id, first_name, last_name, username, phone_number, status, profile_photo, outgoing_link, incoming_link, is_verified, is_support, restriction_reason, have_access, type, language_code, **kwargs):
        
        self.id = id  # int
        self.first_name = first_name  # str
        self.last_name = last_name  # str
        self.username = username  # str
        self.phone_number = phone_number  # str
        self.status = status  # UserStatus
        self.profile_photo = profile_photo  # ProfilePhoto
        self.outgoing_link = outgoing_link  # LinkState
        self.incoming_link = incoming_link  # LinkState
        self.is_verified = is_verified  # bool
        self.is_support = is_support  # bool
        self.restriction_reason = restriction_reason  # str
        self.have_access = have_access  # bool
        self.type = type  # UserType
        self.language_code = language_code  # str

    @staticmethod
    def read(q: dict, *args) -> "User":
        id = q.get('id')
        first_name = q.get('first_name')
        last_name = q.get('last_name')
        username = q.get('username')
        phone_number = q.get('phone_number')
        status = Object.read(q.get('status'))
        profile_photo = Object.read(q.get('profile_photo'))
        outgoing_link = Object.read(q.get('outgoing_link'))
        incoming_link = Object.read(q.get('incoming_link'))
        is_verified = q.get('is_verified')
        is_support = q.get('is_support')
        restriction_reason = q.get('restriction_reason')
        have_access = q.get('have_access')
        type = Object.read(q.get('type'))
        language_code = q.get('language_code')
        return User(id, first_name, last_name, username, phone_number, status, profile_photo, outgoing_link, incoming_link, is_verified, is_support, restriction_reason, have_access, type, language_code)
