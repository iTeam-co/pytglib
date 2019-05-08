

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
    def read(q: dict, *args) -> "ChatEventMemberLeft or ChatEventMessageEdited or ChatEventMemberJoined or ChatEventInvitesToggled or ChatEventMemberPromoted or ChatEventMemberRestricted or ChatEventSignMessagesToggled or ChatEventPhotoChanged or ChatEventIsAllHistoryAvailableToggled or ChatEventMessagePinned or ChatEventDescriptionChanged or ChatEventTitleChanged or ChatEventMessageUnpinned or ChatEventMemberInvited or ChatEventStickerSetChanged or ChatEventMessageDeleted or ChatEventUsernameChanged":
        if q.get("@type"):
            return Object.read(q)
        return ChatEventAction()
