

from ..utils import Object


class WriteGeneratedFilePart(Object):
    """
    Writes a part of a generated file. This method is intended to be used only if the client has no direct access to TDLib's file system, because it is usually slower than a direct write to the destination file

    Attributes:
        ID (:obj:`str`): ``WriteGeneratedFilePart``

    Args:
        generation_id (:obj:`int`):
            The identifier of the generation process 
        offset (:obj:`int`):
            The offset from which to write the data to the file 
        data (:obj:`bytes`):
            The data to write

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "writeGeneratedFilePart"

    def __init__(self, generation_id, offset, data, extra=None, **kwargs):
        self.extra = extra
        self.generation_id = generation_id  # int
        self.offset = offset  # int
        self.data = data  # bytes

    @staticmethod
    def read(q: dict, *args) -> "WriteGeneratedFilePart":
        generation_id = q.get('generation_id')
        offset = q.get('offset')
        data = q.get('data')
        return WriteGeneratedFilePart(generation_id, offset, data)
