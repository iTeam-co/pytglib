

from ..utils import Object


class PollTypeRegular(Object):
    """
    A regular poll 

    Attributes:
        ID (:obj:`str`): ``PollTypeRegular``

    Args:
        allow_multiple_answers (:obj:`bool`):
            True, if multiple answer options can be chosen simultaneously

    Returns:
        PollType

    Raises:
        :class:`telegram.Error`
    """
    ID = "pollTypeRegular"

    def __init__(self, allow_multiple_answers, **kwargs):
        
        self.allow_multiple_answers = allow_multiple_answers  # bool

    @staticmethod
    def read(q: dict, *args) -> "PollTypeRegular":
        allow_multiple_answers = q.get('allow_multiple_answers')
        return PollTypeRegular(allow_multiple_answers)
