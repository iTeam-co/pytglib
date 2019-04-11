

from ..utils import Object


class SearchChatMembers(Object):
    """
    Searches for a specified query in the first name, last name and username of the members of a specified chat. Requires administrator rights in channels 

    Attributes:
        ID (:obj:`str`): ``SearchChatMembers``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        query (:obj:`str`):
            Query to search for 
        limit (:obj:`int`):
            The maximum number of users to be returned 
        filter (:class:`telegram.api.types.ChatMembersFilter`):
            The type of users to returnBy default, chatMembersFilterMembers

    Returns:
        ChatMembers

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchChatMembers"

    def __init__(self, chat_id, query, limit, filter, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.query = query  # str
        self.limit = limit  # int
        self.filter = filter  # ChatMembersFilter

    @staticmethod
    def read(q: dict, *args) -> "SearchChatMembers":
        chat_id = q.get('chat_id')
        query = q.get('query')
        limit = q.get('limit')
        filter = Object.read(q.get('filter'))
        return SearchChatMembers(chat_id, query, limit, filter)
