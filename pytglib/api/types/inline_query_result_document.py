

from ..utils import Object


class InlineQueryResultDocument(Object):
    """
    Represents a document 

    Attributes:
        ID (:obj:`str`): ``InlineQueryResultDocument``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        document (:class:`telegram.api.types.document`):
            Document 
        title (:obj:`str`):
            Document title 
        description (:obj:`str`):
            Document description

    Returns:
        InlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineQueryResultDocument"

    def __init__(self, id, document, title, description, **kwargs):
        
        self.id = id  # str
        self.document = document  # Document
        self.title = title  # str
        self.description = description  # str

    @staticmethod
    def read(q: dict, *args) -> "InlineQueryResultDocument":
        id = q.get('id')
        document = Object.read(q.get('document'))
        title = q.get('title')
        description = q.get('description')
        return InlineQueryResultDocument(id, document, title, description)
