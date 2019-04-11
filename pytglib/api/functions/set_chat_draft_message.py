

from ..utils import Object


class SetChatDraftMessage(Object):
    """
    Changes the draft message in a chat 

    Attributes:
        ID (:obj:`str`): ``SetChatDraftMessage``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        draft_message (:class:`telegram.api.types.draftMessage`):
            New draft message; may be null

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatDraftMessage"

    def __init__(self, chat_id, draft_message, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.draft_message = draft_message  # DraftMessage

    @staticmethod
    def read(q: dict, *args) -> "SetChatDraftMessage":
        chat_id = q.get('chat_id')
        draft_message = Object.read(q.get('draft_message'))
        return SetChatDraftMessage(chat_id, draft_message)
