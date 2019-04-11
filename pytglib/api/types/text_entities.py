

from ..utils import Object


class TextEntities(Object):
    """
    Contains a list of text entities 

    Attributes:
        ID (:obj:`str`): ``TextEntities``

    Args:
        entities (List of :class:`telegram.api.types.textEntity`):
            List of text entities

    Returns:
        TextEntities

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntities"

    def __init__(self, entities, **kwargs):
        
        self.entities = entities  # list of textEntity

    @staticmethod
    def read(q: dict, *args) -> "TextEntities":
        entities = [Object.read(i) for i in q.get('entities', [])]
        return TextEntities(entities)
