

from ..utils import Object


class PageBlockAudio(Object):
    """
    An audio file 

    Attributes:
        ID (:obj:`str`): ``PageBlockAudio``

    Args:
        audio (:class:`telegram.api.types.audio`):
            Audio file; may be null 
        caption (:class:`telegram.api.types.pageBlockCaption`):
            Audio file caption

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockAudio"

    def __init__(self, audio, caption, **kwargs):
        
        self.audio = audio  # Audio
        self.caption = caption  # PageBlockCaption

    @staticmethod
    def read(q: dict, *args) -> "PageBlockAudio":
        audio = Object.read(q.get('audio'))
        caption = Object.read(q.get('caption'))
        return PageBlockAudio(audio, caption)
