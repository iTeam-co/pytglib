

from ..utils import Object


class InlineQueryResultVoiceNote(Object):
    """
    Represents a voice note 

    Attributes:
        ID (:obj:`str`): ``InlineQueryResultVoiceNote``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        voice_note (:class:`telegram.api.types.voiceNote`):
            Voice note 
        title (:obj:`str`):
            Title of the voice note

    Returns:
        InlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineQueryResultVoiceNote"

    def __init__(self, id, voice_note, title, **kwargs):
        
        self.id = id  # str
        self.voice_note = voice_note  # VoiceNote
        self.title = title  # str

    @staticmethod
    def read(q: dict, *args) -> "InlineQueryResultVoiceNote":
        id = q.get('id')
        voice_note = Object.read(q.get('voice_note'))
        title = q.get('title')
        return InlineQueryResultVoiceNote(id, voice_note, title)
