

from ..utils import Object


class TextParseModeMarkdown(Object):
    """
    The text uses Markdown-style formatting

    Attributes:
        ID (:obj:`str`): ``TextParseModeMarkdown``

    Args:
        version (:obj:`int`):
            Version of the parser: 0 or 1 - Telegram Bot API "Markdown" parse mode, 2 - Telegram Bot API "MarkdownV2" parse mode

    Returns:
        TextParseMode

    Raises:
        :class:`telegram.Error`
    """
    ID = "textParseModeMarkdown"

    def __init__(self, version, **kwargs):
        
        self.version = version  # int

    @staticmethod
    def read(q: dict, *args) -> "TextParseModeMarkdown":
        version = q.get('version')
        return TextParseModeMarkdown(version)
