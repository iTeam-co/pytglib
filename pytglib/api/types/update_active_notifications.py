

from ..utils import Object


class UpdateActiveNotifications(Object):
    """
    Contains active notifications that was shown on previous application launches. This update is sent only if the message database is used. In that case it comes once before any updateNotification and updateNotificationGroup update 

    Attributes:
        ID (:obj:`str`): ``UpdateActiveNotifications``

    Args:
        groups (List of :class:`telegram.api.types.notificationGroup`):
            Lists of active notification groups

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateActiveNotifications"

    def __init__(self, groups, **kwargs):
        
        self.groups = groups  # list of notificationGroup

    @staticmethod
    def read(q: dict, *args) -> "UpdateActiveNotifications":
        groups = [Object.read(i) for i in q.get('groups', [])]
        return UpdateActiveNotifications(groups)
