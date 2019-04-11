

from ..utils import Object


class SearchMessagesFilterAnimation(Object):
    """
    Returns only animation messages

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterAnimation``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterAnimation"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterAnimation":
        
        return SearchMessagesFilterAnimation()
