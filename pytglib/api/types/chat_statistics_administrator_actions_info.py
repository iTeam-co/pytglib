

from ..utils import Object


class ChatStatisticsAdministratorActionsInfo(Object):
    """
    Contains statistics about administrator actions done by a user

    Attributes:
        ID (:obj:`str`): ``ChatStatisticsAdministratorActionsInfo``

    Args:
        user_id (:obj:`int`):
            Administrator user identifier
        deleted_message_count (:obj:`int`):
            Number of messages deleted by the administrator
        banned_user_count (:obj:`int`):
            Number of users banned by the administrator
        restricted_user_count (:obj:`int`):
            Number of users restricted by the administrator

    Returns:
        ChatStatisticsAdministratorActionsInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatStatisticsAdministratorActionsInfo"

    def __init__(self, user_id, deleted_message_count, banned_user_count, restricted_user_count, **kwargs):
        
        self.user_id = user_id  # int
        self.deleted_message_count = deleted_message_count  # int
        self.banned_user_count = banned_user_count  # int
        self.restricted_user_count = restricted_user_count  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatStatisticsAdministratorActionsInfo":
        user_id = q.get('user_id')
        deleted_message_count = q.get('deleted_message_count')
        banned_user_count = q.get('banned_user_count')
        restricted_user_count = q.get('restricted_user_count')
        return ChatStatisticsAdministratorActionsInfo(user_id, deleted_message_count, banned_user_count, restricted_user_count)
