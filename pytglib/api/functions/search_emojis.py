

from ..utils import Object


class SearchEmojis(Object):
    """
    Searches for emojis by keywords. Supported only if the file database is enabled 

    Attributes:
        ID (:obj:`str`): ``SearchEmojis``

    Args:
        text (:obj:`str`):
            Text to search for 
        exact_match (:obj:`bool`):
            Pass true if only emojis, which exactly match the text, needs to be returned 
        input_language_codes (List of :obj:`str`):
            List of possible IETF language tags of the user's input language; may be empty if unknown

    Returns:
        Emojis

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchEmojis"

    def __init__(self, text, exact_match, input_language_codes, extra=None, **kwargs):
        self.extra = extra
        self.text = text  # str
        self.exact_match = exact_match  # bool
        self.input_language_codes = input_language_codes  # list of str

    @staticmethod
    def read(q: dict, *args) -> "SearchEmojis":
        text = q.get('text')
        exact_match = q.get('exact_match')
        input_language_codes = q.get('input_language_codes')
        return SearchEmojis(text, exact_match, input_language_codes)
