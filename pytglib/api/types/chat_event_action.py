

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
    def read(q: dict, *args) -> "ChatEventMemberInvited or ChatEventIsAllHistoryAvailableToggled or ChatEventMessagePinned or ChatEventDescriptionChanged or ChatEventVideoChatParticipantVolumeLevelChanged or ChatEventMemberPromoted or ChatEventPermissionsChanged or ChatEventSignMessagesToggled or ChatEventPollStopped or ChatEventInviteLinkRevoked or ChatEventInviteLinkDeleted or ChatEventMemberJoinedByRequest or ChatEventMessageEdited or ChatEventInvitesToggled or ChatEventVideoChatCreated or ChatEventPhotoChanged or ChatEventMessageDeleted or ChatEventTitleChanged or ChatEventMessageTtlChanged or ChatEventLocationChanged or ChatEventInviteLinkEdited or ChatEventSlowModeDelayChanged or ChatEventMemberRestricted or ChatEventVideoChatParticipantIsMutedToggled or ChatEventLinkedChatChanged or ChatEventHasProtectedContentToggled or ChatEventVideoChatMuteNewParticipantsToggled or ChatEventAvailableReactionsChanged or ChatEventMemberLeft or ChatEventUsernameChanged or ChatEventMessageUnpinned or ChatEventMemberJoinedByInviteLink or ChatEventStickerSetChanged or ChatEventVideoChatEnded or ChatEventMemberJoined":
        if q.get("@type"):
            return Object.read(q)
        return ChatEventAction()
