

from ..utils import Object


class TdlibParameters(Object):
    """
    Contains parameters for TDLib initialization

    Attributes:
        ID (:obj:`str`): ``TdlibParameters``

    Args:
        use_test_dc (:obj:`bool`):
            If set to true, the Telegram test environment will be used instead of the production environment
        database_directory (:obj:`str`):
            The path to the directory for the persistent database; if empty, the current working directory will be used
        files_directory (:obj:`str`):
            The path to the directory for storing files; if empty, database_directory will be used
        use_file_database (:obj:`bool`):
            If set to true, information about downloaded and uploaded files will be saved between application restarts
        use_chat_info_database (:obj:`bool`):
            If set to true, the library will maintain a cache of users, basic groups, supergroups, channels and secret chatsImplies use_file_database
        use_message_database (:obj:`bool`):
            If set to true, the library will maintain a cache of chats and messagesImplies use_chat_info_database
        use_secret_chats (:obj:`bool`):
            If set to true, support for secret chats will be enabled
        api_id (:obj:`int`):
            Application identifier for Telegram API access, which can be obtained at https://mytelegramorg
        api_hash (:obj:`str`):
            Application identifier hash for Telegram API access, which can be obtained at https://mytelegramorg
        system_language_code (:obj:`str`):
            IETF language tag of the user's operating system language; must be non-empty
        device_model (:obj:`str`):
            Model of the device the application is being run on; must be non-empty
        system_version (:obj:`str`):
            Version of the operating system the application is being run on; must be non-empty
        application_version (:obj:`str`):
            Application version; must be non-empty
        enable_storage_optimizer (:obj:`bool`):
            If set to true, old files will automatically be deleted
        ignore_file_names (:obj:`bool`):
            If set to true, original file names will be ignoredOtherwise, downloaded files will be saved under names as close as possible to the original name

    Returns:
        TdlibParameters

    Raises:
        :class:`telegram.Error`
    """
    ID = "tdlibParameters"

    def __init__(self, use_test_dc, database_directory, files_directory, use_file_database, use_chat_info_database, use_message_database, use_secret_chats, api_id, api_hash, system_language_code, device_model, system_version, application_version, enable_storage_optimizer, ignore_file_names, **kwargs):
        
        self.use_test_dc = use_test_dc  # bool
        self.database_directory = database_directory  # str
        self.files_directory = files_directory  # str
        self.use_file_database = use_file_database  # bool
        self.use_chat_info_database = use_chat_info_database  # bool
        self.use_message_database = use_message_database  # bool
        self.use_secret_chats = use_secret_chats  # bool
        self.api_id = api_id  # int
        self.api_hash = api_hash  # str
        self.system_language_code = system_language_code  # str
        self.device_model = device_model  # str
        self.system_version = system_version  # str
        self.application_version = application_version  # str
        self.enable_storage_optimizer = enable_storage_optimizer  # bool
        self.ignore_file_names = ignore_file_names  # bool

    @staticmethod
    def read(q: dict, *args) -> "TdlibParameters":
        use_test_dc = q.get('use_test_dc')
        database_directory = q.get('database_directory')
        files_directory = q.get('files_directory')
        use_file_database = q.get('use_file_database')
        use_chat_info_database = q.get('use_chat_info_database')
        use_message_database = q.get('use_message_database')
        use_secret_chats = q.get('use_secret_chats')
        api_id = q.get('api_id')
        api_hash = q.get('api_hash')
        system_language_code = q.get('system_language_code')
        device_model = q.get('device_model')
        system_version = q.get('system_version')
        application_version = q.get('application_version')
        enable_storage_optimizer = q.get('enable_storage_optimizer')
        ignore_file_names = q.get('ignore_file_names')
        return TdlibParameters(use_test_dc, database_directory, files_directory, use_file_database, use_chat_info_database, use_message_database, use_secret_chats, api_id, api_hash, system_language_code, device_model, system_version, application_version, enable_storage_optimizer, ignore_file_names)
