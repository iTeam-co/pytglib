

from ..utils import Object


class InputBackgroundLocal(Object):
    """
    A background from a local file

    Attributes:
        ID (:obj:`str`): ``InputBackgroundLocal``

    Args:
        background (:class:`telegram.api.types.InputFile`):
            Background file to useOnly inputFileLocal and inputFileGenerated are supportedThe file must be in JPEG format for wallpapers and in PNG format for patterns

    Returns:
        InputBackground

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputBackgroundLocal"

    def __init__(self, background, **kwargs):
        
        self.background = background  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "InputBackgroundLocal":
        background = Object.read(q.get('background'))
        return InputBackgroundLocal(background)
