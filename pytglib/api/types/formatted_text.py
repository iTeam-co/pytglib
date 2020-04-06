

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
            Entities contained in the textEntities can be nested, but must not mutually intersect with each otherPre, Code and PreCode entities can't contain other entitiesBold, Italic, Underline and Strikethrough entities can contain and to be contained in all other entitiesAll other entities can't contain each other

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
