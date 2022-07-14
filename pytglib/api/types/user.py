

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
        is_contact (:obj:`bool`):
            The user is a contact of the current user
        is_mutual_contact (:obj:`bool`):
            The user is a contact of the current user and the current user is a contact of the user
        is_verified (:obj:`bool`):
            True, if the user is verified
        is_premium (:obj:`bool`):
            True, if the user is a Telegram Premium user
        is_support (:obj:`bool`):
            True, if the user is Telegram support account
        restriction_reason (:obj:`str`):
            If non-empty, it contains a human-readable description of the reason why access to this user must be restricted
        is_scam (:obj:`bool`):
            True, if many users reported this user as a scam
        is_fake (:obj:`bool`):
            True, if many users reported this user as a fake account
        have_access (:obj:`bool`):
            If false, the user is inaccessible, and the only information known about the user is inside this classIdentifier of the user can't be passed to any method except GetUser
        type (:class:`telegram.api.types.UserType`):
            Type of the user
        language_code (:obj:`str`):
            IETF language tag of the user's language; only available to bots
        added_to_attachment_menu (:obj:`bool`):
            True, if the user added the current bot to attachment menu; only available to bots

    Returns:
        User

    Raises:
        :class:`telegram.Error`
    """
    ID = "user"

    def __init__(self, id, first_name, last_name, username, phone_number, status, profile_photo, is_contact, is_mutual_contact, is_verified, is_premium, is_support, restriction_reason, is_scam, is_fake, have_access, type, language_code, added_to_attachment_menu, **kwargs):
        
        self.id = id  # int
        self.first_name = first_name  # str
        self.last_name = last_name  # str
        self.username = username  # str
        self.phone_number = phone_number  # str
        self.status = status  # UserStatus
        self.profile_photo = profile_photo  # ProfilePhoto
        self.is_contact = is_contact  # bool
        self.is_mutual_contact = is_mutual_contact  # bool
        self.is_verified = is_verified  # bool
        self.is_premium = is_premium  # bool
        self.is_support = is_support  # bool
        self.restriction_reason = restriction_reason  # str
        self.is_scam = is_scam  # bool
        self.is_fake = is_fake  # bool
        self.have_access = have_access  # bool
        self.type = type  # UserType
        self.language_code = language_code  # str
        self.added_to_attachment_menu = added_to_attachment_menu  # bool

    @staticmethod
    def read(q: dict, *args) -> "User":
        id = q.get('id')
        first_name = q.get('first_name')
        last_name = q.get('last_name')
        username = q.get('username')
        phone_number = q.get('phone_number')
        status = Object.read(q.get('status'))
        profile_photo = Object.read(q.get('profile_photo'))
        is_contact = q.get('is_contact')
        is_mutual_contact = q.get('is_mutual_contact')
        is_verified = q.get('is_verified')
        is_premium = q.get('is_premium')
        is_support = q.get('is_support')
        restriction_reason = q.get('restriction_reason')
        is_scam = q.get('is_scam')
        is_fake = q.get('is_fake')
        have_access = q.get('have_access')
        type = Object.read(q.get('type'))
        language_code = q.get('language_code')
        added_to_attachment_menu = q.get('added_to_attachment_menu')
        return User(id, first_name, last_name, username, phone_number, status, profile_photo, is_contact, is_mutual_contact, is_verified, is_premium, is_support, restriction_reason, is_scam, is_fake, have_access, type, language_code, added_to_attachment_menu)
