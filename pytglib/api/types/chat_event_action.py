

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
    def read(q: dict, *args) -> "ChatEventTitleChanged or ChatEventMemberInvited or ChatEventMemberJoined or ChatEventMessageUnpinned or ChatEventMessageDeleted or ChatEventMemberPromoted or ChatEventInvitesToggled or ChatEventPhotoChanged or ChatEventMemberLeft or ChatEventMessagePinned or ChatEventMemberRestricted or ChatEventStickerSetChanged or ChatEventMessageEdited or ChatEventUsernameChanged or ChatEventIsAllHistoryAvailableToggled or ChatEventSignMessagesToggled or ChatEventDescriptionChanged":
        if q.get("@type"):
            return Object.read(q)
        return ChatEventAction()
