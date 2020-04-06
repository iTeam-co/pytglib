

from ..utils import Object


class ParseMarkdown(Object):
    """
    Parses Markdown entities in a human-friendly format, ignoring mark up errors. This is an offline method. Can be called before authorization. Can be called synchronously

    Attributes:
        ID (:obj:`str`): ``ParseMarkdown``

    Args:
        text (:class:`telegram.api.types.formattedText`):
            The text to parseFor example, "__italic__ ~~strikethrough~~ **bold** `code` ```pre``` __[italic__ text_url](telegramorg) __italic**bold italic__bold**"

    Returns:
        FormattedText

    Raises:
        :class:`telegram.Error`
    """
    ID = "parseMarkdown"

    def __init__(self, text, extra=None, **kwargs):
        self.extra = extra
        self.text = text  # FormattedText

    @staticmethod
    def read(q: dict, *args) -> "ParseMarkdown":
        text = Object.read(q.get('text'))
        return ParseMarkdown(text)
