

from ..utils import Object


class InputFile(Object):
    """
    Points to a file

    No parameters required.
    """
    ID = "inputFile"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InputFileId or InputFileGenerated or InputFileLocal or InputFileRemote":
        if q.get("@type"):
            return Object.read(q)
        return InputFile()
