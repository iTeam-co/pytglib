

from ..utils import Object


class UpdateFileGenerationStop(Object):
    """
    File generation is no longer needed 

    Attributes:
        ID (:obj:`str`): ``UpdateFileGenerationStop``

    Args:
        generation_id (:obj:`int`):
            Unique identifier for the generation process

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateFileGenerationStop"

    def __init__(self, generation_id, **kwargs):
        
        self.generation_id = generation_id  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateFileGenerationStop":
        generation_id = q.get('generation_id')
        return UpdateFileGenerationStop(generation_id)
