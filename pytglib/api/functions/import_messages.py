

from ..utils import Object


class ImportMessages(Object):
    """
    Imports messages exported from another app

    Attributes:
        ID (:obj:`str`): ``ImportMessages``

    Args:
        chat_id (:obj:`int`):
            Identifier of a chat to which the messages will be importedIt must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info administrator right
        message_file (:class:`telegram.api.types.InputFile`):
            File with messages to importOnly inputFileLocal and inputFileGenerated are supportedThe file must not be previously uploaded
        attached_files (List of :class:`telegram.api.types.InputFile`):
            Files used in the imported messagesOnly inputFileLocal and inputFileGenerated are supportedThe files must not be previously uploaded

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "importMessages"

    def __init__(self, chat_id, message_file, attached_files, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_file = message_file  # InputFile
        self.attached_files = attached_files  # list of InputFile

    @staticmethod
    def read(q: dict, *args) -> "ImportMessages":
        chat_id = q.get('chat_id')
        message_file = Object.read(q.get('message_file'))
        attached_files = [Object.read(i) for i in q.get('attached_files', [])]
        return ImportMessages(chat_id, message_file, attached_files)
