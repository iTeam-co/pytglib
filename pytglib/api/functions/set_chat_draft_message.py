

from ..utils import Object


class SetChatDraftMessage(Object):
    """
    Changes the draft message in a chat 

    Attributes:
        ID (:obj:`str`): ``SetChatDraftMessage``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_thread_id (:obj:`int`):
            If not 0, a message thread identifier in which the draft was changed 
        draft_message (:class:`telegram.api.types.draftMessage`):
            New draft message; pass null to remove the draft

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatDraftMessage"

    def __init__(self, chat_id, message_thread_id, draft_message, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_thread_id = message_thread_id  # int
        self.draft_message = draft_message  # DraftMessage

    @staticmethod
    def read(q: dict, *args) -> "SetChatDraftMessage":
        chat_id = q.get('chat_id')
        message_thread_id = q.get('message_thread_id')
        draft_message = Object.read(q.get('draft_message'))
        return SetChatDraftMessage(chat_id, message_thread_id, draft_message)
