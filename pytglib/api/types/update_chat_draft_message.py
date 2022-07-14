

from ..utils import Object


class UpdateChatDraftMessage(Object):
    """
    A chat draft has changed. Be aware that the update may come in the currently opened chat but with old content of the draft. If the user has changed the content of the draft, this update mustn't be applied 

    Attributes:
        ID (:obj:`str`): ``UpdateChatDraftMessage``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        draft_message (:class:`telegram.api.types.draftMessage`):
            The new draft message; may be null 
        positions (List of :class:`telegram.api.types.chatPosition`):
            The new chat positions in the chat lists

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatDraftMessage"

    def __init__(self, chat_id, draft_message, positions, **kwargs):
        
        self.chat_id = chat_id  # int
        self.draft_message = draft_message  # DraftMessage
        self.positions = positions  # list of chatPosition

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatDraftMessage":
        chat_id = q.get('chat_id')
        draft_message = Object.read(q.get('draft_message'))
        positions = [Object.read(i) for i in q.get('positions', [])]
        return UpdateChatDraftMessage(chat_id, draft_message, positions)
