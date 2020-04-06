

from ..utils import Object


class BackgroundTypePattern(Object):
    """
    A PNG or TGV (gzipped subset of SVG with MIME type "application/x-tgwallpattern") pattern to be combined with the background fill chosen by the user

    Attributes:
        ID (:obj:`str`): ``BackgroundTypePattern``

    Args:
        fill (:class:`telegram.api.types.BackgroundFill`):
            Description of the background fill
        intensity (:obj:`int`):
            Intensity of the pattern when it is shown above the filled background, 0-100
        is_moving (:obj:`bool`):
            True, if the background needs to be slightly moved when device is tilted

    Returns:
        BackgroundType

    Raises:
        :class:`telegram.Error`
    """
    ID = "backgroundTypePattern"

    def __init__(self, fill, intensity, is_moving, **kwargs):
        
        self.fill = fill  # BackgroundFill
        self.intensity = intensity  # int
        self.is_moving = is_moving  # bool

    @staticmethod
    def read(q: dict, *args) -> "BackgroundTypePattern":
        fill = Object.read(q.get('fill'))
        intensity = q.get('intensity')
        is_moving = q.get('is_moving')
        return BackgroundTypePattern(fill, intensity, is_moving)
