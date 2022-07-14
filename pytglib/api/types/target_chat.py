

from ..utils import Object


class TargetChat(Object):
    """
    Describes the target chat to be opened

    No parameters required.
    """
    ID = "targetChat"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TargetChatChosen or TargetChatInternalLink or TargetChatCurrent":
        if q.get("@type"):
            return Object.read(q)
        return TargetChat()
