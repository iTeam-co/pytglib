

from ..utils import Object


class SearchMessagesFilterPhotoAndVideo(Object):
    """
    Returns only photo and video messages

    Attributes:
        ID (:obj:`str`): ``SearchMessagesFilterPhotoAndVideo``

    No parameters required.

    Returns:
        SearchMessagesFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessagesFilterPhotoAndVideo"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterPhotoAndVideo":
        
        return SearchMessagesFilterPhotoAndVideo()
