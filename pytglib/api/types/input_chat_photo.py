

from ..utils import Object


class InputChatPhoto(Object):
    """
    Describes a photo to be set as a user profile or chat photo

    No parameters required.
    """
    ID = "inputChatPhoto"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InputChatPhotoAnimation or InputChatPhotoPrevious or InputChatPhotoStatic":
        if q.get("@type"):
            return Object.read(q)
        return InputChatPhoto()
