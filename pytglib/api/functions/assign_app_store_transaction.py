

from ..utils import Object


class AssignAppStoreTransaction(Object):
    """
    Informs server about a Telegram Premium purchase through App Store. For official applications only 

    Attributes:
        ID (:obj:`str`): ``AssignAppStoreTransaction``

    Args:
        receipt (:obj:`bytes`):
            App Store receipt 
        is_restore (:obj:`bool`):
            Pass true if this is a restore of a Telegram Premium purchase

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "assignAppStoreTransaction"

    def __init__(self, receipt, is_restore, extra=None, **kwargs):
        self.extra = extra
        self.receipt = receipt  # bytes
        self.is_restore = is_restore  # bool

    @staticmethod
    def read(q: dict, *args) -> "AssignAppStoreTransaction":
        receipt = q.get('receipt')
        is_restore = q.get('is_restore')
        return AssignAppStoreTransaction(receipt, is_restore)
