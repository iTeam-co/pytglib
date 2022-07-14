

from ..utils import Object


class ChatActionBar(Object):
    """
    Describes actions which must be possible to do through a chat action bar

    No parameters required.
    """
    ID = "chatActionBar"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionBarAddContact or ChatActionBarReportAddBlock or ChatActionBarReportUnrelatedLocation or ChatActionBarInviteMembers or ChatActionBarSharePhoneNumber or ChatActionBarJoinRequest or ChatActionBarReportSpam":
        if q.get("@type"):
            return Object.read(q)
        return ChatActionBar()
