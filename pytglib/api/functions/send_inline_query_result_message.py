

from ..utils import Object


class SendInlineQueryResultMessage(Object):
    """
    Sends the result of an inline query as a message. Returns the sent message. Always clears a chat draft message 

    Attributes:
        ID (:obj:`str`): ``SendInlineQueryResultMessage``

    Args:
        chat_id (:obj:`int`):
            Target chat 
        reply_to_message_id (:obj:`int`):
            Identifier of a message to reply to or 0
        disable_notification (:obj:`bool`):
            Pass true to disable notification for the messageNot supported in secret chats 
        from_background (:obj:`bool`):
            Pass true if the message is sent from background
        query_id (:obj:`int`):
            Identifier of the inline query 
        result_id (:obj:`str`):
            Identifier of the inline result
        hide_via_bot (:obj:`bool`):
            If true, there will be no mention of a bot, via which the message is sentCan be used only for bots GetOption("animation_search_bot_username"), GetOption("photo_search_bot_username") and GetOption("venue_search_bot_username")

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendInlineQueryResultMessage"

    def __init__(self, chat_id, reply_to_message_id, disable_notification, from_background, query_id, result_id, hide_via_bot, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.reply_to_message_id = reply_to_message_id  # int
        self.disable_notification = disable_notification  # bool
        self.from_background = from_background  # bool
        self.query_id = query_id  # int
        self.result_id = result_id  # str
        self.hide_via_bot = hide_via_bot  # bool

    @staticmethod
    def read(q: dict, *args) -> "SendInlineQueryResultMessage":
        chat_id = q.get('chat_id')
        reply_to_message_id = q.get('reply_to_message_id')
        disable_notification = q.get('disable_notification')
        from_background = q.get('from_background')
        query_id = q.get('query_id')
        result_id = q.get('result_id')
        hide_via_bot = q.get('hide_via_bot')
        return SendInlineQueryResultMessage(chat_id, reply_to_message_id, disable_notification, from_background, query_id, result_id, hide_via_bot)
