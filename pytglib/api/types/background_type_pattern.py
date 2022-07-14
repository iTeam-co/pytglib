

from ..utils import Object


class BackgroundTypePattern(Object):
    """
    A PNG or TGV (gzipped subset of SVG with MIME type "application/x-tgwallpattern") pattern to be combined with the background fill chosen by the user

    Attributes:
        ID (:obj:`str`): ``BackgroundTypePattern``

    Args:
        fill (:class:`telegram.api.types.BackgroundFill`):
            Fill of the background
        intensity (:obj:`int`):
            Intensity of the pattern when it is shown above the filled background; 0-100
        is_inverted (:obj:`bool`):
            True, if the background fill must be applied only to the pattern itselfAll other pixels are black in this caseFor dark themes only
        is_moving (:obj:`bool`):
            True, if the background needs to be slightly moved when device is tilted

    Returns:
        BackgroundType

    Raises:
        :class:`telegram.Error`
    """
    ID = "backgroundTypePattern"

    def __init__(self, fill, intensity, is_inverted, is_moving, **kwargs):
        
        self.fill = fill  # BackgroundFill
        self.intensity = intensity  # int
        self.is_inverted = is_inverted  # bool
        self.is_moving = is_moving  # bool

    @staticmethod
    def read(q: dict, *args) -> "BackgroundTypePattern":
        fill = Object.read(q.get('fill'))
        intensity = q.get('intensity')
        is_inverted = q.get('is_inverted')
        is_moving = q.get('is_moving')
        return BackgroundTypePattern(fill, intensity, is_inverted, is_moving)
