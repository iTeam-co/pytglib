

from ..utils import Object


class PasswordState(Object):
    """
    Represents the current state of 2-step verification 

    Attributes:
        ID (:obj:`str`): ``PasswordState``

    Args:
        has_password (:obj:`bool`):
            True if a 2-step verification password is set 
        password_hint (:obj:`str`):
            Hint for the password; can be empty 
        has_recovery_email_address (:obj:`bool`):
            True if a recovery email is set 
        has_passport_data (:obj:`bool`):
            True if some Telegram Passport elements were saved 
        unconfirmed_recovery_email_address_pattern (:obj:`str`):
            Pattern of the email address to which the confirmation email was sent

    Returns:
        PasswordState

    Raises:
        :class:`telegram.Error`
    """
    ID = "passwordState"

    def __init__(self, has_password, password_hint, has_recovery_email_address, has_passport_data, unconfirmed_recovery_email_address_pattern, **kwargs):
        
        self.has_password = has_password  # bool
        self.password_hint = password_hint  # str
        self.has_recovery_email_address = has_recovery_email_address  # bool
        self.has_passport_data = has_passport_data  # bool
        self.unconfirmed_recovery_email_address_pattern = unconfirmed_recovery_email_address_pattern  # str

    @staticmethod
    def read(q: dict, *args) -> "PasswordState":
        has_password = q.get('has_password')
        password_hint = q.get('password_hint')
        has_recovery_email_address = q.get('has_recovery_email_address')
        has_passport_data = q.get('has_passport_data')
        unconfirmed_recovery_email_address_pattern = q.get('unconfirmed_recovery_email_address_pattern')
        return PasswordState(has_password, password_hint, has_recovery_email_address, has_passport_data, unconfirmed_recovery_email_address_pattern)
