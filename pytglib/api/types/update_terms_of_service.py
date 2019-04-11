

from ..utils import Object


class UpdateTermsOfService(Object):
    """
    New terms of service must be accepted by the user. If the terms of service are declined, then the deleteAccount method should be called with the reason "Decline ToS update" 

    Attributes:
        ID (:obj:`str`): ``UpdateTermsOfService``

    Args:
        terms_of_service_id (:obj:`str`):
            Identifier of the terms of service 
        terms_of_service (:class:`telegram.api.types.termsOfService`):
            The new terms of service

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateTermsOfService"

    def __init__(self, terms_of_service_id, terms_of_service, **kwargs):
        
        self.terms_of_service_id = terms_of_service_id  # str
        self.terms_of_service = terms_of_service  # TermsOfService

    @staticmethod
    def read(q: dict, *args) -> "UpdateTermsOfService":
        terms_of_service_id = q.get('terms_of_service_id')
        terms_of_service = Object.read(q.get('terms_of_service'))
        return UpdateTermsOfService(terms_of_service_id, terms_of_service)
