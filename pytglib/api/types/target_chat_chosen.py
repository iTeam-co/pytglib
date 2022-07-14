

from ..utils import Object


class TargetChatChosen(Object):
    """
    The chat needs to be chosen by the user among chats of the specified types

    Attributes:
        ID (:obj:`str`): ``TargetChatChosen``

    Args:
        allow_user_chats (:obj:`bool`):
            True, if private chats with ordinary users are allowed
        allow_bot_chats (:obj:`bool`):
            True, if private chats with other bots are allowed
        allow_group_chats (:obj:`bool`):
            True, if basic group and supergroup chats are allowed
        allow_channel_chats (:obj:`bool`):
            True, if channel chats are allowed

    Returns:
        TargetChat

    Raises:
        :class:`telegram.Error`
    """
    ID = "targetChatChosen"

    def __init__(self, allow_user_chats, allow_bot_chats, allow_group_chats, allow_channel_chats, **kwargs):
        
        self.allow_user_chats = allow_user_chats  # bool
        self.allow_bot_chats = allow_bot_chats  # bool
        self.allow_group_chats = allow_group_chats  # bool
        self.allow_channel_chats = allow_channel_chats  # bool

    @staticmethod
    def read(q: dict, *args) -> "TargetChatChosen":
        allow_user_chats = q.get('allow_user_chats')
        allow_bot_chats = q.get('allow_bot_chats')
        allow_group_chats = q.get('allow_group_chats')
        allow_channel_chats = q.get('allow_channel_chats')
        return TargetChatChosen(allow_user_chats, allow_bot_chats, allow_group_chats, allow_channel_chats)
