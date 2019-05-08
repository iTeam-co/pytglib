

from ..utils import Object


class LanguagePackInfo(Object):
    """
    Contains information about a language pack 

    Attributes:
        ID (:obj:`str`): ``LanguagePackInfo``

    Args:
        id (:obj:`str`):
            Unique language pack identifier
        base_language_pack_id (:obj:`str`):
            Identifier of a base language pack; may be emptyIf a string is missed in the language pack, then it should be fetched from base language packUnsupported in custom language packs
        name (:obj:`str`):
            Language name 
        native_name (:obj:`str`):
            Name of the language in that language
        plural_code (:obj:`str`):
            A language code to be used to apply plural formsSee https://wwwunicodeorg/cldr/charts/latest/supplemental/language_plural_ruleshtml for more info
        is_official (:obj:`bool`):
            True, if the language pack is official 
        is_rtl (:obj:`bool`):
            True, if the language pack strings are RTL 
        is_beta (:obj:`bool`):
            True, if the language pack is a beta language pack
        is_installed (:obj:`bool`):
            True, if the language pack is installed by the current user
        total_string_count (:obj:`int`):
            Total number of non-deleted strings from the language pack 
        translated_string_count (:obj:`int`):
            Total number of translated strings from the language pack
        local_string_count (:obj:`int`):
            Total number of non-deleted strings from the language pack available locally 
        translation_url (:obj:`str`):
            Link to language translation interface; empty for custom local language packs

    Returns:
        LanguagePackInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "languagePackInfo"

    def __init__(self, id, base_language_pack_id, name, native_name, plural_code, is_official, is_rtl, is_beta, is_installed, total_string_count, translated_string_count, local_string_count, translation_url, **kwargs):
        
        self.id = id  # str
        self.base_language_pack_id = base_language_pack_id  # str
        self.name = name  # str
        self.native_name = native_name  # str
        self.plural_code = plural_code  # str
        self.is_official = is_official  # bool
        self.is_rtl = is_rtl  # bool
        self.is_beta = is_beta  # bool
        self.is_installed = is_installed  # bool
        self.total_string_count = total_string_count  # int
        self.translated_string_count = translated_string_count  # int
        self.local_string_count = local_string_count  # int
        self.translation_url = translation_url  # str

    @staticmethod
    def read(q: dict, *args) -> "LanguagePackInfo":
        id = q.get('id')
        base_language_pack_id = q.get('base_language_pack_id')
        name = q.get('name')
        native_name = q.get('native_name')
        plural_code = q.get('plural_code')
        is_official = q.get('is_official')
        is_rtl = q.get('is_rtl')
        is_beta = q.get('is_beta')
        is_installed = q.get('is_installed')
        total_string_count = q.get('total_string_count')
        translated_string_count = q.get('translated_string_count')
        local_string_count = q.get('local_string_count')
        translation_url = q.get('translation_url')
        return LanguagePackInfo(id, base_language_pack_id, name, native_name, plural_code, is_official, is_rtl, is_beta, is_installed, total_string_count, translated_string_count, local_string_count, translation_url)
