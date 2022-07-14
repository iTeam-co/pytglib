

from ..utils import Object


class PollTypeQuiz(Object):
    """
    A poll in quiz mode, which has exactly one correct answer option and can be answered only once

    Attributes:
        ID (:obj:`str`): ``PollTypeQuiz``

    Args:
        correct_option_id (:obj:`int`):
            0-based identifier of the correct answer option; -1 for a yet unanswered poll
        explanation (:class:`telegram.api.types.formattedText`):
            Text that is shown when the user chooses an incorrect answer or taps on the lamp icon; 0-200 characters with at most 2 line feeds; empty for a yet unanswered poll

    Returns:
        PollType

    Raises:
        :class:`telegram.Error`
    """
    ID = "pollTypeQuiz"

    def __init__(self, correct_option_id, explanation, **kwargs):
        
        self.correct_option_id = correct_option_id  # int
        self.explanation = explanation  # FormattedText

    @staticmethod
    def read(q: dict, *args) -> "PollTypeQuiz":
        correct_option_id = q.get('correct_option_id')
        explanation = Object.read(q.get('explanation'))
        return PollTypeQuiz(correct_option_id, explanation)
