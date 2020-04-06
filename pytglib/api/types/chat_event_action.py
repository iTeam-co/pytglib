

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
    def read(q: dict, *args) -> "ChatEventStickerSetChanged or ChatEventMemberLeft or ChatEventPermissionsChanged or ChatEventMemberJoined or ChatEventTitleChanged or ChatEventSlowModeDelayChanged or ChatEventDescriptionChanged or ChatEventInvitesToggled or ChatEventUsernameChanged or ChatEventMemberPromoted or ChatEventLocationChanged or ChatEventIsAllHistoryAvailableToggled or ChatEventMessagePinned or ChatEventPhotoChanged or ChatEventPollStopped or ChatEventMemberInvited or ChatEventMessageDeleted or ChatEventSignMessagesToggled or ChatEventMessageUnpinned or ChatEventMessageEdited or ChatEventLinkedChatChanged or ChatEventMemberRestricted":
        if q.get("@type"):
            return Object.read(q)
        return ChatEventAction()
