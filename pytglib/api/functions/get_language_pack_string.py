

from ..utils import Object


class GetLanguagePackString(Object):
    """
    Returns a string stored in the local database from the specified localization target and language pack by its key. Returns a 404 error if the string is not found. This is an offline method. Can be called before authorization. Can be called synchronously

    Attributes:
        ID (:obj:`str`): ``GetLanguagePackString``

    Args:
        language_pack_database_path (:obj:`str`):
            Path to the language pack database in which strings are stored 
        localization_target (:obj:`str`):
            Localization target to which the language pack belongs 
        language_pack_id (:obj:`str`):
            Language pack identifier 
        key (:obj:`str`):
            Language pack key of the string to be returned

    Returns:
        LanguagePackStringValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "getLanguagePackString"

    def __init__(self, language_pack_database_path, localization_target, language_pack_id, key, extra=None, **kwargs):
        self.extra = extra
        self.language_pack_database_path = language_pack_database_path  # str
        self.localization_target = localization_target  # str
        self.language_pack_id = language_pack_id  # str
        self.key = key  # str

    @staticmethod
    def read(q: dict, *args) -> "GetLanguagePackString":
        language_pack_database_path = q.get('language_pack_database_path')
        localization_target = q.get('localization_target')
        language_pack_id = q.get('language_pack_id')
        key = q.get('key')
        return GetLanguagePackString(language_pack_database_path, localization_target, language_pack_id, key)
