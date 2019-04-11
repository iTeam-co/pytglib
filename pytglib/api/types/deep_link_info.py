

from ..utils import Object


class DeepLinkInfo(Object):
    """
    Contains information about a tg:// deep link 

    Attributes:
        ID (:obj:`str`): ``DeepLinkInfo``

    Args:
        text (:class:`telegram.api.types.formattedText`):
            Text to be shown to the user 
        need_update_application (:obj:`bool`):
            True, if user should be asked to update the application

    Returns:
        DeepLinkInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "deepLinkInfo"

    def __init__(self, text, need_update_application, **kwargs):
        
        self.text = text  # FormattedText
        self.need_update_application = need_update_application  # bool

    @staticmethod
    def read(q: dict, *args) -> "DeepLinkInfo":
        text = Object.read(q.get('text'))
        need_update_application = q.get('need_update_application')
        return DeepLinkInfo(text, need_update_application)
