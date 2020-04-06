

from ..utils import Object


class PageBlockVoiceNote(Object):
    """
    A voice note 

    Attributes:
        ID (:obj:`str`): ``PageBlockVoiceNote``

    Args:
        voice_note (:class:`telegram.api.types.voiceNote`):
            Voice note; may be null 
        caption (:class:`telegram.api.types.pageBlockCaption`):
            Voice note caption

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockVoiceNote"

    def __init__(self, voice_note, caption, **kwargs):
        
        self.voice_note = voice_note  # VoiceNote
        self.caption = caption  # PageBlockCaption

    @staticmethod
    def read(q: dict, *args) -> "PageBlockVoiceNote":
        voice_note = Object.read(q.get('voice_note'))
        caption = Object.read(q.get('caption'))
        return PageBlockVoiceNote(voice_note, caption)
