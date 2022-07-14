

from ..utils import Object


class ToggleAllDownloadsArePaused(Object):
    """
    Changes pause state of all files in the file download list 

    Attributes:
        ID (:obj:`str`): ``ToggleAllDownloadsArePaused``

    Args:
        are_paused (:obj:`bool`):
            Pass true to pause all downloads; pass false to unpause them

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleAllDownloadsArePaused"

    def __init__(self, are_paused, extra=None, **kwargs):
        self.extra = extra
        self.are_paused = are_paused  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleAllDownloadsArePaused":
        are_paused = q.get('are_paused')
        return ToggleAllDownloadsArePaused(are_paused)
