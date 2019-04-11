

from ..utils import Object


class BasicGroupFullInfo(Object):
    """
    Contains full information about a basic group 

    Attributes:
        ID (:obj:`str`): ``BasicGroupFullInfo``

    Args:
        creator_user_id (:obj:`int`):
            User identifier of the creator of the group; 0 if unknown 
        members (List of :class:`telegram.api.types.chatMember`):
            Group members 
        invite_link (:obj:`str`):
            Invite link for this group; available only for the group creator and only after it has been generated at least once

    Returns:
        BasicGroupFullInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "basicGroupFullInfo"

    def __init__(self, creator_user_id, members, invite_link, **kwargs):
        
        self.creator_user_id = creator_user_id  # int
        self.members = members  # list of chatMember
        self.invite_link = invite_link  # str

    @staticmethod
    def read(q: dict, *args) -> "BasicGroupFullInfo":
        creator_user_id = q.get('creator_user_id')
        members = [Object.read(i) for i in q.get('members', [])]
        invite_link = q.get('invite_link')
        return BasicGroupFullInfo(creator_user_id, members, invite_link)
