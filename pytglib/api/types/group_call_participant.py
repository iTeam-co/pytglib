

from ..utils import Object


class GroupCallParticipant(Object):
    """
    Represents a group call participant

    Attributes:
        ID (:obj:`str`): ``GroupCallParticipant``

    Args:
        participant_id (:class:`telegram.api.types.MessageSender`):
            Identifier of the group call participant
        audio_source_id (:obj:`int`):
            User's audio channel synchronization source identifier
        screen_sharing_audio_source_id (:obj:`int`):
            User's screen sharing audio channel synchronization source identifier
        video_info (:class:`telegram.api.types.groupCallParticipantVideoInfo`):
            Information about user's video channel; may be null if there is no active video
        screen_sharing_video_info (:class:`telegram.api.types.groupCallParticipantVideoInfo`):
            Information about user's screen sharing video channel; may be null if there is no active screen sharing video
        bio (:obj:`str`):
            The participant user's bio or the participant chat's description
        is_current_user (:obj:`bool`):
            True, if the participant is the current user
        is_speaking (:obj:`bool`):
            True, if the participant is speaking as set by setGroupCallParticipantIsSpeaking
        is_hand_raised (:obj:`bool`):
            True, if the participant hand is raised
        can_be_muted_for_all_users (:obj:`bool`):
            True, if the current user can mute the participant for all other group call participants
        can_be_unmuted_for_all_users (:obj:`bool`):
            True, if the current user can allow the participant to unmute themselves or unmute the participant (if the participant is the current user)
        can_be_muted_for_current_user (:obj:`bool`):
            True, if the current user can mute the participant only for self
        can_be_unmuted_for_current_user (:obj:`bool`):
            True, if the current user can unmute the participant for self
        is_muted_for_all_users (:obj:`bool`):
            True, if the participant is muted for all users
        is_muted_for_current_user (:obj:`bool`):
            True, if the participant is muted for the current user
        can_unmute_self (:obj:`bool`):
            True, if the participant is muted for all users, but can unmute themselves
        volume_level (:obj:`int`):
            Participant's volume level; 1-20000 in hundreds of percents
        order (:obj:`str`):
            User's order in the group call participant listOrders must be compared lexicographicallyThe bigger is order, the higher is user in the listIf order is empty, the user must be removed from the participant list

    Returns:
        GroupCallParticipant

    Raises:
        :class:`telegram.Error`
    """
    ID = "groupCallParticipant"

    def __init__(self, participant_id, audio_source_id, screen_sharing_audio_source_id, video_info, screen_sharing_video_info, bio, is_current_user, is_speaking, is_hand_raised, can_be_muted_for_all_users, can_be_unmuted_for_all_users, can_be_muted_for_current_user, can_be_unmuted_for_current_user, is_muted_for_all_users, is_muted_for_current_user, can_unmute_self, volume_level, order, **kwargs):
        
        self.participant_id = participant_id  # MessageSender
        self.audio_source_id = audio_source_id  # int
        self.screen_sharing_audio_source_id = screen_sharing_audio_source_id  # int
        self.video_info = video_info  # GroupCallParticipantVideoInfo
        self.screen_sharing_video_info = screen_sharing_video_info  # GroupCallParticipantVideoInfo
        self.bio = bio  # str
        self.is_current_user = is_current_user  # bool
        self.is_speaking = is_speaking  # bool
        self.is_hand_raised = is_hand_raised  # bool
        self.can_be_muted_for_all_users = can_be_muted_for_all_users  # bool
        self.can_be_unmuted_for_all_users = can_be_unmuted_for_all_users  # bool
        self.can_be_muted_for_current_user = can_be_muted_for_current_user  # bool
        self.can_be_unmuted_for_current_user = can_be_unmuted_for_current_user  # bool
        self.is_muted_for_all_users = is_muted_for_all_users  # bool
        self.is_muted_for_current_user = is_muted_for_current_user  # bool
        self.can_unmute_self = can_unmute_self  # bool
        self.volume_level = volume_level  # int
        self.order = order  # str

    @staticmethod
    def read(q: dict, *args) -> "GroupCallParticipant":
        participant_id = Object.read(q.get('participant_id'))
        audio_source_id = q.get('audio_source_id')
        screen_sharing_audio_source_id = q.get('screen_sharing_audio_source_id')
        video_info = Object.read(q.get('video_info'))
        screen_sharing_video_info = Object.read(q.get('screen_sharing_video_info'))
        bio = q.get('bio')
        is_current_user = q.get('is_current_user')
        is_speaking = q.get('is_speaking')
        is_hand_raised = q.get('is_hand_raised')
        can_be_muted_for_all_users = q.get('can_be_muted_for_all_users')
        can_be_unmuted_for_all_users = q.get('can_be_unmuted_for_all_users')
        can_be_muted_for_current_user = q.get('can_be_muted_for_current_user')
        can_be_unmuted_for_current_user = q.get('can_be_unmuted_for_current_user')
        is_muted_for_all_users = q.get('is_muted_for_all_users')
        is_muted_for_current_user = q.get('is_muted_for_current_user')
        can_unmute_self = q.get('can_unmute_self')
        volume_level = q.get('volume_level')
        order = q.get('order')
        return GroupCallParticipant(participant_id, audio_source_id, screen_sharing_audio_source_id, video_info, screen_sharing_video_info, bio, is_current_user, is_speaking, is_hand_raised, can_be_muted_for_all_users, can_be_unmuted_for_all_users, can_be_muted_for_current_user, can_be_unmuted_for_current_user, is_muted_for_all_users, is_muted_for_current_user, can_unmute_self, volume_level, order)
