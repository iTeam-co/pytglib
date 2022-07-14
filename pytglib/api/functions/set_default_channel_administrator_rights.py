

from ..utils import Object


class SetDefaultChannelAdministratorRights(Object):
    """
    Sets default administrator rights for adding the bot to channel chats; for bots only 

    Attributes:
        ID (:obj:`str`): ``SetDefaultChannelAdministratorRights``

    Args:
        default_channel_administrator_rights (:class:`telegram.api.types.chatAdministratorRights`):
            Default administrator rights for adding the bot to channels; may be null

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setDefaultChannelAdministratorRights"

    def __init__(self, default_channel_administrator_rights, extra=None, **kwargs):
        self.extra = extra
        self.default_channel_administrator_rights = default_channel_administrator_rights  # ChatAdministratorRights

    @staticmethod
    def read(q: dict, *args) -> "SetDefaultChannelAdministratorRights":
        default_channel_administrator_rights = Object.read(q.get('default_channel_administrator_rights'))
        return SetDefaultChannelAdministratorRights(default_channel_administrator_rights)
