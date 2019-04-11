

from ..utils import Object


class PassportSuitableElement(Object):
    """
    Contains information about a Telegram Passport element that was requested by a service 

    Attributes:
        ID (:obj:`str`): ``PassportSuitableElement``

    Args:
        type (:class:`telegram.api.types.PassportElementType`):
            Type of the element 
        is_selfie_required (:obj:`bool`):
            True, if a selfie is required with the identity document
        is_translation_required (:obj:`bool`):
            True, if a certified English translation is required with the document 
        is_native_name_required (:obj:`bool`):
            True, if personal details must include the user's name in the language of their country of residence

    Returns:
        PassportSuitableElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportSuitableElement"

    def __init__(self, type, is_selfie_required, is_translation_required, is_native_name_required, **kwargs):
        
        self.type = type  # PassportElementType
        self.is_selfie_required = is_selfie_required  # bool
        self.is_translation_required = is_translation_required  # bool
        self.is_native_name_required = is_native_name_required  # bool

    @staticmethod
    def read(q: dict, *args) -> "PassportSuitableElement":
        type = Object.read(q.get('type'))
        is_selfie_required = q.get('is_selfie_required')
        is_translation_required = q.get('is_translation_required')
        is_native_name_required = q.get('is_native_name_required')
        return PassportSuitableElement(type, is_selfie_required, is_translation_required, is_native_name_required)
