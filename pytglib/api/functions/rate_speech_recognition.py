

from ..utils import Object


class RateSpeechRecognition(Object):
    """
    Rates recognized speech in a voice note message 

    Attributes:
        ID (:obj:`str`): ``RateSpeechRecognition``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to which the message belongs 
        message_id (:obj:`int`):
            Identifier of the message 
        is_good (:obj:`bool`):
            Pass true if the speech recognition is good

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "rateSpeechRecognition"

    def __init__(self, chat_id, message_id, is_good, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.is_good = is_good  # bool

    @staticmethod
    def read(q: dict, *args) -> "RateSpeechRecognition":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        is_good = q.get('is_good')
        return RateSpeechRecognition(chat_id, message_id, is_good)
