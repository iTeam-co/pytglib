

from ..utils import Object


class SearchFileDownloads(Object):
    """
    Searches for files in the file download list or recently downloaded files from the list

    Attributes:
        ID (:obj:`str`): ``SearchFileDownloads``

    Args:
        query (:obj:`str`):
            Query to search for; may be empty to return all downloaded files
        only_active (:obj:`bool`):
            Pass true to search only for active downloads, including paused
        only_completed (:obj:`bool`):
            Pass true to search only for completed downloads
        offset (:obj:`str`):
            Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        limit (:obj:`int`):
            The maximum number of files to be returned

    Returns:
        FoundFileDownloads

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchFileDownloads"

    def __init__(self, query, only_active, only_completed, offset, limit, extra=None, **kwargs):
        self.extra = extra
        self.query = query  # str
        self.only_active = only_active  # bool
        self.only_completed = only_completed  # bool
        self.offset = offset  # str
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "SearchFileDownloads":
        query = q.get('query')
        only_active = q.get('only_active')
        only_completed = q.get('only_completed')
        offset = q.get('offset')
        limit = q.get('limit')
        return SearchFileDownloads(query, only_active, only_completed, offset, limit)
