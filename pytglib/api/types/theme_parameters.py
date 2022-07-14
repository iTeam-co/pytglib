

from ..utils import Object


class ThemeParameters(Object):
    """
    Contains parameters of the application theme 

    Attributes:
        ID (:obj:`str`): ``ThemeParameters``

    Args:
        background_color (:obj:`int`):
            A color of the background in the RGB24 format 
        secondary_background_color (:obj:`int`):
            A secondary color for the background in the RGB24 format
        text_color (:obj:`int`):
            A color of text in the RGB24 format 
        hint_color (:obj:`int`):
            A color of hints in the RGB24 format 
        link_color (:obj:`int`):
            A color of links in the RGB24 format 
        button_color (:obj:`int`):
            A color of the buttons in the RGB24 format
        button_text_color (:obj:`int`):
            A color of text on the buttons in the RGB24 format

    Returns:
        ThemeParameters

    Raises:
        :class:`telegram.Error`
    """
    ID = "themeParameters"

    def __init__(self, background_color, secondary_background_color, text_color, hint_color, link_color, button_color, button_text_color, **kwargs):
        
        self.background_color = background_color  # int
        self.secondary_background_color = secondary_background_color  # int
        self.text_color = text_color  # int
        self.hint_color = hint_color  # int
        self.link_color = link_color  # int
        self.button_color = button_color  # int
        self.button_text_color = button_text_color  # int

    @staticmethod
    def read(q: dict, *args) -> "ThemeParameters":
        background_color = q.get('background_color')
        secondary_background_color = q.get('secondary_background_color')
        text_color = q.get('text_color')
        hint_color = q.get('hint_color')
        link_color = q.get('link_color')
        button_color = q.get('button_color')
        button_text_color = q.get('button_text_color')
        return ThemeParameters(background_color, secondary_background_color, text_color, hint_color, link_color, button_color, button_text_color)
