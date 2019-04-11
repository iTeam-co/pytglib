

from ..utils import Object


class PassportAuthorizationForm(Object):
    """
    Contains information about a Telegram Passport authorization form that was requested 

    Attributes:
        ID (:obj:`str`): ``PassportAuthorizationForm``

    Args:
        id (:obj:`int`):
            Unique identifier of the authorization form
        required_elements (List of :class:`telegram.api.types.passportRequiredElement`):
            Information about the Telegram Passport elements that need to be provided to complete the form 
        elements (List of :class:`telegram.api.types.PassportElement`):
            Already available Telegram Passport elements
        errors (List of :class:`telegram.api.types.passportElementError`):
            Errors in the elements that are already available 
        privacy_policy_url (:obj:`str`):
            URL for the privacy policy of the service; can be empty

    Returns:
        PassportAuthorizationForm

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportAuthorizationForm"

    def __init__(self, id, required_elements, elements, errors, privacy_policy_url, **kwargs):
        
        self.id = id  # int
        self.required_elements = required_elements  # list of passportRequiredElement
        self.elements = elements  # list of PassportElement
        self.errors = errors  # list of passportElementError
        self.privacy_policy_url = privacy_policy_url  # str

    @staticmethod
    def read(q: dict, *args) -> "PassportAuthorizationForm":
        id = q.get('id')
        required_elements = [Object.read(i) for i in q.get('required_elements', [])]
        elements = [Object.read(i) for i in q.get('elements', [])]
        errors = [Object.read(i) for i in q.get('errors', [])]
        privacy_policy_url = q.get('privacy_policy_url')
        return PassportAuthorizationForm(id, required_elements, elements, errors, privacy_policy_url)
