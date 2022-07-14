

from ..utils import Object


class RecognizeSpeech(Object):
    """
    Recognizes speech in a voice note message. The message must be successfully sent and must not be scheduled. May return an error with a message "MSG_VOICE_TOO_LONG" if the voice note is too long to be recognized

    Attributes:
        ID (:obj:`str`): ``RecognizeSpeech``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to which the message belongs
        message_id (:obj:`int`):
            Identifier of the message

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "recognizeSpeech"

    def __init__(self, chat_id, message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "RecognizeSpeech":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return RecognizeSpeech(chat_id, message_id)
