

from ..utils import Object


class DraftMessage(Object):
    """
    Contains information about a message draft 

    Attributes:
        ID (:obj:`str`): ``DraftMessage``

    Args:
        reply_to_message_id (:obj:`int`):
            Identifier of the message to reply to; 0 if none 
        input_message_text (:class:`telegram.api.types.InputMessageContent`):
            Content of the message draft; this should always be of type inputMessageText

    Returns:
        DraftMessage

    Raises:
        :class:`telegram.Error`
    """
    ID = "draftMessage"

    def __init__(self, reply_to_message_id, input_message_text, **kwargs):
        
        self.reply_to_message_id = reply_to_message_id  # int
        self.input_message_text = input_message_text  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "DraftMessage":
        reply_to_message_id = q.get('reply_to_message_id')
        input_message_text = Object.read(q.get('input_message_text'))
        return DraftMessage(reply_to_message_id, input_message_text)
