

from ..utils import Object


class UpdateWebAppMessageSent(Object):
    """
    A message was sent by an opened Web App, so the Web App needs to be closed 

    Attributes:
        ID (:obj:`str`): ``UpdateWebAppMessageSent``

    Args:
        web_app_launch_id (:obj:`int`):
            Identifier of Web App launch

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateWebAppMessageSent"

    def __init__(self, web_app_launch_id, **kwargs):
        
        self.web_app_launch_id = web_app_launch_id  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateWebAppMessageSent":
        web_app_launch_id = q.get('web_app_launch_id')
        return UpdateWebAppMessageSent(web_app_launch_id)
