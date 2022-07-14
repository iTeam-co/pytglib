

from ..utils import Object


class DeleteAllRevokedChatInviteLinks(Object):
    """
    Deletes all revoked chat invite links created by a given chat administrator. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links

    Attributes:
        ID (:obj:`str`): ``DeleteAllRevokedChatInviteLinks``

    Args:
        chat_id (:obj:`int`):
            Chat identifier
        creator_user_id (:obj:`int`):
            User identifier of a chat administrator, which links will be deletedMust be an identifier of the current user for non-owner

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteAllRevokedChatInviteLinks"

    def __init__(self, chat_id, creator_user_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.creator_user_id = creator_user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "DeleteAllRevokedChatInviteLinks":
        chat_id = q.get('chat_id')
        creator_user_id = q.get('creator_user_id')
        return DeleteAllRevokedChatInviteLinks(chat_id, creator_user_id)
