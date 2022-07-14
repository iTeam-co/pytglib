

from ..utils import Object


class GetMessageImportConfirmationText(Object):
    """
    Returns a confirmation text to be shown to the user before starting message import

    Attributes:
        ID (:obj:`str`): ``GetMessageImportConfirmationText``

    Args:
        chat_id (:obj:`int`):
            Identifier of a chat to which the messages will be importedIt must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info administrator right

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMessageImportConfirmationText"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetMessageImportConfirmationText":
        chat_id = q.get('chat_id')
        return GetMessageImportConfirmationText(chat_id)
