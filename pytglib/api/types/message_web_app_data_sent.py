

from ..utils import Object


class MessageWebAppDataSent(Object):
    """
    Data from a Web App has been sent to a bot 

    Attributes:
        ID (:obj:`str`): ``MessageWebAppDataSent``

    Args:
        button_text (:obj:`str`):
            Text of the keyboardButtonTypeWebApp button, which opened the Web App

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageWebAppDataSent"

    def __init__(self, button_text, **kwargs):
        
        self.button_text = button_text  # str

    @staticmethod
    def read(q: dict, *args) -> "MessageWebAppDataSent":
        button_text = q.get('button_text')
        return MessageWebAppDataSent(button_text)
