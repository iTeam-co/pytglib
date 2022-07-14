

from ..utils import Object


class GroupCall(Object):
    """
    Describes a group call

    Attributes:
        ID (:obj:`str`): ``GroupCall``

    Args:
        id (:obj:`int`):
            Group call identifier
        title (:obj:`str`):
            Group call title
        scheduled_start_date (:obj:`int`):
            Point in time (Unix timestamp) when the group call is supposed to be started by an administrator; 0 if it is already active or was ended
        enabled_start_notification (:obj:`bool`):
            True, if the group call is scheduled and the current user will receive a notification when the group call will start
        is_active (:obj:`bool`):
            True, if the call is active
        is_rtmp_stream (:obj:`bool`):
            True, if the chat is an RTMP stream instead of an ordinary video chat
        is_joined (:obj:`bool`):
            True, if the call is joined
        need_rejoin (:obj:`bool`):
            True, if user was kicked from the call because of network loss and the call needs to be rejoined
        can_be_managed (:obj:`bool`):
            True, if the current user can manage the group call
        participant_count (:obj:`int`):
            Number of participants in the group call
        has_hidden_listeners (:obj:`bool`):
            True, if group call participants, which are muted, aren't returned in participant list
        loaded_all_participants (:obj:`bool`):
            True, if all group call participants are loaded
        recent_speakers (List of :class:`telegram.api.types.groupCallRecentSpeaker`):
            At most 3 recently speaking users in the group call
        is_my_video_enabled (:obj:`bool`):
            True, if the current user's video is enabled
        is_my_video_paused (:obj:`bool`):
            True, if the current user's video is paused
        can_enable_video (:obj:`bool`):
            True, if the current user can broadcast video or share screen
        mute_new_participants (:obj:`bool`):
            True, if only group call administrators can unmute new participants
        can_toggle_mute_new_participants (:obj:`bool`):
            True, if the current user can enable or disable mute_new_participants setting
        record_duration (:obj:`int`):
            Duration of the ongoing group call recording, in seconds; 0 if noneAn updateGroupCall update is not triggered when value of this field changes, but the same recording goes on
        is_video_recorded (:obj:`bool`):
            True, if a video file is being recorded for the call
        duration (:obj:`int`):
            Call duration, in seconds; for ended calls only

    Returns:
        GroupCall

    Raises:
        :class:`telegram.Error`
    """
    ID = "groupCall"

    def __init__(self, id, title, scheduled_start_date, enabled_start_notification, is_active, is_rtmp_stream, is_joined, need_rejoin, can_be_managed, participant_count, has_hidden_listeners, loaded_all_participants, recent_speakers, is_my_video_enabled, is_my_video_paused, can_enable_video, mute_new_participants, can_toggle_mute_new_participants, record_duration, is_video_recorded, duration, **kwargs):
        
        self.id = id  # int
        self.title = title  # str
        self.scheduled_start_date = scheduled_start_date  # int
        self.enabled_start_notification = enabled_start_notification  # bool
        self.is_active = is_active  # bool
        self.is_rtmp_stream = is_rtmp_stream  # bool
        self.is_joined = is_joined  # bool
        self.need_rejoin = need_rejoin  # bool
        self.can_be_managed = can_be_managed  # bool
        self.participant_count = participant_count  # int
        self.has_hidden_listeners = has_hidden_listeners  # bool
        self.loaded_all_participants = loaded_all_participants  # bool
        self.recent_speakers = recent_speakers  # list of groupCallRecentSpeaker
        self.is_my_video_enabled = is_my_video_enabled  # bool
        self.is_my_video_paused = is_my_video_paused  # bool
        self.can_enable_video = can_enable_video  # bool
        self.mute_new_participants = mute_new_participants  # bool
        self.can_toggle_mute_new_participants = can_toggle_mute_new_participants  # bool
        self.record_duration = record_duration  # int
        self.is_video_recorded = is_video_recorded  # bool
        self.duration = duration  # int

    @staticmethod
    def read(q: dict, *args) -> "GroupCall":
        id = q.get('id')
        title = q.get('title')
        scheduled_start_date = q.get('scheduled_start_date')
        enabled_start_notification = q.get('enabled_start_notification')
        is_active = q.get('is_active')
        is_rtmp_stream = q.get('is_rtmp_stream')
        is_joined = q.get('is_joined')
        need_rejoin = q.get('need_rejoin')
        can_be_managed = q.get('can_be_managed')
        participant_count = q.get('participant_count')
        has_hidden_listeners = q.get('has_hidden_listeners')
        loaded_all_participants = q.get('loaded_all_participants')
        recent_speakers = [Object.read(i) for i in q.get('recent_speakers', [])]
        is_my_video_enabled = q.get('is_my_video_enabled')
        is_my_video_paused = q.get('is_my_video_paused')
        can_enable_video = q.get('can_enable_video')
        mute_new_participants = q.get('mute_new_participants')
        can_toggle_mute_new_participants = q.get('can_toggle_mute_new_participants')
        record_duration = q.get('record_duration')
        is_video_recorded = q.get('is_video_recorded')
        duration = q.get('duration')
        return GroupCall(id, title, scheduled_start_date, enabled_start_notification, is_active, is_rtmp_stream, is_joined, need_rejoin, can_be_managed, participant_count, has_hidden_listeners, loaded_all_participants, recent_speakers, is_my_video_enabled, is_my_video_paused, can_enable_video, mute_new_participants, can_toggle_mute_new_participants, record_duration, is_video_recorded, duration)
