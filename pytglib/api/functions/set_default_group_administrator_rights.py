

from ..utils import Object


class SetDefaultGroupAdministratorRights(Object):
    """
    Sets default administrator rights for adding the bot to basic group and supergroup chats; for bots only 

    Attributes:
        ID (:obj:`str`): ``SetDefaultGroupAdministratorRights``

    Args:
        default_group_administrator_rights (:class:`telegram.api.types.chatAdministratorRights`):
            Default administrator rights for adding the bot to basic group and supergroup chats; may be null

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setDefaultGroupAdministratorRights"

    def __init__(self, default_group_administrator_rights, extra=None, **kwargs):
        self.extra = extra
        self.default_group_administrator_rights = default_group_administrator_rights  # ChatAdministratorRights

    @staticmethod
    def read(q: dict, *args) -> "SetDefaultGroupAdministratorRights":
        default_group_administrator_rights = Object.read(q.get('default_group_administrator_rights'))
        return SetDefaultGroupAdministratorRights(default_group_administrator_rights)
