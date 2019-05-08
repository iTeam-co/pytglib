

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
    def read(q: dict, *args) -> "TextEntityTypeHashtag or TextEntityTypeCashtag or TextEntityTypePreCode or TextEntityTypeBotCommand or TextEntityTypeEmailAddress or TextEntityTypeUrl or TextEntityTypeMention or TextEntityTypeTextUrl or TextEntityTypeCode or TextEntityTypeBold or TextEntityTypePhoneNumber or TextEntityTypeItalic or TextEntityTypeMentionName or TextEntityTypePre":
        if q.get("@type"):
            return Object.read(q)
        return TextEntityType()
