

from ..utils import Object


class RichTextPhoneNumber(Object):
    """
    A rich text phone number 

    Attributes:
        ID (:obj:`str`): ``RichTextPhoneNumber``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Text 
        phone_number (:obj:`str`):
            Phone number

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextPhoneNumber"

    def __init__(self, text, phone_number, **kwargs):
        
        self.text = text  # RichText
        self.phone_number = phone_number  # str

    @staticmethod
    def read(q: dict, *args) -> "RichTextPhoneNumber":
        text = Object.read(q.get('text'))
        phone_number = q.get('phone_number')
        return RichTextPhoneNumber(text, phone_number)
