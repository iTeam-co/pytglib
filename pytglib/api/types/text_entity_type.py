

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
    def read(q: dict, *args) -> "TextEntityTypeBotCommand or TextEntityTypeBold or TextEntityTypeMention or TextEntityTypeUrl or TextEntityTypeSpoiler or TextEntityTypeMentionName or TextEntityTypeHashtag or TextEntityTypeItalic or TextEntityTypeCode or TextEntityTypePre or TextEntityTypePreCode or TextEntityTypeStrikethrough or TextEntityTypeTextUrl or TextEntityTypePhoneNumber or TextEntityTypeBankCardNumber or TextEntityTypeMediaTimestamp or TextEntityTypeCashtag or TextEntityTypeUnderline or TextEntityTypeEmailAddress":
        if q.get("@type"):
            return Object.read(q)
        return TextEntityType()
