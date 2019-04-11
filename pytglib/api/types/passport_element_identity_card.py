

from ..utils import Object


class PassportElementIdentityCard(Object):
    """
    A Telegram Passport element containing the user's identity card 

    Attributes:
        ID (:obj:`str`): ``PassportElementIdentityCard``

    Args:
        identity_card (:class:`telegram.api.types.identityDocument`):
            Identity card

    Returns:
        PassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementIdentityCard"

    def __init__(self, identity_card, **kwargs):
        
        self.identity_card = identity_card  # IdentityDocument

    @staticmethod
    def read(q: dict, *args) -> "PassportElementIdentityCard":
        identity_card = Object.read(q.get('identity_card'))
        return PassportElementIdentityCard(identity_card)
