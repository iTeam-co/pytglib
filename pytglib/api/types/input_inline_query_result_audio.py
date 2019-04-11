

from ..utils import Object


class InputInlineQueryResultAudio(Object):
    """
    Represents a link to an MP3 audio file 

    Attributes:
        ID (:obj:`str`): ``InputInlineQueryResultAudio``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        title (:obj:`str`):
            Title of the audio file 
        performer (:obj:`str`):
            Performer of the audio file
        audio_url (:obj:`str`):
            The URL of the audio file 
        audio_duration (:obj:`int`):
            Audio file duration, in seconds
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The message reply markupMust be of type replyMarkupInlineKeyboard or null
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            The content of the message to be sentMust be one of the following types: InputMessageText, InputMessageAudio, InputMessageLocation, InputMessageVenue or InputMessageContact

    Returns:
        InputInlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputInlineQueryResultAudio"

    def __init__(self, id, title, performer, audio_url, audio_duration, reply_markup, input_message_content, **kwargs):
        
        self.id = id  # str
        self.title = title  # str
        self.performer = performer  # str
        self.audio_url = audio_url  # str
        self.audio_duration = audio_duration  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "InputInlineQueryResultAudio":
        id = q.get('id')
        title = q.get('title')
        performer = q.get('performer')
        audio_url = q.get('audio_url')
        audio_duration = q.get('audio_duration')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return InputInlineQueryResultAudio(id, title, performer, audio_url, audio_duration, reply_markup, input_message_content)
