

from ..utils import Object


class InputPassportElementIdentityCard(Object):
    """
    A Telegram Passport element to be saved containing the user's identity card 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementIdentityCard``

    Args:
        identity_card (:class:`telegram.api.types.inputIdentityDocument`):
            The identity card to be saved

    Returns:
        InputPassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementIdentityCard"

    def __init__(self, identity_card, **kwargs):
        
        self.identity_card = identity_card  # InputIdentityDocument

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementIdentityCard":
        identity_card = Object.read(q.get('identity_card'))
        return InputPassportElementIdentityCard(identity_card)
