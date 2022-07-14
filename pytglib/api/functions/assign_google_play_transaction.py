

from ..utils import Object


class AssignGooglePlayTransaction(Object):
    """
    Informs server about a Telegram Premium purchase through Google Play. For official applications only 

    Attributes:
        ID (:obj:`str`): ``AssignGooglePlayTransaction``

    Args:
        purchase_token (:obj:`str`):
            Google Play purchase token

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "assignGooglePlayTransaction"

    def __init__(self, purchase_token, extra=None, **kwargs):
        self.extra = extra
        self.purchase_token = purchase_token  # str

    @staticmethod
    def read(q: dict, *args) -> "AssignGooglePlayTransaction":
        purchase_token = q.get('purchase_token')
        return AssignGooglePlayTransaction(purchase_token)
