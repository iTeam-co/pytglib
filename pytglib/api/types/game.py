

from ..utils import Object


class Game(Object):
    """
    Describes a game 

    Attributes:
        ID (:obj:`str`): ``Game``

    Args:
        id (:obj:`int`):
            Game ID 
        short_name (:obj:`str`):
            Game short nameTo share a game use the URL https://tme/{bot_username}?game={game_short_name} 
        title (:obj:`str`):
            Game title 
        text (:class:`telegram.api.types.formattedText`):
            Game text, usually containing scoreboards for a game
        description (:obj:`str`):
            Game description 
        photo (:class:`telegram.api.types.photo`):
            Game photo 
        animation (:class:`telegram.api.types.animation`):
            Game animation; may be null

    Returns:
        Game

    Raises:
        :class:`telegram.Error`
    """
    ID = "game"

    def __init__(self, id, short_name, title, text, description, photo, animation, **kwargs):
        
        self.id = id  # int
        self.short_name = short_name  # str
        self.title = title  # str
        self.text = text  # FormattedText
        self.description = description  # str
        self.photo = photo  # Photo
        self.animation = animation  # Animation

    @staticmethod
    def read(q: dict, *args) -> "Game":
        id = q.get('id')
        short_name = q.get('short_name')
        title = q.get('title')
        text = Object.read(q.get('text'))
        description = q.get('description')
        photo = Object.read(q.get('photo'))
        animation = Object.read(q.get('animation'))
        return Game(id, short_name, title, text, description, photo, animation)
