

from ..utils import Object


class PremiumLimitTypeCaptionLength(Object):
    """
    The maximum length of sent media caption

    Attributes:
        ID (:obj:`str`): ``PremiumLimitTypeCaptionLength``

    No parameters required.

    Returns:
        PremiumLimitType

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumLimitTypeCaptionLength"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumLimitTypeCaptionLength":
        
        return PremiumLimitTypeCaptionLength()
