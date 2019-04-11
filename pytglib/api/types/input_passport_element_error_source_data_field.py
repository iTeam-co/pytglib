

from ..utils import Object


class InputPassportElementErrorSourceDataField(Object):
    """
    A data field contains an error. The error is considered resolved when the field's value changes 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementErrorSourceDataField``

    Args:
        field_name (:obj:`str`):
            Field name 
        data_hash (:obj:`bytes`):
            Current data hash

    Returns:
        InputPassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementErrorSourceDataField"

    def __init__(self, field_name, data_hash, **kwargs):
        
        self.field_name = field_name  # str
        self.data_hash = data_hash  # bytes

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementErrorSourceDataField":
        field_name = q.get('field_name')
        data_hash = q.get('data_hash')
        return InputPassportElementErrorSourceDataField(field_name, data_hash)
