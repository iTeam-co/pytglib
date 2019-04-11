

from ..utils import Object


class SetBio(Object):
    """
    Changes the bio of the current user 

    Attributes:
        ID (:obj:`str`): ``SetBio``

    Args:
        bio (:obj:`str`):
            The new value of the user bio; 0-70 characters without line feeds

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setBio"

    def __init__(self, bio, extra=None, **kwargs):
        self.extra = extra
        self.bio = bio  # str

    @staticmethod
    def read(q: dict, *args) -> "SetBio":
        bio = q.get('bio')
        return SetBio(bio)
