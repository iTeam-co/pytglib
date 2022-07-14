

from ..utils import Object


class InternalLinkTypePassportDataRequest(Object):
    """
    The link contains a request of Telegram passport data. Call getPassportAuthorizationForm with the given parameters to process the link if the link was received from outside of the application, otherwise ignore it

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypePassportDataRequest``

    Args:
        bot_user_id (:obj:`int`):
            User identifier of the service's bot 
        scope (:obj:`str`):
            Telegram Passport element types requested by the service 
        public_key (:obj:`str`):
            Service's public key 
        nonce (:obj:`str`):
            Unique request identifier provided by the service
        callback_url (:obj:`str`):
            An HTTP URL to open once the request is finished or canceled with the parameter tg_passport=success or tg_passport=cancel respectivelyIf empty, then the link tgbot{bot_user_id}://passport/success or tgbot{bot_user_id}://passport/cancel needs to be opened instead

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypePassportDataRequest"

    def __init__(self, bot_user_id, scope, public_key, nonce, callback_url, **kwargs):
        
        self.bot_user_id = bot_user_id  # int
        self.scope = scope  # str
        self.public_key = public_key  # str
        self.nonce = nonce  # str
        self.callback_url = callback_url  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypePassportDataRequest":
        bot_user_id = q.get('bot_user_id')
        scope = q.get('scope')
        public_key = q.get('public_key')
        nonce = q.get('nonce')
        callback_url = q.get('callback_url')
        return InternalLinkTypePassportDataRequest(bot_user_id, scope, public_key, nonce, callback_url)
