

from ..utils import Object


class TermsOfService(Object):
    """
    Contains Telegram terms of service 

    Attributes:
        ID (:obj:`str`): ``TermsOfService``

    Args:
        text (:class:`telegram.api.types.formattedText`):
            Text of the terms of service 
        min_user_age (:obj:`int`):
            The minimum age of a user to be able to accept the terms; 0 if any 
        show_popup (:obj:`bool`):
            True, if a blocking popup with terms of service must be shown to the user

    Returns:
        TermsOfService

    Raises:
        :class:`telegram.Error`
    """
    ID = "termsOfService"

    def __init__(self, text, min_user_age, show_popup, **kwargs):
        
        self.text = text  # FormattedText
        self.min_user_age = min_user_age  # int
        self.show_popup = show_popup  # bool

    @staticmethod
    def read(q: dict, *args) -> "TermsOfService":
        text = Object.read(q.get('text'))
        min_user_age = q.get('min_user_age')
        show_popup = q.get('show_popup')
        return TermsOfService(text, min_user_age, show_popup)
