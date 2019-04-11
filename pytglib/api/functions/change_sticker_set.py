

from ..utils import Object


class ChangeStickerSet(Object):
    """
    Installs/uninstalls or activates/archives a sticker set 

    Attributes:
        ID (:obj:`str`): ``ChangeStickerSet``

    Args:
        set_id (:obj:`int`):
            Identifier of the sticker set 
        is_installed (:obj:`bool`):
            The new value of is_installed 
        is_archived (:obj:`bool`):
            The new value of is_archivedA sticker set can't be installed and archived simultaneously

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "changeStickerSet"

    def __init__(self, set_id, is_installed, is_archived, extra=None, **kwargs):
        self.extra = extra
        self.set_id = set_id  # int
        self.is_installed = is_installed  # bool
        self.is_archived = is_archived  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChangeStickerSet":
        set_id = q.get('set_id')
        is_installed = q.get('is_installed')
        is_archived = q.get('is_archived')
        return ChangeStickerSet(set_id, is_installed, is_archived)
