

from ..utils import Object


class MessageInteractionInfo(Object):
    """
    Contains information about interactions with a message

    Attributes:
        ID (:obj:`str`): ``MessageInteractionInfo``

    Args:
        view_count (:obj:`int`):
            Number of times the message was viewed
        forward_count (:obj:`int`):
            Number of times the message was forwarded
        reply_info (:class:`telegram.api.types.messageReplyInfo`):
            Information about direct or indirect replies to the message; may be nullCurrently, available only in channels with a discussion supergroup and discussion supergroups for messages, which are not replies itself
        reactions (List of :class:`telegram.api.types.messageReaction`):
            The list of reactions added to the message

    Returns:
        MessageInteractionInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageInteractionInfo"

    def __init__(self, view_count, forward_count, reply_info, reactions, **kwargs):
        
        self.view_count = view_count  # int
        self.forward_count = forward_count  # int
        self.reply_info = reply_info  # MessageReplyInfo
        self.reactions = reactions  # list of messageReaction

    @staticmethod
    def read(q: dict, *args) -> "MessageInteractionInfo":
        view_count = q.get('view_count')
        forward_count = q.get('forward_count')
        reply_info = Object.read(q.get('reply_info'))
        reactions = [Object.read(i) for i in q.get('reactions', [])]
        return MessageInteractionInfo(view_count, forward_count, reply_info, reactions)
