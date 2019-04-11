

from ..utils import Object


class ChatReportSpamState(Object):
    """
    Contains information about the availability of the "Report spam" action for a chat 

    Attributes:
        ID (:obj:`str`): ``ChatReportSpamState``

    Args:
        can_report_spam (:obj:`bool`):
            True, if a prompt with the "Report spam" action should be shown to the user

    Returns:
        ChatReportSpamState

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatReportSpamState"

    def __init__(self, can_report_spam, **kwargs):
        
        self.can_report_spam = can_report_spam  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatReportSpamState":
        can_report_spam = q.get('can_report_spam')
        return ChatReportSpamState(can_report_spam)
