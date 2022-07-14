

from ..utils import Object


class TranslateText(Object):
    """
    Translates a text to the given language. Returns a 404 error if the translation can't be performed

    Attributes:
        ID (:obj:`str`): ``TranslateText``

    Args:
        text (:obj:`str`):
            Text to translate
        from_language_code (:obj:`str`):
            A two-letter ISO 639-1 language code of the language from which the message is translatedIf empty, the language will be detected automatically
        to_language_code (:obj:`str`):
            A two-letter ISO 639-1 language code of the language to which the message is translated

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "translateText"

    def __init__(self, text, from_language_code, to_language_code, extra=None, **kwargs):
        self.extra = extra
        self.text = text  # str
        self.from_language_code = from_language_code  # str
        self.to_language_code = to_language_code  # str

    @staticmethod
    def read(q: dict, *args) -> "TranslateText":
        text = q.get('text')
        from_language_code = q.get('from_language_code')
        to_language_code = q.get('to_language_code')
        return TranslateText(text, from_language_code, to_language_code)
