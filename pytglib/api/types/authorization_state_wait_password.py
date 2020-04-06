

from ..utils import Object


class AuthorizationStateWaitPassword(Object):
    """
    The user has been authorized, but needs to enter a password to start using the application 

    Attributes:
        ID (:obj:`str`): ``AuthorizationStateWaitPassword``

    Args:
        password_hint (:obj:`str`):
            Hint for the password; may be empty 
        has_recovery_email_address (:obj:`bool`):
            True, if a recovery email address has been set up
        recovery_email_address_pattern (:obj:`str`):
            Pattern of the email address to which the recovery email was sent; empty until a recovery email has been sent

    Returns:
        AuthorizationState

    Raises:
        :class:`telegram.Error`
    """
    ID = "authorizationStateWaitPassword"

    def __init__(self, password_hint, has_recovery_email_address, recovery_email_address_pattern, **kwargs):
        
        self.password_hint = password_hint  # str
        self.has_recovery_email_address = has_recovery_email_address  # bool
        self.recovery_email_address_pattern = recovery_email_address_pattern  # str

    @staticmethod
    def read(q: dict, *args) -> "AuthorizationStateWaitPassword":
        password_hint = q.get('password_hint')
        has_recovery_email_address = q.get('has_recovery_email_address')
        recovery_email_address_pattern = q.get('recovery_email_address_pattern')
        return AuthorizationStateWaitPassword(password_hint, has_recovery_email_address, recovery_email_address_pattern)
