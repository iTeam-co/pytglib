

from ..utils import Object


class GetLogTags(Object):
    """
    Returns list of available TDLib internal log tags, for example, ["actor", "binlog", "connections", "notifications", "proxy"]. This is an offline method. Can be called before authorization. Can be called synchronously

    Attributes:
        ID (:obj:`str`): ``GetLogTags``

    No parameters required.

    Returns:
        LogTags

    Raises:
        :class:`telegram.Error`
    """
    ID = "getLogTags"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetLogTags":
        
        return GetLogTags()
