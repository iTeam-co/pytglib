

from ..utils import Object


class UpdateDiceEmojis(Object):
    """
    The list of supported dice emojis has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateDiceEmojis``

    Args:
        emojis (List of :obj:`str`):
            The new list of supported dice emojis

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateDiceEmojis"

    def __init__(self, emojis, **kwargs):
        
        self.emojis = emojis  # list of str

    @staticmethod
    def read(q: dict, *args) -> "UpdateDiceEmojis":
        emojis = q.get('emojis')
        return UpdateDiceEmojis(emojis)
