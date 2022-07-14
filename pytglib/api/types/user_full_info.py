

from ..utils import Object


class UserFullInfo(Object):
    """
    Contains full information about a user

    Attributes:
        ID (:obj:`str`): ``UserFullInfo``

    Args:
        photo (:class:`telegram.api.types.chatPhoto`):
            User profile photo; may be null
        is_blocked (:obj:`bool`):
            True, if the user is blocked by the current user
        can_be_called (:obj:`bool`):
            True, if the user can be called
        supports_video_calls (:obj:`bool`):
            True, if a video call can be created with the user
        has_private_calls (:obj:`bool`):
            True, if the user can't be called due to their privacy settings
        has_private_forwards (:obj:`bool`):
            True, if the user can't be linked in forwarded messages due to their privacy settings
        need_phone_number_privacy_exception (:obj:`bool`):
            True, if the current user needs to explicitly allow to share their phone number with the user when the method addContact is used
        bio (:class:`telegram.api.types.formattedText`):
            A short user bio; may be null for bots
        group_in_common_count (:obj:`int`):
            Number of group chats where both the other user and the current user are a member; 0 for the current user
        bot_info (:class:`telegram.api.types.botInfo`):
            For bots, information about the bot; may be null

    Returns:
        UserFullInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "userFullInfo"

    def __init__(self, photo, is_blocked, can_be_called, supports_video_calls, has_private_calls, has_private_forwards, need_phone_number_privacy_exception, bio, group_in_common_count, bot_info, **kwargs):
        
        self.photo = photo  # ChatPhoto
        self.is_blocked = is_blocked  # bool
        self.can_be_called = can_be_called  # bool
        self.supports_video_calls = supports_video_calls  # bool
        self.has_private_calls = has_private_calls  # bool
        self.has_private_forwards = has_private_forwards  # bool
        self.need_phone_number_privacy_exception = need_phone_number_privacy_exception  # bool
        self.bio = bio  # FormattedText
        self.group_in_common_count = group_in_common_count  # int
        self.bot_info = bot_info  # BotInfo

    @staticmethod
    def read(q: dict, *args) -> "UserFullInfo":
        photo = Object.read(q.get('photo'))
        is_blocked = q.get('is_blocked')
        can_be_called = q.get('can_be_called')
        supports_video_calls = q.get('supports_video_calls')
        has_private_calls = q.get('has_private_calls')
        has_private_forwards = q.get('has_private_forwards')
        need_phone_number_privacy_exception = q.get('need_phone_number_privacy_exception')
        bio = Object.read(q.get('bio'))
        group_in_common_count = q.get('group_in_common_count')
        bot_info = Object.read(q.get('bot_info'))
        return UserFullInfo(photo, is_blocked, can_be_called, supports_video_calls, has_private_calls, has_private_forwards, need_phone_number_privacy_exception, bio, group_in_common_count, bot_info)
