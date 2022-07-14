

from ..utils import Object


class MessageWebAppDataReceived(Object):
    """
    Data from a Web App has been received; for bots only 

    Attributes:
        ID (:obj:`str`): ``MessageWebAppDataReceived``

    Args:
        button_text (:obj:`str`):
            Text of the keyboardButtonTypeWebApp button, which opened the Web App 
        data (:obj:`str`):
            Received data

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageWebAppDataReceived"

    def __init__(self, button_text, data, **kwargs):
        
        self.button_text = button_text  # str
        self.data = data  # str

    @staticmethod
    def read(q: dict, *args) -> "MessageWebAppDataReceived":
        button_text = q.get('button_text')
        data = q.get('data')
        return MessageWebAppDataReceived(button_text, data)
