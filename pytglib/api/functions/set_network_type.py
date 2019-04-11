

from ..utils import Object


class SetNetworkType(Object):
    """
    Sets the current network type. Can be called before authorization. Calling this method forces all network connections to reopen, mitigating the delay in switching between different networks, so it should be called whenever the network is changed, even if the network type remains the same.Network type is used to check whether the library can use the network at all and also for collecting detailed network data usage statistics 

    Attributes:
        ID (:obj:`str`): ``SetNetworkType``

    Args:
        type (:class:`telegram.api.types.NetworkType`):
            The new network typeBy default, networkTypeOther

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setNetworkType"

    def __init__(self, type, extra=None, **kwargs):
        self.extra = extra
        self.type = type  # NetworkType

    @staticmethod
    def read(q: dict, *args) -> "SetNetworkType":
        type = Object.read(q.get('type'))
        return SetNetworkType(type)
