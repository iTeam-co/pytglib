

from ..utils import Object


class InputChatPhotoStatic(Object):
    """
    A static photo in JPEG format 

    Attributes:
        ID (:obj:`str`): ``InputChatPhotoStatic``

    Args:
        photo (:class:`telegram.api.types.InputFile`):
            Photo to be set as profile photoOnly inputFileLocal and inputFileGenerated are allowed

    Returns:
        InputChatPhoto

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputChatPhotoStatic"

    def __init__(self, photo, **kwargs):
        
        self.photo = photo  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "InputChatPhotoStatic":
        photo = Object.read(q.get('photo'))
        return InputChatPhotoStatic(photo)
