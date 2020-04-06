

from ..utils import Object


class BankCardInfo(Object):
    """
    Information about a bank card 

    Attributes:
        ID (:obj:`str`): ``BankCardInfo``

    Args:
        title (:obj:`str`):
            Title of the bank card description 
        actions (List of :class:`telegram.api.types.bankCardActionOpenUrl`):
            Actions that can be done with the bank card number

    Returns:
        BankCardInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "bankCardInfo"

    def __init__(self, title, actions, **kwargs):
        
        self.title = title  # str
        self.actions = actions  # list of bankCardActionOpenUrl

    @staticmethod
    def read(q: dict, *args) -> "BankCardInfo":
        title = q.get('title')
        actions = [Object.read(i) for i in q.get('actions', [])]
        return BankCardInfo(title, actions)
