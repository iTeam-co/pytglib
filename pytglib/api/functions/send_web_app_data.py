

from ..utils import Object


class SendWebAppData(Object):
    """
    Sends data received from a keyboardButtonTypeWebApp Web App to a bot

    Attributes:
        ID (:obj:`str`): ``SendWebAppData``

    Args:
        bot_user_id (:obj:`int`):
            Identifier of the target bot 
        button_text (:obj:`str`):
            Text of the keyboardButtonTypeWebApp button, which opened the Web App 
        data (:obj:`str`):
            Received data

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendWebAppData"

    def __init__(self, bot_user_id, button_text, data, extra=None, **kwargs):
        self.extra = extra
        self.bot_user_id = bot_user_id  # int
        self.button_text = button_text  # str
        self.data = data  # str

    @staticmethod
    def read(q: dict, *args) -> "SendWebAppData":
        bot_user_id = q.get('bot_user_id')
        button_text = q.get('button_text')
        data = q.get('data')
        return SendWebAppData(bot_user_id, button_text, data)
