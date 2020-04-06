

from ..utils import Object


class UserPrivacySettingRuleRestrictChatMembers(Object):
    """
    A rule to restrict all members of specified basic groups and supergroups from doing something 

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingRuleRestrictChatMembers``

    Args:
        chat_ids (List of :obj:`int`):
            The chat identifiers, total number of chats in all rules must not exceed 20

    Returns:
        UserPrivacySettingRule

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingRuleRestrictChatMembers"

    def __init__(self, chat_ids, **kwargs):
        
        self.chat_ids = chat_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingRuleRestrictChatMembers":
        chat_ids = q.get('chat_ids')
        return UserPrivacySettingRuleRestrictChatMembers(chat_ids)
