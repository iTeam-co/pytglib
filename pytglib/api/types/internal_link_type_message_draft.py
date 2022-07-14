

from ..utils import Object


class InternalLinkTypeMessageDraft(Object):
    """
    The link contains a message draft text. A share screen needs to be shown to the user, then the chosen chat must be opened and the text is added to the input field

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeMessageDraft``

    Args:
        text (:class:`telegram.api.types.formattedText`):
            Message draft text 
        contains_link (:obj:`bool`):
            True, if the first line of the text contains a linkIf true, the input field needs to be focused and the text after the link must be selected

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeMessageDraft"

    def __init__(self, text, contains_link, **kwargs):
        
        self.text = text  # FormattedText
        self.contains_link = contains_link  # bool

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeMessageDraft":
        text = Object.read(q.get('text'))
        contains_link = q.get('contains_link')
        return InternalLinkTypeMessageDraft(text, contains_link)
