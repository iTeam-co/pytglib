

from ..utils import Object


class PassportElementErrorSourceDataField(Object):
    """
    One of the data fields contains an error. The error will be considered resolved when the value of the field changes 

    Attributes:
        ID (:obj:`str`): ``PassportElementErrorSourceDataField``

    Args:
        field_name (:obj:`str`):
            Field name

    Returns:
        PassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementErrorSourceDataField"

    def __init__(self, field_name, **kwargs):
        
        self.field_name = field_name  # str

    @staticmethod
    def read(q: dict, *args) -> "PassportElementErrorSourceDataField":
        field_name = q.get('field_name')
        return PassportElementErrorSourceDataField(field_name)
