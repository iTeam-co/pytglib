

from ..utils import Object


class InternalLinkTypePrivacyAndSecuritySettings(Object):
    """
    The link is a link to the privacy and security settings section of the app

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypePrivacyAndSecuritySettings``

    No parameters required.

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypePrivacyAndSecuritySettings"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypePrivacyAndSecuritySettings":
        
        return InternalLinkTypePrivacyAndSecuritySettings()
