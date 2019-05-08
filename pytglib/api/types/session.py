

from ..utils import Object


class Session(Object):
    """
    Contains information about one session in a Telegram application used by the current user. Sessions should be shown to the user in the returned order

    Attributes:
        ID (:obj:`str`): ``Session``

    Args:
        id (:obj:`int`):
            Session identifier 
        is_current (:obj:`bool`):
            True, if this session is the current session
        is_password_pending (:obj:`bool`):
            True, if a password is needed to complete authorization of the session
        api_id (:obj:`int`):
            Telegram API identifier, as provided by the application 
        application_name (:obj:`str`):
            Name of the application, as provided by the application
        application_version (:obj:`str`):
            The version of the application, as provided by the application 
        is_official_application (:obj:`bool`):
            True, if the application is an official application or uses the api_id of an official application
        device_model (:obj:`str`):
            Model of the device the application has been run or is running on, as provided by the application 
        platform (:obj:`str`):
            Operating system the application has been run or is running on, as provided by the application
        system_version (:obj:`str`):
            Version of the operating system the application has been run or is running on, as provided by the application 
        log_in_date (:obj:`int`):
            Point in time (Unix timestamp) when the user has logged in
        last_active_date (:obj:`int`):
            Point in time (Unix timestamp) when the session was last used 
        ip (:obj:`str`):
            IP address from which the session was created, in human-readable format
        country (:obj:`str`):
            A two-letter country code for the country from which the session was created, based on the IP address 
        region (:obj:`str`):
            Region code from which the session was created, based on the IP address

    Returns:
        Session

    Raises:
        :class:`telegram.Error`
    """
    ID = "session"

    def __init__(self, id, is_current, is_password_pending, api_id, application_name, application_version, is_official_application, device_model, platform, system_version, log_in_date, last_active_date, ip, country, region, **kwargs):
        
        self.id = id  # int
        self.is_current = is_current  # bool
        self.is_password_pending = is_password_pending  # bool
        self.api_id = api_id  # int
        self.application_name = application_name  # str
        self.application_version = application_version  # str
        self.is_official_application = is_official_application  # bool
        self.device_model = device_model  # str
        self.platform = platform  # str
        self.system_version = system_version  # str
        self.log_in_date = log_in_date  # int
        self.last_active_date = last_active_date  # int
        self.ip = ip  # str
        self.country = country  # str
        self.region = region  # str

    @staticmethod
    def read(q: dict, *args) -> "Session":
        id = q.get('id')
        is_current = q.get('is_current')
        is_password_pending = q.get('is_password_pending')
        api_id = q.get('api_id')
        application_name = q.get('application_name')
        application_version = q.get('application_version')
        is_official_application = q.get('is_official_application')
        device_model = q.get('device_model')
        platform = q.get('platform')
        system_version = q.get('system_version')
        log_in_date = q.get('log_in_date')
        last_active_date = q.get('last_active_date')
        ip = q.get('ip')
        country = q.get('country')
        region = q.get('region')
        return Session(id, is_current, is_password_pending, api_id, application_name, application_version, is_official_application, device_model, platform, system_version, log_in_date, last_active_date, ip, country, region)
