

from ..utils import Object


class NetworkStatisticsEntryCall(Object):
    """
    Contains information about the total amount of data that was used for calls 

    Attributes:
        ID (:obj:`str`): ``NetworkStatisticsEntryCall``

    Args:
        network_type (:class:`telegram.api.types.NetworkType`):
            Type of the network the data was sent throughCall setNetworkType to maintain the actual network type
        sent_bytes (:obj:`int`):
            Total number of bytes sent 
        received_bytes (:obj:`int`):
            Total number of bytes received 
        duration (:obj:`float`):
            Total call duration, in seconds

    Returns:
        NetworkStatisticsEntry

    Raises:
        :class:`telegram.Error`
    """
    ID = "networkStatisticsEntryCall"

    def __init__(self, network_type, sent_bytes, received_bytes, duration, **kwargs):
        
        self.network_type = network_type  # NetworkType
        self.sent_bytes = sent_bytes  # int
        self.received_bytes = received_bytes  # int
        self.duration = duration  # float

    @staticmethod
    def read(q: dict, *args) -> "NetworkStatisticsEntryCall":
        network_type = Object.read(q.get('network_type'))
        sent_bytes = q.get('sent_bytes')
        received_bytes = q.get('received_bytes')
        duration = q.get('duration')
        return NetworkStatisticsEntryCall(network_type, sent_bytes, received_bytes, duration)
