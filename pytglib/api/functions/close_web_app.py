

from ..utils import Object


class CloseWebApp(Object):
    """
    Informs TDLib that a previously opened Web App was closed 

    Attributes:
        ID (:obj:`str`): ``CloseWebApp``

    Args:
        web_app_launch_id (:obj:`int`):
            Identifier of Web App launch, received from openWebApp

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "closeWebApp"

    def __init__(self, web_app_launch_id, extra=None, **kwargs):
        self.extra = extra
        self.web_app_launch_id = web_app_launch_id  # int

    @staticmethod
    def read(q: dict, *args) -> "CloseWebApp":
        web_app_launch_id = q.get('web_app_launch_id')
        return CloseWebApp(web_app_launch_id)
