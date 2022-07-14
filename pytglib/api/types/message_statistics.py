

from ..utils import Object


class MessageStatistics(Object):
    """
    A detailed statistics about a message 

    Attributes:
        ID (:obj:`str`): ``MessageStatistics``

    Args:
        message_interaction_graph (:class:`telegram.api.types.StatisticalGraph`):
            A graph containing number of message views and shares

    Returns:
        MessageStatistics

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageStatistics"

    def __init__(self, message_interaction_graph, **kwargs):
        
        self.message_interaction_graph = message_interaction_graph  # StatisticalGraph

    @staticmethod
    def read(q: dict, *args) -> "MessageStatistics":
        message_interaction_graph = Object.read(q.get('message_interaction_graph'))
        return MessageStatistics(message_interaction_graph)
