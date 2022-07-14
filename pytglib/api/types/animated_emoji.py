

from ..utils import Object


class AnimatedEmoji(Object):
    """
    Describes an animated representation of an emoji

    Attributes:
        ID (:obj:`str`): ``AnimatedEmoji``

    Args:
        sticker (:class:`telegram.api.types.sticker`):
            Animated sticker for the emoji
        fitzpatrick_type (:obj:`int`):
            Emoji modifier fitzpatrick type; 0-6; 0 if none
        sound (:class:`telegram.api.types.file`):
            File containing the sound to be played when the animated emoji is clicked; may be nullThe sound is encoded with the Opus codec, and stored inside an OGG container

    Returns:
        AnimatedEmoji

    Raises:
        :class:`telegram.Error`
    """
    ID = "animatedEmoji"

    def __init__(self, sticker, fitzpatrick_type, sound, **kwargs):
        
        self.sticker = sticker  # Sticker
        self.fitzpatrick_type = fitzpatrick_type  # int
        self.sound = sound  # File

    @staticmethod
    def read(q: dict, *args) -> "AnimatedEmoji":
        sticker = Object.read(q.get('sticker'))
        fitzpatrick_type = q.get('fitzpatrick_type')
        sound = Object.read(q.get('sound'))
        return AnimatedEmoji(sticker, fitzpatrick_type, sound)
