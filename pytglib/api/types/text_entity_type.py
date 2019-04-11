

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
    def read(q: dict, *args) -> "TextEntityTypePhoneNumber or TextEntityTypePreCode or TextEntityTypeMention or TextEntityTypeMentionName or TextEntityTypeCashtag or TextEntityTypeItalic or TextEntityTypeEmailAddress or TextEntityTypePre or TextEntityTypeBotCommand or TextEntityTypeUrl or TextEntityTypeHashtag or TextEntityTypeCode or TextEntityTypeTextUrl or TextEntityTypeBold":
        if q.get("@type"):
            return Object.read(q)
        return TextEntityType()
