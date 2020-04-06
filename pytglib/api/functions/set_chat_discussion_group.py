

from ..utils import Object


class SetChatDiscussionGroup(Object):
    """
    Changes the discussion group of a channel chat; requires can_change_info rights in the channel if it is specified 

    Attributes:
        ID (:obj:`str`): ``SetChatDiscussionGroup``

    Args:
        chat_id (:obj:`int`):
            Identifier of the channel chatPass 0 to remove a link from the supergroup passed in the second argument to a linked channel chat (requires can_pin_messages rights in the supergroup) 
        discussion_chat_id (:obj:`int`):
            Identifier of a new channel's discussion groupUse 0 to remove the discussion groupUse the method getSuitableDiscussionChats to find all suitable groupsBasic group chats needs to be first upgraded to supergroup chatsIf new chat members don't have access to old messages in the supergroup, then toggleSupergroupIsAllHistoryAvailable needs to be used first to change that

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatDiscussionGroup"

    def __init__(self, chat_id, discussion_chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.discussion_chat_id = discussion_chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "SetChatDiscussionGroup":
        chat_id = q.get('chat_id')
        discussion_chat_id = q.get('discussion_chat_id')
        return SetChatDiscussionGroup(chat_id, discussion_chat_id)
