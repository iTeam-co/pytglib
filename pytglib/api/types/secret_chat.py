

from ..utils import Object


class SecretChat(Object):
    """
    Represents a secret chat

    Attributes:
        ID (:obj:`str`): ``SecretChat``

    Args:
        id (:obj:`int`):
            Secret chat identifier
        user_id (:obj:`int`):
            Identifier of the chat partner
        state (:class:`telegram.api.types.SecretChatState`):
            State of the secret chat
        is_outbound (:obj:`bool`):
            True, if the chat was created by the current user; otherwise false
        ttl (:obj:`int`):
            Current message Time To Live setting (self-destruct timer) for the chat, in seconds
        key_hash (:obj:`bytes`):
            Hash of the currently used key for comparison with the hash of the chat partner's keyThis is a string of 36 little-endian bytes, which must be split into groups of 2 bits, each denoting a pixel of one of 4 colors FFFFFF, D5E6F3, 2D5775, and 2F99C9The pixels must be used to make a 12x12 square image filled from left to right, top to bottomAlternatively, the first 32 bytes of the hash can be converted to the hexadecimal format and printed as 32 2-digit hex numbers
        layer (:obj:`int`):
            Secret chat layer; determines features supported by the other clientVideo notes are supported if the layer >= 66; nested text entities and underline and strikethrough entities are supported if the layer >= 101

    Returns:
        SecretChat

    Raises:
        :class:`telegram.Error`
    """
    ID = "secretChat"

    def __init__(self, id, user_id, state, is_outbound, ttl, key_hash, layer, **kwargs):
        
        self.id = id  # int
        self.user_id = user_id  # int
        self.state = state  # SecretChatState
        self.is_outbound = is_outbound  # bool
        self.ttl = ttl  # int
        self.key_hash = key_hash  # bytes
        self.layer = layer  # int

    @staticmethod
    def read(q: dict, *args) -> "SecretChat":
        id = q.get('id')
        user_id = q.get('user_id')
        state = Object.read(q.get('state'))
        is_outbound = q.get('is_outbound')
        ttl = q.get('ttl')
        key_hash = q.get('key_hash')
        layer = q.get('layer')
        return SecretChat(id, user_id, state, is_outbound, ttl, key_hash, layer)
