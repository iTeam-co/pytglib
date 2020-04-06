

from ..utils import Object


class UserPrivacySettingRuleAllowChatMembers(Object):
    """
    A rule to allow all members of certain specified basic groups and supergroups to doing something 

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingRuleAllowChatMembers``

    Args:
        chat_ids (List of :obj:`int`):
            The chat identifiers, total number of chats in all rules must not exceed 20

    Returns:
        UserPrivacySettingRule

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingRuleAllowChatMembers"

    def __init__(self, chat_ids, **kwargs):
        
        self.chat_ids = chat_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingRuleAllowChatMembers":
        chat_ids = q.get('chat_ids')
        return UserPrivacySettingRuleAllowChatMembers(chat_ids)
