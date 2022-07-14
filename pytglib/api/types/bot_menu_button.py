

from ..utils import Object


class BotMenuButton(Object):
    """
    Describes a button to be shown instead of bot commands menu button 

    Attributes:
        ID (:obj:`str`): ``BotMenuButton``

    Args:
        text (:obj:`str`):
            Text of the button 
        url (:obj:`str`):
            URL to be passed to openWebApp

    Returns:
        BotMenuButton

    Raises:
        :class:`telegram.Error`
    """
    ID = "botMenuButton"

    def __init__(self, text, url, **kwargs):
        
        self.text = text  # str
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "BotMenuButton":
        text = q.get('text')
        url = q.get('url')
        return BotMenuButton(text, url)
