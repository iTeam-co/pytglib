

from ..utils import Object


class InputMessageText(Object):
    """
    A text message 

    Attributes:
        ID (:obj:`str`): ``InputMessageText``

    Args:
        text (:class:`telegram.api.types.formattedText`):
            Formatted text to be sent; 1-GetOption("message_text_length_max") charactersOnly Bold, Italic, Underline, Strikethrough, Code, Pre, PreCode, TextUrl and MentionName entities are allowed to be specified manually
        disable_web_page_preview (:obj:`bool`):
            True, if rich web page previews for URLs in the message text should be disabled 
        clear_draft (:obj:`bool`):
            True, if a chat message draft should be deleted

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageText"

    def __init__(self, text, disable_web_page_preview, clear_draft, **kwargs):
        
        self.text = text  # FormattedText
        self.disable_web_page_preview = disable_web_page_preview  # bool
        self.clear_draft = clear_draft  # bool

    @staticmethod
    def read(q: dict, *args) -> "InputMessageText":
        text = Object.read(q.get('text'))
        disable_web_page_preview = q.get('disable_web_page_preview')
        clear_draft = q.get('clear_draft')
        return InputMessageText(text, disable_web_page_preview, clear_draft)
