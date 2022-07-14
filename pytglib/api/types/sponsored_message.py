

from ..utils import Object


class SponsoredMessage(Object):
    """
    Describes a sponsored message

    Attributes:
        ID (:obj:`str`): ``SponsoredMessage``

    Args:
        message_id (:obj:`int`):
            Message identifier; unique for the chat to which the sponsored message belongs among both ordinary and sponsored messages
        is_recommended (:obj:`bool`):
            True, if the message needs to be labeled as "recommended" instead of "sponsored"
        sponsor_chat_id (:obj:`int`):
            Sponsor chat identifier; 0 if the sponsor chat is accessible through an invite link
        sponsor_chat_info (:class:`telegram.api.types.chatInviteLinkInfo`):
            Information about the sponsor chat; may be null unless sponsor_chat_id == 0
        link (:class:`telegram.api.types.InternalLinkType`):
            An internal link to be opened when the sponsored message is clicked; may be null if the sponsor chat needs to be opened instead
        content (:class:`telegram.api.types.MessageContent`):
            Content of the messageCurrently, can be only of the type messageText

    Returns:
        SponsoredMessage

    Raises:
        :class:`telegram.Error`
    """
    ID = "sponsoredMessage"

    def __init__(self, message_id, is_recommended, sponsor_chat_id, sponsor_chat_info, link, content, **kwargs):
        
        self.message_id = message_id  # int
        self.is_recommended = is_recommended  # bool
        self.sponsor_chat_id = sponsor_chat_id  # int
        self.sponsor_chat_info = sponsor_chat_info  # ChatInviteLinkInfo
        self.link = link  # InternalLinkType
        self.content = content  # MessageContent

    @staticmethod
    def read(q: dict, *args) -> "SponsoredMessage":
        message_id = q.get('message_id')
        is_recommended = q.get('is_recommended')
        sponsor_chat_id = q.get('sponsor_chat_id')
        sponsor_chat_info = Object.read(q.get('sponsor_chat_info'))
        link = Object.read(q.get('link'))
        content = Object.read(q.get('content'))
        return SponsoredMessage(message_id, is_recommended, sponsor_chat_id, sponsor_chat_info, link, content)
