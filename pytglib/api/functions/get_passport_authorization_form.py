

from ..utils import Object


class GetPassportAuthorizationForm(Object):
    """
    Returns a Telegram Passport authorization form for sharing data with a service 

    Attributes:
        ID (:obj:`str`): ``GetPassportAuthorizationForm``

    Args:
        bot_user_id (:obj:`int`):
            User identifier of the service's bot 
        scope (:obj:`str`):
            Telegram Passport element types requested by the service 
        public_key (:obj:`str`):
            Service's public_key 
        nonce (:obj:`str`):
            Authorization form nonce provided by the service

    Returns:
        PassportAuthorizationForm

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPassportAuthorizationForm"

    def __init__(self, bot_user_id, scope, public_key, nonce, extra=None, **kwargs):
        self.extra = extra
        self.bot_user_id = bot_user_id  # int
        self.scope = scope  # str
        self.public_key = public_key  # str
        self.nonce = nonce  # str

    @staticmethod
    def read(q: dict, *args) -> "GetPassportAuthorizationForm":
        bot_user_id = q.get('bot_user_id')
        scope = q.get('scope')
        public_key = q.get('public_key')
        nonce = q.get('nonce')
        return GetPassportAuthorizationForm(bot_user_id, scope, public_key, nonce)
