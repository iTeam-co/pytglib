

from ..utils import Object


class BankCardActionOpenUrl(Object):
    """
    Describes an action associated with a bank card number 

    Attributes:
        ID (:obj:`str`): ``BankCardActionOpenUrl``

    Args:
        text (:obj:`str`):
            Action text 
        url (:obj:`str`):
            The URL to be opened

    Returns:
        BankCardActionOpenUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "bankCardActionOpenUrl"

    def __init__(self, text, url, **kwargs):
        
        self.text = text  # str
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "BankCardActionOpenUrl":
        text = q.get('text')
        url = q.get('url')
        return BankCardActionOpenUrl(text, url)
