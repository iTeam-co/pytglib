

from ..utils import Object


class FinishFileGeneration(Object):
    """
    Finishes the file generation

    Attributes:
        ID (:obj:`str`): ``FinishFileGeneration``

    Args:
        generation_id (:obj:`int`):
            The identifier of the generation process
        error (:class:`telegram.api.types.error`):
            If set, means that file generation has failed and should be terminated

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "finishFileGeneration"

    def __init__(self, generation_id, error, extra=None, **kwargs):
        self.extra = extra
        self.generation_id = generation_id  # int
        self.error = error  # Error

    @staticmethod
    def read(q: dict, *args) -> "FinishFileGeneration":
        generation_id = q.get('generation_id')
        error = Object.read(q.get('error'))
        return FinishFileGeneration(generation_id, error)
