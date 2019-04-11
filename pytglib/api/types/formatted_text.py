

from ..utils import Object


class FormattedText(Object):
    """
    A text with some entities 

    Attributes:
        ID (:obj:`str`): ``FormattedText``

    Args:
        text (:obj:`str`):
            The text 
        entities (List of :class:`telegram.api.types.textEntity`):
            Entities contained in the text

    Returns:
        FormattedText

    Raises:
        :class:`telegram.Error`
    """
    ID = "formattedText"

    def __init__(self, text, entities, **kwargs):
        
        self.text = text  # str
        self.entities = entities  # list of textEntity

    @staticmethod
    def read(q: dict, *args) -> "FormattedText":
        text = q.get('text')
        entities = [Object.read(i) for i in q.get('entities', [])]
        return FormattedText(text, entities)
