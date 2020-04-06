

from ..utils import Object


class PollType(Object):
    """
    Describes the type of a poll

    No parameters required.
    """
    ID = "pollType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PollTypeRegular or PollTypeQuiz":
        if q.get("@type"):
            return Object.read(q)
        return PollType()
