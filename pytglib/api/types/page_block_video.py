

from ..utils import Object


class PageBlockVideo(Object):
    """
    A video 

    Attributes:
        ID (:obj:`str`): ``PageBlockVideo``

    Args:
        video (:class:`telegram.api.types.video`):
            Video file; may be null 
        caption (:class:`telegram.api.types.pageBlockCaption`):
            Video caption 
        need_autoplay (:obj:`bool`):
            True, if the video should be played automatically 
        is_looped (:obj:`bool`):
            True, if the video should be looped

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockVideo"

    def __init__(self, video, caption, need_autoplay, is_looped, **kwargs):
        
        self.video = video  # Video
        self.caption = caption  # PageBlockCaption
        self.need_autoplay = need_autoplay  # bool
        self.is_looped = is_looped  # bool

    @staticmethod
    def read(q: dict, *args) -> "PageBlockVideo":
        video = Object.read(q.get('video'))
        caption = Object.read(q.get('caption'))
        need_autoplay = q.get('need_autoplay')
        is_looped = q.get('is_looped')
        return PageBlockVideo(video, caption, need_autoplay, is_looped)
