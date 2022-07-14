

from ..utils import Object


class PushMessageContentMediaAlbum(Object):
    """
    A media album 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentMediaAlbum``

    Args:
        total_count (:obj:`int`):
            Number of messages in the album 
        has_photos (:obj:`bool`):
            True, if the album has at least one photo 
        has_videos (:obj:`bool`):
            True, if the album has at least one video
        has_audios (:obj:`bool`):
            True, if the album has at least one audio file 
        has_documents (:obj:`bool`):
            True, if the album has at least one document

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentMediaAlbum"

    def __init__(self, total_count, has_photos, has_videos, has_audios, has_documents, **kwargs):
        
        self.total_count = total_count  # int
        self.has_photos = has_photos  # bool
        self.has_videos = has_videos  # bool
        self.has_audios = has_audios  # bool
        self.has_documents = has_documents  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentMediaAlbum":
        total_count = q.get('total_count')
        has_photos = q.get('has_photos')
        has_videos = q.get('has_videos')
        has_audios = q.get('has_audios')
        has_documents = q.get('has_documents')
        return PushMessageContentMediaAlbum(total_count, has_photos, has_videos, has_audios, has_documents)
