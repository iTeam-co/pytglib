

from ..utils import Object


class GetMarkdownText(Object):
    """
    Replaces text entities with Markdown formatting in a human-friendly format. Entities that can't be represented in Markdown unambiguously are kept as is. This is an offline method. Can be called before authorization. Can be called synchronously 

    Attributes:
        ID (:obj:`str`): ``GetMarkdownText``

    Args:
        text (:class:`telegram.api.types.formattedText`):
            The text

    Returns:
        FormattedText

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMarkdownText"

    def __init__(self, text, extra=None, **kwargs):
        self.extra = extra
        self.text = text  # FormattedText

    @staticmethod
    def read(q: dict, *args) -> "GetMarkdownText":
        text = Object.read(q.get('text'))
        return GetMarkdownText(text)
