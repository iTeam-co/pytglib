

from ..utils import Object


class LogStream(Object):
    """
    Describes a stream to which TDLib internal log is written

    No parameters required.
    """
    ID = "logStream"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "LogStreamEmpty or LogStreamDefault or LogStreamFile":
        if q.get("@type"):
            return Object.read(q)
        return LogStream()
