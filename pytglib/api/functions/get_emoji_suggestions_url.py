

from ..utils import Object


class GetEmojiSuggestionsUrl(Object):
    """
    Returns an HTTP URL which can be used to automatically log in to the translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation 

    Attributes:
        ID (:obj:`str`): ``GetEmojiSuggestionsUrl``

    Args:
        language_code (:obj:`str`):
            Language code for which the emoji replacements will be suggested

    Returns:
        HttpUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "getEmojiSuggestionsUrl"

    def __init__(self, language_code, extra=None, **kwargs):
        self.extra = extra
        self.language_code = language_code  # str

    @staticmethod
    def read(q: dict, *args) -> "GetEmojiSuggestionsUrl":
        language_code = q.get('language_code')
        return GetEmojiSuggestionsUrl(language_code)
