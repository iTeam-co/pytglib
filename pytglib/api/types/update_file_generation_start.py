

from ..utils import Object


class UpdateFileGenerationStart(Object):
    """
    The file generation process needs to be started by the client

    Attributes:
        ID (:obj:`str`): ``UpdateFileGenerationStart``

    Args:
        generation_id (:obj:`int`):
            Unique identifier for the generation process
        original_path (:obj:`str`):
            The path to a file from which a new file is generated; may be empty
        destination_path (:obj:`str`):
            The path to a file that should be created and where the new file should be generated
        conversion (:obj:`str`):
            String specifying the conversion applied to the original fileIf conversion is "#url#" than original_path contains an HTTP/HTTPS URL of a file, which should be downloaded by the client

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateFileGenerationStart"

    def __init__(self, generation_id, original_path, destination_path, conversion, **kwargs):
        
        self.generation_id = generation_id  # int
        self.original_path = original_path  # str
        self.destination_path = destination_path  # str
        self.conversion = conversion  # str

    @staticmethod
    def read(q: dict, *args) -> "UpdateFileGenerationStart":
        generation_id = q.get('generation_id')
        original_path = q.get('original_path')
        destination_path = q.get('destination_path')
        conversion = q.get('conversion')
        return UpdateFileGenerationStart(generation_id, original_path, destination_path, conversion)
