

from ..utils import Object


class ChatStatisticsSupergroup(Object):
    """
    A detailed statistics about a supergroup chat

    Attributes:
        ID (:obj:`str`): ``ChatStatisticsSupergroup``

    Args:
        period (:class:`telegram.api.types.dateRange`):
            A period to which the statistics applies
        member_count (:class:`telegram.api.types.statisticalValue`):
            Number of members in the chat
        message_count (:class:`telegram.api.types.statisticalValue`):
            Number of messages sent to the chat
        viewer_count (:class:`telegram.api.types.statisticalValue`):
            Number of users who viewed messages in the chat
        sender_count (:class:`telegram.api.types.statisticalValue`):
            Number of users who sent messages to the chat
        member_count_graph (:class:`telegram.api.types.StatisticalGraph`):
            A graph containing number of members in the chat
        join_graph (:class:`telegram.api.types.StatisticalGraph`):
            A graph containing number of members joined and left the chat
        join_by_source_graph (:class:`telegram.api.types.StatisticalGraph`):
            A graph containing number of new member joins per source
        language_graph (:class:`telegram.api.types.StatisticalGraph`):
            A graph containing distribution of active users per language
        message_content_graph (:class:`telegram.api.types.StatisticalGraph`):
            A graph containing distribution of sent messages by content type
        action_graph (:class:`telegram.api.types.StatisticalGraph`):
            A graph containing number of different actions in the chat
        day_graph (:class:`telegram.api.types.StatisticalGraph`):
            A graph containing distribution of message views per hour
        week_graph (:class:`telegram.api.types.StatisticalGraph`):
            A graph containing distribution of message views per day of week
        top_senders (List of :class:`telegram.api.types.chatStatisticsMessageSenderInfo`):
            List of users sent most messages in the last week
        top_administrators (List of :class:`telegram.api.types.chatStatisticsAdministratorActionsInfo`):
            List of most active administrators in the last week
        top_inviters (List of :class:`telegram.api.types.chatStatisticsInviterInfo`):
            List of most active inviters of new members in the last week

    Returns:
        ChatStatistics

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatStatisticsSupergroup"

    def __init__(self, period, member_count, message_count, viewer_count, sender_count, member_count_graph, join_graph, join_by_source_graph, language_graph, message_content_graph, action_graph, day_graph, week_graph, top_senders, top_administrators, top_inviters, **kwargs):
        
        self.period = period  # DateRange
        self.member_count = member_count  # StatisticalValue
        self.message_count = message_count  # StatisticalValue
        self.viewer_count = viewer_count  # StatisticalValue
        self.sender_count = sender_count  # StatisticalValue
        self.member_count_graph = member_count_graph  # StatisticalGraph
        self.join_graph = join_graph  # StatisticalGraph
        self.join_by_source_graph = join_by_source_graph  # StatisticalGraph
        self.language_graph = language_graph  # StatisticalGraph
        self.message_content_graph = message_content_graph  # StatisticalGraph
        self.action_graph = action_graph  # StatisticalGraph
        self.day_graph = day_graph  # StatisticalGraph
        self.week_graph = week_graph  # StatisticalGraph
        self.top_senders = top_senders  # list of chatStatisticsMessageSenderInfo
        self.top_administrators = top_administrators  # list of chatStatisticsAdministratorActionsInfo
        self.top_inviters = top_inviters  # list of chatStatisticsInviterInfo

    @staticmethod
    def read(q: dict, *args) -> "ChatStatisticsSupergroup":
        period = Object.read(q.get('period'))
        member_count = Object.read(q.get('member_count'))
        message_count = Object.read(q.get('message_count'))
        viewer_count = Object.read(q.get('viewer_count'))
        sender_count = Object.read(q.get('sender_count'))
        member_count_graph = Object.read(q.get('member_count_graph'))
        join_graph = Object.read(q.get('join_graph'))
        join_by_source_graph = Object.read(q.get('join_by_source_graph'))
        language_graph = Object.read(q.get('language_graph'))
        message_content_graph = Object.read(q.get('message_content_graph'))
        action_graph = Object.read(q.get('action_graph'))
        day_graph = Object.read(q.get('day_graph'))
        week_graph = Object.read(q.get('week_graph'))
        top_senders = [Object.read(i) for i in q.get('top_senders', [])]
        top_administrators = [Object.read(i) for i in q.get('top_administrators', [])]
        top_inviters = [Object.read(i) for i in q.get('top_inviters', [])]
        return ChatStatisticsSupergroup(period, member_count, message_count, viewer_count, sender_count, member_count_graph, join_graph, join_by_source_graph, language_graph, message_content_graph, action_graph, day_graph, week_graph, top_senders, top_administrators, top_inviters)
