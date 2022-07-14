

from ..utils import Object


class SuggestedActionEnableArchiveAndMuteNewChats(Object):
    """
    Suggests the user to enable "archive_and_mute_new_chats_from_unknown_users" option

    Attributes:
        ID (:obj:`str`): ``SuggestedActionEnableArchiveAndMuteNewChats``

    No parameters required.

    Returns:
        SuggestedAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "suggestedActionEnableArchiveAndMuteNewChats"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SuggestedActionEnableArchiveAndMuteNewChats":
        
        return SuggestedActionEnableArchiveAndMuteNewChats()
