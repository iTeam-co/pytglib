

from ..utils import Object


class InputPassportElementErrorSourceUnspecified(Object):
    """
    The element contains an error in an unspecified place. The error will be considered resolved when new data is added 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementErrorSourceUnspecified``

    Args:
        element_hash (:obj:`bytes`):
            Current hash of the entire element

    Returns:
        InputPassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementErrorSourceUnspecified"

    def __init__(self, element_hash, **kwargs):
        
        self.element_hash = element_hash  # bytes

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementErrorSourceUnspecified":
        element_hash = q.get('element_hash')
        return InputPassportElementErrorSourceUnspecified(element_hash)
