

from ..utils import Object


class ChatStatistics(Object):
    """
    A detailed statistics about a chat

    Attributes:
        ID (:obj:`str`): ``ChatStatistics``

    Args:
        period (:class:`telegram.api.types.dateRange`):
            A period to which the statistics applies
        member_count (:class:`telegram.api.types.statisticsValue`):
            Number of members in the chat
        mean_view_count (:class:`telegram.api.types.statisticsValue`):
            Mean number of times the recently sent messages was viewed
        mean_share_count (:class:`telegram.api.types.statisticsValue`):
            Mean number of times the recently sent messages was shared
        enabled_notifications_percentage (:obj:`float`):
            A percentage of users with enabled notifications for the chat
        member_count_graph (:class:`telegram.api.types.StatisticsGraph`):
            A graph containing number of members in the chat
        join_graph (:class:`telegram.api.types.StatisticsGraph`):
            A graph containing number of members joined and left the chat
        mute_graph (:class:`telegram.api.types.StatisticsGraph`):
            A graph containing number of members muted and unmuted the chat
        view_count_by_hour_graph (:class:`telegram.api.types.StatisticsGraph`):
            A graph containing number of message views in a given hour in the last two weeks
        view_count_by_source_graph (:class:`telegram.api.types.StatisticsGraph`):
            A graph containing number of message views per source
        join_by_source_graph (:class:`telegram.api.types.StatisticsGraph`):
            A graph containing number of new member joins per source
        language_graph (:class:`telegram.api.types.StatisticsGraph`):
            A graph containing number of users viewed chat messages per language
        message_interaction_graph (:class:`telegram.api.types.StatisticsGraph`):
            A graph containing number of chat message views and shares
        instant_view_interaction_graph (:class:`telegram.api.types.StatisticsGraph`):
            A graph containing number of views of associated with the chat instant views
        recent_message_interactions (List of :class:`telegram.api.types.chatStatisticsMessageInteractionCounters`):
            Detailed statistics about number of views and shares of recently sent messages

    Returns:
        ChatStatistics

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatStatistics"

    def __init__(self, period, member_count, mean_view_count, mean_share_count, enabled_notifications_percentage, member_count_graph, join_graph, mute_graph, view_count_by_hour_graph, view_count_by_source_graph, join_by_source_graph, language_graph, message_interaction_graph, instant_view_interaction_graph, recent_message_interactions, **kwargs):
        
        self.period = period  # DateRange
        self.member_count = member_count  # StatisticsValue
        self.mean_view_count = mean_view_count  # StatisticsValue
        self.mean_share_count = mean_share_count  # StatisticsValue
        self.enabled_notifications_percentage = enabled_notifications_percentage  # float
        self.member_count_graph = member_count_graph  # StatisticsGraph
        self.join_graph = join_graph  # StatisticsGraph
        self.mute_graph = mute_graph  # StatisticsGraph
        self.view_count_by_hour_graph = view_count_by_hour_graph  # StatisticsGraph
        self.view_count_by_source_graph = view_count_by_source_graph  # StatisticsGraph
        self.join_by_source_graph = join_by_source_graph  # StatisticsGraph
        self.language_graph = language_graph  # StatisticsGraph
        self.message_interaction_graph = message_interaction_graph  # StatisticsGraph
        self.instant_view_interaction_graph = instant_view_interaction_graph  # StatisticsGraph
        self.recent_message_interactions = recent_message_interactions  # list of chatStatisticsMessageInteractionCounters

    @staticmethod
    def read(q: dict, *args) -> "ChatStatistics":
        period = Object.read(q.get('period'))
        member_count = Object.read(q.get('member_count'))
        mean_view_count = Object.read(q.get('mean_view_count'))
        mean_share_count = Object.read(q.get('mean_share_count'))
        enabled_notifications_percentage = q.get('enabled_notifications_percentage')
        member_count_graph = Object.read(q.get('member_count_graph'))
        join_graph = Object.read(q.get('join_graph'))
        mute_graph = Object.read(q.get('mute_graph'))
        view_count_by_hour_graph = Object.read(q.get('view_count_by_hour_graph'))
        view_count_by_source_graph = Object.read(q.get('view_count_by_source_graph'))
        join_by_source_graph = Object.read(q.get('join_by_source_graph'))
        language_graph = Object.read(q.get('language_graph'))
        message_interaction_graph = Object.read(q.get('message_interaction_graph'))
        instant_view_interaction_graph = Object.read(q.get('instant_view_interaction_graph'))
        recent_message_interactions = [Object.read(i) for i in q.get('recent_message_interactions', [])]
        return ChatStatistics(period, member_count, mean_view_count, mean_share_count, enabled_notifications_percentage, member_count_graph, join_graph, mute_graph, view_count_by_hour_graph, view_count_by_source_graph, join_by_source_graph, language_graph, message_interaction_graph, instant_view_interaction_graph, recent_message_interactions)
