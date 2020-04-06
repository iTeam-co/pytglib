

from ..utils import Object


class Document(Object):
    """
    Describes a document of any type 

    Attributes:
        ID (:obj:`str`): ``Document``

    Args:
        file_name (:obj:`str`):
            Original name of the file; as defined by the sender 
        mime_type (:obj:`str`):
            MIME type of the file; as defined by the sender
        minithumbnail (:class:`telegram.api.types.minithumbnail`):
            Document minithumbnail; may be null 
        thumbnail (:class:`telegram.api.types.photoSize`):
            Document thumbnail in JPEG or PNG format (PNG will be used only for background patterns); as defined by the sender; may be null 
        document (:class:`telegram.api.types.file`):
            File containing the document

    Returns:
        Document

    Raises:
        :class:`telegram.Error`
    """
    ID = "document"

    def __init__(self, file_name, mime_type, minithumbnail, thumbnail, document, **kwargs):
        
        self.file_name = file_name  # str
        self.mime_type = mime_type  # str
        self.minithumbnail = minithumbnail  # Minithumbnail
        self.thumbnail = thumbnail  # PhotoSize
        self.document = document  # File

    @staticmethod
    def read(q: dict, *args) -> "Document":
        file_name = q.get('file_name')
        mime_type = q.get('mime_type')
        minithumbnail = Object.read(q.get('minithumbnail'))
        thumbnail = Object.read(q.get('thumbnail'))
        document = Object.read(q.get('document'))
        return Document(file_name, mime_type, minithumbnail, thumbnail, document)
