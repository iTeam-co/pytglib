

from ..utils import Object


class Background(Object):
    """
    Describes a chat background

    Attributes:
        ID (:obj:`str`): ``Background``

    Args:
        id (:obj:`int`):
            Unique background identifier
        is_default (:obj:`bool`):
            True, if this is one of default backgrounds
        is_dark (:obj:`bool`):
            True, if the background is dark and is recommended to be used with dark theme
        name (:obj:`str`):
            Unique background name
        document (:class:`telegram.api.types.document`):
            Document with the background; may be nullNull only for filled backgrounds
        type (:class:`telegram.api.types.BackgroundType`):
            Type of the background

    Returns:
        Background

    Raises:
        :class:`telegram.Error`
    """
    ID = "background"

    def __init__(self, id, is_default, is_dark, name, document, type, **kwargs):
        
        self.id = id  # int
        self.is_default = is_default  # bool
        self.is_dark = is_dark  # bool
        self.name = name  # str
        self.document = document  # Document
        self.type = type  # BackgroundType

    @staticmethod
    def read(q: dict, *args) -> "Background":
        id = q.get('id')
        is_default = q.get('is_default')
        is_dark = q.get('is_dark')
        name = q.get('name')
        document = Object.read(q.get('document'))
        type = Object.read(q.get('type'))
        return Background(id, is_default, is_dark, name, document, type)
