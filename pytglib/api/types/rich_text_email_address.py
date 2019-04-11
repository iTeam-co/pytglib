

from ..utils import Object


class RichTextEmailAddress(Object):
    """
    A rich text email link 

    Attributes:
        ID (:obj:`str`): ``RichTextEmailAddress``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Text 
        email_address (:obj:`str`):
            Email address

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextEmailAddress"

    def __init__(self, text, email_address, **kwargs):
        
        self.text = text  # RichText
        self.email_address = email_address  # str

    @staticmethod
    def read(q: dict, *args) -> "RichTextEmailAddress":
        text = Object.read(q.get('text'))
        email_address = q.get('email_address')
        return RichTextEmailAddress(text, email_address)
