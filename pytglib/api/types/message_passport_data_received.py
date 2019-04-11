

from ..utils import Object


class MessagePassportDataReceived(Object):
    """
    Telegram Passport data has been received; for bots only 

    Attributes:
        ID (:obj:`str`): ``MessagePassportDataReceived``

    Args:
        elements (List of :class:`telegram.api.types.encryptedPassportElement`):
            List of received Telegram Passport elements 
        credentials (:class:`telegram.api.types.encryptedCredentials`):
            Encrypted data credentials

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messagePassportDataReceived"

    def __init__(self, elements, credentials, **kwargs):
        
        self.elements = elements  # list of encryptedPassportElement
        self.credentials = credentials  # EncryptedCredentials

    @staticmethod
    def read(q: dict, *args) -> "MessagePassportDataReceived":
        elements = [Object.read(i) for i in q.get('elements', [])]
        credentials = Object.read(q.get('credentials'))
        return MessagePassportDataReceived(elements, credentials)
