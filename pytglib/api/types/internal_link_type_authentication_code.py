

from ..utils import Object


class InternalLinkTypeAuthenticationCode(Object):
    """
    The link contains an authentication code. Call checkAuthenticationCode with the code if the current authorization state is authorizationStateWaitCode 

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeAuthenticationCode``

    Args:
        code (:obj:`str`):
            The authentication code

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeAuthenticationCode"

    def __init__(self, code, **kwargs):
        
        self.code = code  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeAuthenticationCode":
        code = q.get('code')
        return InternalLinkTypeAuthenticationCode(code)
