

from ..utils import Object


class MessageDocument(Object):
    """
    A document message (general file) 

    Attributes:
        ID (:obj:`str`): ``MessageDocument``

    Args:
        document (:class:`telegram.api.types.document`):
            The document description 
        caption (:class:`telegram.api.types.formattedText`):
            Document caption

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageDocument"

    def __init__(self, document, caption, **kwargs):
        
        self.document = document  # Document
        self.caption = caption  # FormattedText

    @staticmethod
    def read(q: dict, *args) -> "MessageDocument":
        document = Object.read(q.get('document'))
        caption = Object.read(q.get('caption'))
        return MessageDocument(document, caption)
