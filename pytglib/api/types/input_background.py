

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
    def read(q: dict, *args) -> "InputBackgroundRemote or InputBackgroundLocal":
        if q.get("@type"):
            return Object.read(q)
        return InputBackground()
