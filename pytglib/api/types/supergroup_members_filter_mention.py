

from ..utils import Object


class SupergroupMembersFilterMention(Object):
    """
    Returns users which can be mentioned in the supergroup 

    Attributes:
        ID (:obj:`str`): ``SupergroupMembersFilterMention``

    Args:
        query (:obj:`str`):
            Query to search for 
        message_thread_id (:obj:`int`):
            If non-zero, the identifier of the current message thread

    Returns:
        SupergroupMembersFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "supergroupMembersFilterMention"

    def __init__(self, query, message_thread_id, **kwargs):
        
        self.query = query  # str
        self.message_thread_id = message_thread_id  # int

    @staticmethod
    def read(q: dict, *args) -> "SupergroupMembersFilterMention":
        query = q.get('query')
        message_thread_id = q.get('message_thread_id')
        return SupergroupMembersFilterMention(query, message_thread_id)
