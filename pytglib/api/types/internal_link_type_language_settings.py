

from ..utils import Object


class InternalLinkTypeLanguageSettings(Object):
    """
    The link is a link to the language settings section of the app

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeLanguageSettings``

    No parameters required.

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeLanguageSettings"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeLanguageSettings":
        
        return InternalLinkTypeLanguageSettings()
