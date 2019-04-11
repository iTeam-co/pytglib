

from ..utils import Object


class DeletePassportElement(Object):
    """
    Deletes a Telegram Passport element 

    Attributes:
        ID (:obj:`str`): ``DeletePassportElement``

    Args:
        type (:class:`telegram.api.types.PassportElementType`):
            Element type

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deletePassportElement"

    def __init__(self, type, extra=None, **kwargs):
        self.extra = extra
        self.type = type  # PassportElementType

    @staticmethod
    def read(q: dict, *args) -> "DeletePassportElement":
        type = Object.read(q.get('type'))
        return DeletePassportElement(type)
