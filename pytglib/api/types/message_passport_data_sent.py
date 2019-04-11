

from ..utils import Object


class MessagePassportDataSent(Object):
    """
    Telegram Passport data has been sent 

    Attributes:
        ID (:obj:`str`): ``MessagePassportDataSent``

    Args:
        types (List of :class:`telegram.api.types.PassportElementType`):
            List of Telegram Passport element types sent

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messagePassportDataSent"

    def __init__(self, types, **kwargs):
        
        self.types = types  # list of PassportElementType

    @staticmethod
    def read(q: dict, *args) -> "MessagePassportDataSent":
        types = [Object.read(i) for i in q.get('types', [])]
        return MessagePassportDataSent(types)
