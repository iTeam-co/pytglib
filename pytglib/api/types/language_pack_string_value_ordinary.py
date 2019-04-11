

from ..utils import Object


class LanguagePackStringValueOrdinary(Object):
    """
    An ordinary language pack string 

    Attributes:
        ID (:obj:`str`): ``LanguagePackStringValueOrdinary``

    Args:
        value (:obj:`str`):
            String value

    Returns:
        LanguagePackStringValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "languagePackStringValueOrdinary"

    def __init__(self, value, **kwargs):
        
        self.value = value  # str

    @staticmethod
    def read(q: dict, *args) -> "LanguagePackStringValueOrdinary":
        value = q.get('value')
        return LanguagePackStringValueOrdinary(value)
