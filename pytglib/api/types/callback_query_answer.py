

from ..utils import Object


class CallbackQueryAnswer(Object):
    """
    Contains a bot's answer to a callback query 

    Attributes:
        ID (:obj:`str`): ``CallbackQueryAnswer``

    Args:
        text (:obj:`str`):
            Text of the answer 
        show_alert (:obj:`bool`):
            True, if an alert should be shown to the user instead of a toast notification 
        url (:obj:`str`):
            URL to be opened

    Returns:
        CallbackQueryAnswer

    Raises:
        :class:`telegram.Error`
    """
    ID = "callbackQueryAnswer"

    def __init__(self, text, show_alert, url, **kwargs):
        
        self.text = text  # str
        self.show_alert = show_alert  # bool
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "CallbackQueryAnswer":
        text = q.get('text')
        show_alert = q.get('show_alert')
        url = q.get('url')
        return CallbackQueryAnswer(text, show_alert, url)
