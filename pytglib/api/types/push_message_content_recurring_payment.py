

from ..utils import Object


class PushMessageContentRecurringPayment(Object):
    """
    A new recurrent payment was made by the current user 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentRecurringPayment``

    Args:
        amount (:obj:`str`):
            The paid amount

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentRecurringPayment"

    def __init__(self, amount, **kwargs):
        
        self.amount = amount  # str

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentRecurringPayment":
        amount = q.get('amount')
        return PushMessageContentRecurringPayment(amount)
