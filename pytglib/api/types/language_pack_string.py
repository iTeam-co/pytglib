

from ..utils import Object


class LanguagePackString(Object):
    """
    Represents one language pack string 

    Attributes:
        ID (:obj:`str`): ``LanguagePackString``

    Args:
        key (:obj:`str`):
            String key 
        value (:class:`telegram.api.types.LanguagePackStringValue`):
            String value

    Returns:
        LanguagePackString

    Raises:
        :class:`telegram.Error`
    """
    ID = "languagePackString"

    def __init__(self, key, value, **kwargs):
        
        self.key = key  # str
        self.value = value  # LanguagePackStringValue

    @staticmethod
    def read(q: dict, *args) -> "LanguagePackString":
        key = q.get('key')
        value = Object.read(q.get('value'))
        return LanguagePackString(key, value)
