

from ..utils import Object


class LogTags(Object):
    """
    Contains a list of available TDLib internal log tags 

    Attributes:
        ID (:obj:`str`): ``LogTags``

    Args:
        tags (List of :obj:`str`):
            List of log tags

    Returns:
        LogTags

    Raises:
        :class:`telegram.Error`
    """
    ID = "logTags"

    def __init__(self, tags, **kwargs):
        
        self.tags = tags  # list of str

    @staticmethod
    def read(q: dict, *args) -> "LogTags":
        tags = q.get('tags')
        return LogTags(tags)
