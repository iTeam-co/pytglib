

from ..utils import Object


class InputInvoiceMessage(Object):
    """
    An invoice from a message of the type messageInvoice 

    Attributes:
        ID (:obj:`str`): ``InputInvoiceMessage``

    Args:
        chat_id (:obj:`int`):
            Chat identifier of the message 
        message_id (:obj:`int`):
            Message identifier

    Returns:
        InputInvoice

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputInvoiceMessage"

    def __init__(self, chat_id, message_id, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "InputInvoiceMessage":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return InputInvoiceMessage(chat_id, message_id)
