

from ..utils import Object


class ChatMember(Object):
    """
    A user with information about joining/leaving a chat 

    Attributes:
        ID (:obj:`str`): ``ChatMember``

    Args:
        user_id (:obj:`int`):
            User identifier of the chat member 
        inviter_user_id (:obj:`int`):
            Identifier of a user that invited/promoted/banned this member in the chat; 0 if unknown
        joined_chat_date (:obj:`int`):
            Point in time (Unix timestamp) when the user joined a chat 
        status (:class:`telegram.api.types.ChatMemberStatus`):
            Status of the member in the chat 
        bot_info (:class:`telegram.api.types.botInfo`):
            If the user is a bot, information about the bot; may be nullCan be null even for a bot if the bot is not a chat member

    Returns:
        ChatMember

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMember"

    def __init__(self, user_id, inviter_user_id, joined_chat_date, status, bot_info, **kwargs):
        
        self.user_id = user_id  # int
        self.inviter_user_id = inviter_user_id  # int
        self.joined_chat_date = joined_chat_date  # int
        self.status = status  # ChatMemberStatus
        self.bot_info = bot_info  # BotInfo

    @staticmethod
    def read(q: dict, *args) -> "ChatMember":
        user_id = q.get('user_id')
        inviter_user_id = q.get('inviter_user_id')
        joined_chat_date = q.get('joined_chat_date')
        status = Object.read(q.get('status'))
        bot_info = Object.read(q.get('bot_info'))
        return ChatMember(user_id, inviter_user_id, joined_chat_date, status, bot_info)
