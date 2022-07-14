

from ..utils import Object


class UpdateNotificationGroup(Object):
    """
    A list of active notifications in a notification group has changed

    Attributes:
        ID (:obj:`str`): ``UpdateNotificationGroup``

    Args:
        notification_group_id (:obj:`int`):
            Unique notification group identifier
        type (:class:`telegram.api.types.NotificationGroupType`):
            New type of the notification group
        chat_id (:obj:`int`):
            Identifier of a chat to which all notifications in the group belong
        notification_settings_chat_id (:obj:`int`):
            Chat identifier, which notification settings must be applied to the added notifications
        notification_sound_id (:obj:`int`):
            Identifier of the notification sound to be played; 0 if sound is disabled
        total_count (:obj:`int`):
            Total number of unread notifications in the group, can be bigger than number of active notifications
        added_notifications (List of :class:`telegram.api.types.notification`):
            List of added group notifications, sorted by notification ID 
        removed_notification_ids (List of :obj:`int`):
            Identifiers of removed group notifications, sorted by notification ID

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateNotificationGroup"

    def __init__(self, notification_group_id, type, chat_id, notification_settings_chat_id, notification_sound_id, total_count, added_notifications, removed_notification_ids, **kwargs):
        
        self.notification_group_id = notification_group_id  # int
        self.type = type  # NotificationGroupType
        self.chat_id = chat_id  # int
        self.notification_settings_chat_id = notification_settings_chat_id  # int
        self.notification_sound_id = notification_sound_id  # int
        self.total_count = total_count  # int
        self.added_notifications = added_notifications  # list of notification
        self.removed_notification_ids = removed_notification_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "UpdateNotificationGroup":
        notification_group_id = q.get('notification_group_id')
        type = Object.read(q.get('type'))
        chat_id = q.get('chat_id')
        notification_settings_chat_id = q.get('notification_settings_chat_id')
        notification_sound_id = q.get('notification_sound_id')
        total_count = q.get('total_count')
        added_notifications = [Object.read(i) for i in q.get('added_notifications', [])]
        removed_notification_ids = q.get('removed_notification_ids')
        return UpdateNotificationGroup(notification_group_id, type, chat_id, notification_settings_chat_id, notification_sound_id, total_count, added_notifications, removed_notification_ids)
