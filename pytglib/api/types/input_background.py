

from ..utils import Object


class InputBackground(Object):
    """
    Contains information about background to set

    No parameters required.
    """
    ID = "inputBackground"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InputBackgroundLocal or InputBackgroundRemote":
        if q.get("@type"):
            return Object.read(q)
        return InputBackground()
