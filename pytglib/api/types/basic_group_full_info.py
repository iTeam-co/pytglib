

from ..utils import Object


class BasicGroupFullInfo(Object):
    """
    Contains full information about a basic group

    Attributes:
        ID (:obj:`str`): ``BasicGroupFullInfo``

    Args:
        photo (:class:`telegram.api.types.chatPhoto`):
            Chat photo; may be null
        description (:obj:`str`):
            Group descriptionUpdated only after the basic group is opened
        creator_user_id (:obj:`int`):
            User identifier of the creator of the group; 0 if unknown
        members (List of :class:`telegram.api.types.chatMember`):
            Group members
        invite_link (:class:`telegram.api.types.chatInviteLink`):
            Primary invite link for this group; may be nullFor chat administrators with can_invite_users right onlyUpdated only after the basic group is opened
        bot_commands (List of :class:`telegram.api.types.botCommands`):
            List of commands of bots in the group

    Returns:
        BasicGroupFullInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "basicGroupFullInfo"

    def __init__(self, photo, description, creator_user_id, members, invite_link, bot_commands, **kwargs):
        
        self.photo = photo  # ChatPhoto
        self.description = description  # str
        self.creator_user_id = creator_user_id  # int
        self.members = members  # list of chatMember
        self.invite_link = invite_link  # ChatInviteLink
        self.bot_commands = bot_commands  # list of botCommands

    @staticmethod
    def read(q: dict, *args) -> "BasicGroupFullInfo":
        photo = Object.read(q.get('photo'))
        description = q.get('description')
        creator_user_id = q.get('creator_user_id')
        members = [Object.read(i) for i in q.get('members', [])]
        invite_link = Object.read(q.get('invite_link'))
        bot_commands = [Object.read(i) for i in q.get('bot_commands', [])]
        return BasicGroupFullInfo(photo, description, creator_user_id, members, invite_link, bot_commands)
