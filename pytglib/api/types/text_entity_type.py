

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
    def read(q: dict, *args) -> "TextEntityTypeBold or TextEntityTypeMentionName or TextEntityTypeMention or TextEntityTypePreCode or TextEntityTypeEmailAddress or TextEntityTypePre or TextEntityTypeItalic or TextEntityTypeTextUrl or TextEntityTypeCashtag or TextEntityTypeHashtag or TextEntityTypeBotCommand or TextEntityTypePhoneNumber or TextEntityTypeCode or TextEntityTypeUrl":
        if q.get("@type"):
            return Object.read(q)
        return TextEntityType()
