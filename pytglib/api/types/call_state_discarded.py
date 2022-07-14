

from ..utils import Object


class CallStateDiscarded(Object):
    """
    The call has ended successfully 

    Attributes:
        ID (:obj:`str`): ``CallStateDiscarded``

    Args:
        reason (:class:`telegram.api.types.CallDiscardReason`):
            The reason, why the call has ended 
        need_rating (:obj:`bool`):
            True, if the call rating must be sent to the server 
        need_debug_information (:obj:`bool`):
            True, if the call debug information must be sent to the server 
        need_log (:obj:`bool`):
            True, if the call log must be sent to the server

    Returns:
        CallState

    Raises:
        :class:`telegram.Error`
    """
    ID = "callStateDiscarded"

    def __init__(self, reason, need_rating, need_debug_information, need_log, **kwargs):
        
        self.reason = reason  # CallDiscardReason
        self.need_rating = need_rating  # bool
        self.need_debug_information = need_debug_information  # bool
        self.need_log = need_log  # bool

    @staticmethod
    def read(q: dict, *args) -> "CallStateDiscarded":
        reason = Object.read(q.get('reason'))
        need_rating = q.get('need_rating')
        need_debug_information = q.get('need_debug_information')
        need_log = q.get('need_log')
        return CallStateDiscarded(reason, need_rating, need_debug_information, need_log)
