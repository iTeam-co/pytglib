

from ..utils import Object


class InputChatPhotoAnimation(Object):
    """
    An animation in MPEG4 format; must be square, at most 10 seconds long, have width between 160 and 800 and be at most 2MB in size

    Attributes:
        ID (:obj:`str`): ``InputChatPhotoAnimation``

    Args:
        animation (:class:`telegram.api.types.InputFile`):
            Animation to be set as profile photoOnly inputFileLocal and inputFileGenerated are allowed
        main_frame_timestamp (:obj:`float`):
            Timestamp of the frame, which will be used as static chat photo

    Returns:
        InputChatPhoto

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputChatPhotoAnimation"

    def __init__(self, animation, main_frame_timestamp, **kwargs):
        
        self.animation = animation  # InputFile
        self.main_frame_timestamp = main_frame_timestamp  # float

    @staticmethod
    def read(q: dict, *args) -> "InputChatPhotoAnimation":
        animation = Object.read(q.get('animation'))
        main_frame_timestamp = q.get('main_frame_timestamp')
        return InputChatPhotoAnimation(animation, main_frame_timestamp)
