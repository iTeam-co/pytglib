

from ..utils import Object


class TextEntityTypeMentionName(Object):
    """
    A text shows instead of a raw mention of the user (e.g., when the user has no username) 

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeMentionName``

    Args:
        user_id (:obj:`int`):
            Identifier of the mentioned user

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeMentionName"

    def __init__(self, user_id, **kwargs):
        
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeMentionName":
        user_id = q.get('user_id')
        return TextEntityTypeMentionName(user_id)
