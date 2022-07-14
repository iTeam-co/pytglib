

from ..utils import Object


class SuggestedActionCheckPhoneNumber(Object):
    """
    Suggests the user to check whether authorization phone number is correct and change the phone number if it is inaccessible

    Attributes:
        ID (:obj:`str`): ``SuggestedActionCheckPhoneNumber``

    No parameters required.

    Returns:
        SuggestedAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "suggestedActionCheckPhoneNumber"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SuggestedActionCheckPhoneNumber":
        
        return SuggestedActionCheckPhoneNumber()
