

from ..utils import Object


class AcceptTermsOfService(Object):
    """
    Accepts Telegram terms of services 

    Attributes:
        ID (:obj:`str`): ``AcceptTermsOfService``

    Args:
        terms_of_service_id (:obj:`str`):
            Terms of service identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "acceptTermsOfService"

    def __init__(self, terms_of_service_id, extra=None, **kwargs):
        self.extra = extra
        self.terms_of_service_id = terms_of_service_id  # str

    @staticmethod
    def read(q: dict, *args) -> "AcceptTermsOfService":
        terms_of_service_id = q.get('terms_of_service_id')
        return AcceptTermsOfService(terms_of_service_id)
