

from ..utils import Object


class TextEntityType(Object):
    """
    Represents a part of the text which must be formatted differently

    No parameters required.
    """
    ID = "textEntityType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeCashtag or TextEntityTypeEmailAddress or TextEntityTypePre or TextEntityTypeHashtag or TextEntityTypeStrikethrough or TextEntityTypeBotCommand or TextEntityTypeItalic or TextEntityTypeBankCardNumber or TextEntityTypeCode or TextEntityTypeUrl or TextEntityTypePreCode or TextEntityTypeUnderline or TextEntityTypePhoneNumber or TextEntityTypeMentionName or TextEntityTypeTextUrl or TextEntityTypeMention or TextEntityTypeBold":
        if q.get("@type"):
            return Object.read(q)
        return TextEntityType()
