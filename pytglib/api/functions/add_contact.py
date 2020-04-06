

from ..utils import Object


class AddContact(Object):
    """
    Adds a user to the contact list or edits an existing contact by their user identifier 

    Attributes:
        ID (:obj:`str`): ``AddContact``

    Args:
        contact (:class:`telegram.api.types.contact`):
            The contact to add or edit; phone number can be empty and needs to be specified only if known, vCard is ignored
        share_phone_number (:obj:`bool`):
            True, if the new contact needs to be allowed to see current user's phone numberA corresponding rule to userPrivacySettingShowPhoneNumber will be added if neededUse the field UserFullInfoneed_phone_number_privacy_exception to check whether the current user needs to be asked to share their phone number

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "addContact"

    def __init__(self, contact, share_phone_number, extra=None, **kwargs):
        self.extra = extra
        self.contact = contact  # Contact
        self.share_phone_number = share_phone_number  # bool

    @staticmethod
    def read(q: dict, *args) -> "AddContact":
        contact = Object.read(q.get('contact'))
        share_phone_number = q.get('share_phone_number')
        return AddContact(contact, share_phone_number)
