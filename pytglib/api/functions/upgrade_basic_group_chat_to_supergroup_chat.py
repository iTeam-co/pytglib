

from ..utils import Object


class UpgradeBasicGroupChatToSupergroupChat(Object):
    """
    Creates a new supergroup from an existing basic group and sends a corresponding messageChatUpgradeTo and messageChatUpgradeFrom; requires creator privileges. Deactivates the original basic group 

    Attributes:
        ID (:obj:`str`): ``UpgradeBasicGroupChatToSupergroupChat``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to upgrade

    Returns:
        Chat

    Raises:
        :class:`telegram.Error`
    """
    ID = "upgradeBasicGroupChatToSupergroupChat"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "UpgradeBasicGroupChatToSupergroupChat":
        chat_id = q.get('chat_id')
        return UpgradeBasicGroupChatToSupergroupChat(chat_id)
