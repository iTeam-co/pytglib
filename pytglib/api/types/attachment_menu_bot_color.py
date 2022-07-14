

from ..utils import Object


class AttachmentMenuBotColor(Object):
    """
    Describes a color to highlight a bot added to attachment menu 

    Attributes:
        ID (:obj:`str`): ``AttachmentMenuBotColor``

    Args:
        light_color (:obj:`int`):
            Color in the RGB24 format for light themes 
        dark_color (:obj:`int`):
            Color in the RGB24 format for dark themes

    Returns:
        AttachmentMenuBotColor

    Raises:
        :class:`telegram.Error`
    """
    ID = "attachmentMenuBotColor"

    def __init__(self, light_color, dark_color, **kwargs):
        
        self.light_color = light_color  # int
        self.dark_color = dark_color  # int

    @staticmethod
    def read(q: dict, *args) -> "AttachmentMenuBotColor":
        light_color = q.get('light_color')
        dark_color = q.get('dark_color')
        return AttachmentMenuBotColor(light_color, dark_color)
