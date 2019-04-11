

from ..utils import Object


class InputInlineQueryResultVoiceNote(Object):
    """
    Represents a link to an opus-encoded audio file within an OGG container, single channel audio 

    Attributes:
        ID (:obj:`str`): ``InputInlineQueryResultVoiceNote``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        title (:obj:`str`):
            Title of the voice note
        voice_note_url (:obj:`str`):
            The URL of the voice note file 
        voice_note_duration (:obj:`int`):
            Duration of the voice note, in seconds
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The message reply markupMust be of type replyMarkupInlineKeyboard or null
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            The content of the message to be sentMust be one of the following types: InputMessageText, InputMessageVoiceNote, InputMessageLocation, InputMessageVenue or InputMessageContact

    Returns:
        InputInlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputInlineQueryResultVoiceNote"

    def __init__(self, id, title, voice_note_url, voice_note_duration, reply_markup, input_message_content, **kwargs):
        
        self.id = id  # str
        self.title = title  # str
        self.voice_note_url = voice_note_url  # str
        self.voice_note_duration = voice_note_duration  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "InputInlineQueryResultVoiceNote":
        id = q.get('id')
        title = q.get('title')
        voice_note_url = q.get('voice_note_url')
        voice_note_duration = q.get('voice_note_duration')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return InputInlineQueryResultVoiceNote(id, title, voice_note_url, voice_note_duration, reply_markup, input_message_content)
