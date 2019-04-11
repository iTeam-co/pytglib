

from ..utils import Object


class ChatEventDescriptionChanged(Object):
    """
    The chat description was changed 

    Attributes:
        ID (:obj:`str`): ``ChatEventDescriptionChanged``

    Args:
        old_description (:obj:`str`):
            Previous chat description 
        new_description (:obj:`str`):
            New chat description

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventDescriptionChanged"

    def __init__(self, old_description, new_description, **kwargs):
        
        self.old_description = old_description  # str
        self.new_description = new_description  # str

    @staticmethod
    def read(q: dict, *args) -> "ChatEventDescriptionChanged":
        old_description = q.get('old_description')
        new_description = q.get('new_description')
        return ChatEventDescriptionChanged(old_description, new_description)
