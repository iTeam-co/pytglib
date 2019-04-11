

from ..utils import Object


class ChatReportReasonCustom(Object):
    """
    A custom reason provided by the user 

    Attributes:
        ID (:obj:`str`): ``ChatReportReasonCustom``

    Args:
        text (:obj:`str`):
            Report text

    Returns:
        ChatReportReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatReportReasonCustom"

    def __init__(self, text, **kwargs):
        
        self.text = text  # str

    @staticmethod
    def read(q: dict, *args) -> "ChatReportReasonCustom":
        text = q.get('text')
        return ChatReportReasonCustom(text)
