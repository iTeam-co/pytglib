

from ..utils import Object


class InputPassportElementErrorSourceFiles(Object):
    """
    The list of attached files contains an error. The error is considered resolved when the file list changes 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementErrorSourceFiles``

    Args:
        file_hashes (List of :obj:`bytes`):
            Current hashes of all attached files

    Returns:
        InputPassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementErrorSourceFiles"

    def __init__(self, file_hashes, **kwargs):
        
        self.file_hashes = file_hashes  # list of bytes

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementErrorSourceFiles":
        file_hashes = q.get('file_hashes')
        return InputPassportElementErrorSourceFiles(file_hashes)
