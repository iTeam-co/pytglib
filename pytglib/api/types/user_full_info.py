

from ..utils import Object


class UserFullInfo(Object):
    """
    Contains full information about a user (except the full list of profile photos) 

    Attributes:
        ID (:obj:`str`): ``UserFullInfo``

    Args:
        is_blocked (:obj:`bool`):
            True, if the user is blacklisted by the current user
        can_be_called (:obj:`bool`):
            True, if the user can be called 
        has_private_calls (:obj:`bool`):
            True, if the user can't be called due to their privacy settings
        need_phone_number_privacy_exception (:obj:`bool`):
            True, if the current user needs to explicitly allow to share their phone number with the user when the method addContact is used
        bio (:obj:`str`):
            A short user bio 
        share_text (:obj:`str`):
            For bots, the text that is included with the link when users share the bot 
        group_in_common_count (:obj:`int`):
            Number of group chats where both the other user and the current user are a member; 0 for the current user 
        bot_info (:class:`telegram.api.types.botInfo`):
            If the user is a bot, information about the bot; may be null

    Returns:
        UserFullInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "userFullInfo"

    def __init__(self, is_blocked, can_be_called, has_private_calls, need_phone_number_privacy_exception, bio, share_text, group_in_common_count, bot_info, **kwargs):
        
        self.is_blocked = is_blocked  # bool
        self.can_be_called = can_be_called  # bool
        self.has_private_calls = has_private_calls  # bool
        self.need_phone_number_privacy_exception = need_phone_number_privacy_exception  # bool
        self.bio = bio  # str
        self.share_text = share_text  # str
        self.group_in_common_count = group_in_common_count  # int
        self.bot_info = bot_info  # BotInfo

    @staticmethod
    def read(q: dict, *args) -> "UserFullInfo":
        is_blocked = q.get('is_blocked')
        can_be_called = q.get('can_be_called')
        has_private_calls = q.get('has_private_calls')
        need_phone_number_privacy_exception = q.get('need_phone_number_privacy_exception')
        bio = q.get('bio')
        share_text = q.get('share_text')
        group_in_common_count = q.get('group_in_common_count')
        bot_info = Object.read(q.get('bot_info'))
        return UserFullInfo(is_blocked, can_be_called, has_private_calls, need_phone_number_privacy_exception, bio, share_text, group_in_common_count, bot_info)
