

from ..utils import Object


class SetFileGenerationProgress(Object):
    """
    Informs TDLib on a file generation progress

    Attributes:
        ID (:obj:`str`): ``SetFileGenerationProgress``

    Args:
        generation_id (:obj:`int`):
            The identifier of the generation process
        expected_size (:obj:`int`):
            Expected size of the generated file, in bytes; 0 if unknown
        local_prefix_size (:obj:`int`):
            The number of bytes already generated

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setFileGenerationProgress"

    def __init__(self, generation_id, expected_size, local_prefix_size, extra=None, **kwargs):
        self.extra = extra
        self.generation_id = generation_id  # int
        self.expected_size = expected_size  # int
        self.local_prefix_size = local_prefix_size  # int

    @staticmethod
    def read(q: dict, *args) -> "SetFileGenerationProgress":
        generation_id = q.get('generation_id')
        expected_size = q.get('expected_size')
        local_prefix_size = q.get('local_prefix_size')
        return SetFileGenerationProgress(generation_id, expected_size, local_prefix_size)
