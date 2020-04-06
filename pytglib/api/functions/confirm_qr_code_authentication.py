

from ..utils import Object


class ConfirmQrCodeAuthentication(Object):
    """
    Confirms QR code authentication on another device. Returns created session on success 

    Attributes:
        ID (:obj:`str`): ``ConfirmQrCodeAuthentication``

    Args:
        link (:obj:`str`):
            A link from a QR codeThe link must be scanned by the in-app camera

    Returns:
        Session

    Raises:
        :class:`telegram.Error`
    """
    ID = "confirmQrCodeAuthentication"

    def __init__(self, link, extra=None, **kwargs):
        self.extra = extra
        self.link = link  # str

    @staticmethod
    def read(q: dict, *args) -> "ConfirmQrCodeAuthentication":
        link = q.get('link')
        return ConfirmQrCodeAuthentication(link)
