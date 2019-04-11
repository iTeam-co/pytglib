

from ..utils import Object


class LocalizationTargetInfo(Object):
    """
    Contains information about the current localization target 

    Attributes:
        ID (:obj:`str`): ``LocalizationTargetInfo``

    Args:
        language_packs (List of :class:`telegram.api.types.languagePackInfo`):
            List of available language packs for this application

    Returns:
        LocalizationTargetInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "localizationTargetInfo"

    def __init__(self, language_packs, **kwargs):
        
        self.language_packs = language_packs  # list of languagePackInfo

    @staticmethod
    def read(q: dict, *args) -> "LocalizationTargetInfo":
        language_packs = [Object.read(i) for i in q.get('language_packs', [])]
        return LocalizationTargetInfo(language_packs)
