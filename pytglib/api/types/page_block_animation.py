

from ..utils import Object


class PageBlockAnimation(Object):
    """
    An animation 

    Attributes:
        ID (:obj:`str`): ``PageBlockAnimation``

    Args:
        animation (:class:`telegram.api.types.animation`):
            Animation file; may be null 
        caption (:class:`telegram.api.types.pageBlockCaption`):
            Animation caption 
        need_autoplay (:obj:`bool`):
            True, if the animation should be played automatically

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockAnimation"

    def __init__(self, animation, caption, need_autoplay, **kwargs):
        
        self.animation = animation  # Animation
        self.caption = caption  # PageBlockCaption
        self.need_autoplay = need_autoplay  # bool

    @staticmethod
    def read(q: dict, *args) -> "PageBlockAnimation":
        animation = Object.read(q.get('animation'))
        caption = Object.read(q.get('caption'))
        need_autoplay = q.get('need_autoplay')
        return PageBlockAnimation(animation, caption, need_autoplay)
