

from ..utils import Object


class SuggestedAction(Object):
    """
    Describes an action suggested to the current user

    No parameters required.
    """
    ID = "suggestedAction"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SuggestedActionViewChecksHint or SuggestedActionEnableArchiveAndMuteNewChats or SuggestedActionCheckPassword or SuggestedActionSetPassword or SuggestedActionConvertToBroadcastGroup or SuggestedActionCheckPhoneNumber":
        if q.get("@type"):
            return Object.read(q)
        return SuggestedAction()
