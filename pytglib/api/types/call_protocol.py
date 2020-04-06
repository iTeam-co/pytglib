

from ..utils import Object


class CallProtocol(Object):
    """
    Specifies the supported call protocols

    Attributes:
        ID (:obj:`str`): ``CallProtocol``

    Args:
        udp_p2p (:obj:`bool`):
            True, if UDP peer-to-peer connections are supported
        udp_reflector (:obj:`bool`):
            True, if connection through UDP reflectors is supported
        min_layer (:obj:`int`):
            The minimum supported API layer; use 65
        max_layer (:obj:`int`):
            The maximum supported API layer; use 65
        library_versions (List of :obj:`str`):
            List of supported libtgvoip versions

    Returns:
        CallProtocol

    Raises:
        :class:`telegram.Error`
    """
    ID = "callProtocol"

    def __init__(self, udp_p2p, udp_reflector, min_layer, max_layer, library_versions, **kwargs):
        
        self.udp_p2p = udp_p2p  # bool
        self.udp_reflector = udp_reflector  # bool
        self.min_layer = min_layer  # int
        self.max_layer = max_layer  # int
        self.library_versions = library_versions  # list of str

    @staticmethod
    def read(q: dict, *args) -> "CallProtocol":
        udp_p2p = q.get('udp_p2p')
        udp_reflector = q.get('udp_reflector')
        min_layer = q.get('min_layer')
        max_layer = q.get('max_layer')
        library_versions = q.get('library_versions')
        return CallProtocol(udp_p2p, udp_reflector, min_layer, max_layer, library_versions)
