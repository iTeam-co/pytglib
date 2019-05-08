

from ..utils import Object


class LanguagePackStringValuePluralized(Object):
    """
    A language pack string which has different forms based on the number of some object it mentions. See https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html for more info

    Attributes:
        ID (:obj:`str`): ``LanguagePackStringValuePluralized``

    Args:
        zero_value (:obj:`str`):
            Value for zero objects 
        one_value (:obj:`str`):
            Value for one object 
        two_value (:obj:`str`):
            Value for two objects
        few_value (:obj:`str`):
            Value for few objects 
        many_value (:obj:`str`):
            Value for many objects 
        other_value (:obj:`str`):
            Default value

    Returns:
        LanguagePackStringValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "languagePackStringValuePluralized"

    def __init__(self, zero_value, one_value, two_value, few_value, many_value, other_value, **kwargs):
        
        self.zero_value = zero_value  # str
        self.one_value = one_value  # str
        self.two_value = two_value  # str
        self.few_value = few_value  # str
        self.many_value = many_value  # str
        self.other_value = other_value  # str

    @staticmethod
    def read(q: dict, *args) -> "LanguagePackStringValuePluralized":
        zero_value = q.get('zero_value')
        one_value = q.get('one_value')
        two_value = q.get('two_value')
        few_value = q.get('few_value')
        many_value = q.get('many_value')
        other_value = q.get('other_value')
        return LanguagePackStringValuePluralized(zero_value, one_value, two_value, few_value, many_value, other_value)
