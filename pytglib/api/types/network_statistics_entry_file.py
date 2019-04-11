

from ..utils import Object


class NetworkStatisticsEntryFile(Object):
    """
    Contains information about the total amount of data that was used to send and receive files 

    Attributes:
        ID (:obj:`str`): ``NetworkStatisticsEntryFile``

    Args:
        file_type (:class:`telegram.api.types.FileType`):
            Type of the file the data is part of 
        network_type (:class:`telegram.api.types.NetworkType`):
            Type of the network the data was sent throughCall setNetworkType to maintain the actual network type
        sent_bytes (:obj:`int`):
            Total number of bytes sent 
        received_bytes (:obj:`int`):
            Total number of bytes received

    Returns:
        NetworkStatisticsEntry

    Raises:
        :class:`telegram.Error`
    """
    ID = "networkStatisticsEntryFile"

    def __init__(self, file_type, network_type, sent_bytes, received_bytes, **kwargs):
        
        self.file_type = file_type  # FileType
        self.network_type = network_type  # NetworkType
        self.sent_bytes = sent_bytes  # int
        self.received_bytes = received_bytes  # int

    @staticmethod
    def read(q: dict, *args) -> "NetworkStatisticsEntryFile":
        file_type = Object.read(q.get('file_type'))
        network_type = Object.read(q.get('network_type'))
        sent_bytes = q.get('sent_bytes')
        received_bytes = q.get('received_bytes')
        return NetworkStatisticsEntryFile(file_type, network_type, sent_bytes, received_bytes)
