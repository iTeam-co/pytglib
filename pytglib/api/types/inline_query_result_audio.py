

from ..utils import Object


class InlineQueryResultAudio(Object):
    """
    Represents an audio file 

    Attributes:
        ID (:obj:`str`): ``InlineQueryResultAudio``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        audio (:class:`telegram.api.types.audio`):
            Audio file

    Returns:
        InlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineQueryResultAudio"

    def __init__(self, id, audio, **kwargs):
        
        self.id = id  # str
        self.audio = audio  # Audio

    @staticmethod
    def read(q: dict, *args) -> "InlineQueryResultAudio":
        id = q.get('id')
        audio = Object.read(q.get('audio'))
        return InlineQueryResultAudio(id, audio)
