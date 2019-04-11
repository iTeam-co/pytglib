

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
    def read(q: dict, *args) -> "InputFileGenerated or InputFileRemote or InputFileLocal or InputFileId":
        if q.get("@type"):
            return Object.read(q)
        return InputFile()
