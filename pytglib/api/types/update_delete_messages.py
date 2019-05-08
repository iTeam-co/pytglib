

from ..utils import Object


class UpdateDeleteMessages(Object):
    """
    Some messages were deleted 

    Attributes:
        ID (:obj:`str`): ``UpdateDeleteMessages``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_ids (List of :obj:`int`):
            Identifiers of the deleted messages
        is_permanent (:obj:`bool`):
            True, if the messages are permanently deleted by a user (as opposed to just becoming inaccessible)
        from_cache (:obj:`bool`):
            True, if the messages are deleted only from the cache and can possibly be retrieved again in the future

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateDeleteMessages"

    def __init__(self, chat_id, message_ids, is_permanent, from_cache, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_ids = message_ids  # list of int
        self.is_permanent = is_permanent  # bool
        self.from_cache = from_cache  # bool

    @staticmethod
    def read(q: dict, *args) -> "UpdateDeleteMessages":
        chat_id = q.get('chat_id')
        message_ids = q.get('message_ids')
        is_permanent = q.get('is_permanent')
        from_cache = q.get('from_cache')
        return UpdateDeleteMessages(chat_id, message_ids, is_permanent, from_cache)
