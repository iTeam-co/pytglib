

from ..utils import Object


class LanguagePackInfo(Object):
    """
    Contains information about a language pack 

    Attributes:
        ID (:obj:`str`): ``LanguagePackInfo``

    Args:
        id (:obj:`str`):
            Unique language pack identifier 
        name (:obj:`str`):
            Language name 
        native_name (:obj:`str`):
            Name of the language in that language 
        local_string_count (:obj:`int`):
            Total number of non-deleted strings from the language pack available locally

    Returns:
        LanguagePackInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "languagePackInfo"

    def __init__(self, id, name, native_name, local_string_count, **kwargs):
        
        self.id = id  # str
        self.name = name  # str
        self.native_name = native_name  # str
        self.local_string_count = local_string_count  # int

    @staticmethod
    def read(q: dict, *args) -> "LanguagePackInfo":
        id = q.get('id')
        name = q.get('name')
        native_name = q.get('native_name')
        local_string_count = q.get('local_string_count')
        return LanguagePackInfo(id, name, native_name, local_string_count)
