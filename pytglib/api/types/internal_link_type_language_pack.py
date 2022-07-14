

from ..utils import Object


class InternalLinkTypeLanguagePack(Object):
    """
    The link is a link to a language pack. Call getLanguagePackInfo with the given language pack identifier to process the link 

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeLanguagePack``

    Args:
        language_pack_id (:obj:`str`):
            Language pack identifier

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeLanguagePack"

    def __init__(self, language_pack_id, **kwargs):
        
        self.language_pack_id = language_pack_id  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeLanguagePack":
        language_pack_id = q.get('language_pack_id')
        return InternalLinkTypeLanguagePack(language_pack_id)
