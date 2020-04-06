

from ..utils import Object


class AutoDownloadSettings(Object):
    """
    Contains auto-download settings

    Attributes:
        ID (:obj:`str`): ``AutoDownloadSettings``

    Args:
        is_auto_download_enabled (:obj:`bool`):
            True, if the auto-download is enabled
        max_photo_file_size (:obj:`int`):
            The maximum size of a photo file to be auto-downloaded
        max_video_file_size (:obj:`int`):
            The maximum size of a video file to be auto-downloaded
        max_other_file_size (:obj:`int`):
            The maximum size of other file types to be auto-downloaded
        video_upload_bitrate (:obj:`int`):
            The maximum suggested bitrate for uploaded videos
        preload_large_videos (:obj:`bool`):
            True, if the beginning of videos needs to be preloaded for instant playback
        preload_next_audio (:obj:`bool`):
            True, if the next audio track needs to be preloaded while the user is listening to an audio file
        use_less_data_for_calls (:obj:`bool`):
            True, if "use less data for calls" option needs to be enabled

    Returns:
        AutoDownloadSettings

    Raises:
        :class:`telegram.Error`
    """
    ID = "autoDownloadSettings"

    def __init__(self, is_auto_download_enabled, max_photo_file_size, max_video_file_size, max_other_file_size, video_upload_bitrate, preload_large_videos, preload_next_audio, use_less_data_for_calls, **kwargs):
        
        self.is_auto_download_enabled = is_auto_download_enabled  # bool
        self.max_photo_file_size = max_photo_file_size  # int
        self.max_video_file_size = max_video_file_size  # int
        self.max_other_file_size = max_other_file_size  # int
        self.video_upload_bitrate = video_upload_bitrate  # int
        self.preload_large_videos = preload_large_videos  # bool
        self.preload_next_audio = preload_next_audio  # bool
        self.use_less_data_for_calls = use_less_data_for_calls  # bool

    @staticmethod
    def read(q: dict, *args) -> "AutoDownloadSettings":
        is_auto_download_enabled = q.get('is_auto_download_enabled')
        max_photo_file_size = q.get('max_photo_file_size')
        max_video_file_size = q.get('max_video_file_size')
        max_other_file_size = q.get('max_other_file_size')
        video_upload_bitrate = q.get('video_upload_bitrate')
        preload_large_videos = q.get('preload_large_videos')
        preload_next_audio = q.get('preload_next_audio')
        use_less_data_for_calls = q.get('use_less_data_for_calls')
        return AutoDownloadSettings(is_auto_download_enabled, max_photo_file_size, max_video_file_size, max_other_file_size, video_upload_bitrate, preload_large_videos, preload_next_audio, use_less_data_for_calls)
