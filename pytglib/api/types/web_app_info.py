

from ..utils import Object


class WebAppInfo(Object):
    """
    Contains information about a Web App 

    Attributes:
        ID (:obj:`str`): ``WebAppInfo``

    Args:
        launch_id (:obj:`int`):
            Unique identifier for the Web App launch 
        url (:obj:`str`):
            A Web App URL to open in a web view

    Returns:
        WebAppInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "webAppInfo"

    def __init__(self, launch_id, url, **kwargs):
        
        self.launch_id = launch_id  # int
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "WebAppInfo":
        launch_id = q.get('launch_id')
        url = q.get('url')
        return WebAppInfo(launch_id, url)
