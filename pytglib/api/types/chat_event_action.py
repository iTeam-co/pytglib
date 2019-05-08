

from ..utils import Object


class ChatEventAction(Object):
    """
    Represents a chat event

    No parameters required.
    """
    ID = "chatEventAction"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatEventMemberJoined or ChatEventDescriptionChanged or ChatEventInvitesToggled or ChatEventMessageEdited or ChatEventMemberRestricted or ChatEventMemberInvited or ChatEventMessagePinned or ChatEventMessageUnpinned or ChatEventSignMessagesToggled or ChatEventMemberLeft or ChatEventPhotoChanged or ChatEventUsernameChanged or ChatEventStickerSetChanged or ChatEventMemberPromoted or ChatEventMessageDeleted or ChatEventIsAllHistoryAvailableToggled or ChatEventTitleChanged":
        if q.get("@type"):
            return Object.read(q)
        return ChatEventAction()
