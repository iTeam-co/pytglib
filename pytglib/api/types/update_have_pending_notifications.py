

from ..utils import Object


class UpdateHavePendingNotifications(Object):
    """
    Describes whether there are some pending notification updates. Can be used to prevent application from killing, while there are some pending notifications

    Attributes:
        ID (:obj:`str`): ``UpdateHavePendingNotifications``

    Args:
        have_delayed_notifications (:obj:`bool`):
            True, if there are some delayed notification updates, which will be sent soon
        have_unreceived_notifications (:obj:`bool`):
            True, if there can be some yet unreceived notifications, which are being fetched from the server

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateHavePendingNotifications"

    def __init__(self, have_delayed_notifications, have_unreceived_notifications, **kwargs):
        
        self.have_delayed_notifications = have_delayed_notifications  # bool
        self.have_unreceived_notifications = have_unreceived_notifications  # bool

    @staticmethod
    def read(q: dict, *args) -> "UpdateHavePendingNotifications":
        have_delayed_notifications = q.get('have_delayed_notifications')
        have_unreceived_notifications = q.get('have_unreceived_notifications')
        return UpdateHavePendingNotifications(have_delayed_notifications, have_unreceived_notifications)
