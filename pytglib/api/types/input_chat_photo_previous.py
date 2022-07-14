

from ..utils import Object


class InputChatPhotoPrevious(Object):
    """
    A previously used profile photo of the current user 

    Attributes:
        ID (:obj:`str`): ``InputChatPhotoPrevious``

    Args:
        chat_photo_id (:obj:`int`):
            Identifier of the current user's profile photo to reuse

    Returns:
        InputChatPhoto

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputChatPhotoPrevious"

    def __init__(self, chat_photo_id, **kwargs):
        
        self.chat_photo_id = chat_photo_id  # int

    @staticmethod
    def read(q: dict, *args) -> "InputChatPhotoPrevious":
        chat_photo_id = q.get('chat_photo_id')
        return InputChatPhotoPrevious(chat_photo_id)
