

from ..utils import Object


class UpdateAnimationSearchParameters(Object):
    """
    The parameters of animation search through GetOption("animation_search_bot_username") bot has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateAnimationSearchParameters``

    Args:
        provider (:obj:`str`):
            Name of the animation search provider 
        emojis (List of :obj:`str`):
            The new list of emojis suggested for searching

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateAnimationSearchParameters"

    def __init__(self, provider, emojis, **kwargs):
        
        self.provider = provider  # str
        self.emojis = emojis  # list of str

    @staticmethod
    def read(q: dict, *args) -> "UpdateAnimationSearchParameters":
        provider = q.get('provider')
        emojis = q.get('emojis')
        return UpdateAnimationSearchParameters(provider, emojis)
