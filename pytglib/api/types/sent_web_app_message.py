

from ..utils import Object


class SentWebAppMessage(Object):
    """
    Information about the message sent by answerWebAppQuery 

    Attributes:
        ID (:obj:`str`): ``SentWebAppMessage``

    Args:
        inline_message_id (:obj:`str`):
            Identifier of the sent inline message, if known

    Returns:
        SentWebAppMessage

    Raises:
        :class:`telegram.Error`
    """
    ID = "sentWebAppMessage"

    def __init__(self, inline_message_id, **kwargs):
        
        self.inline_message_id = inline_message_id  # str

    @staticmethod
    def read(q: dict, *args) -> "SentWebAppMessage":
        inline_message_id = q.get('inline_message_id')
        return SentWebAppMessage(inline_message_id)
