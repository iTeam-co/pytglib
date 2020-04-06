from pytglib.api.functions import *
from pytglib.api.types import *

"""
 !!! This file is not adapted to new TDLib version !!!
"""


class Function:
    def __init__(self, client):
        self.client = client
        self.send = client.send
        self.execute = client.execute

    def send_message(self, chat_id: int, text: str, reply_to_message_id=0, disable_notification=False,
                     from_background=False, scheduling_state=False,
                     markup=None, parse_mode=None, disable_web_page_preview=False, clear_draft=True):
        """
        Sends a message to a chat. The chat must be in the tdlib's database.
        If there is no chat in the DB, tdlib returns an error.
        Chat is being saved to the database when the client receives a message or when you call the `get_chats` method.

        Args:
            chat_id (:obj:`int`):
                Target chat
            text (:obj:`str`):
                Text to send
            reply_to_message_id (:obj:`int`):
                Identifier of the message to reply to or 0
            disable_notification (:obj:`bool`):
                Pass true to disable notification for the message
                Not supported in secret chats
            from_background (:obj:`bool`):
                Pass true if the message is sent from the background
            scheduling_state (:class:`pytglib.api.types.MessageSchedulingState`):
                Pass a MessageSchedulingState if you want message to be scheduled
            markup (:class:`pytglib.api.types.ReplyMarkup`):
                Markup for replying to the message; for bots only
            parse_mode (:obj:`str`):
                Text parse mode
                MarkDown, HTML or None
            disable_web_page_preview (:obj:`bool`):
                True, if rich web page previews for URLs in the message text should be disabled
            clear_draft (:obj:`bool`):
                True, if a chat message draft should be deleted

        Returns:
            AsyncResult
        """
        if parse_mode is not None:
            parse_mode = TextParseModeMarkdown(version=1) if parse_mode.lower() in ["md", "markdown"] \
                else TextParseModeHTML()
            msg_text = self.execute(ParseTextEntities(text, parse_mode))
        else:
            msg_text = FormattedText(text, [])
        data = SendMessage(chat_id, reply_to_message_id,
                           SendMessageOptions(disable_notification, from_background, scheduling_state), markup,
                           InputMessageText(msg_text, disable_web_page_preview, clear_draft))

        return self.send(data)

    def press_inline_button(self, chat_id: int, message_id: int, button_data: str):

        """
        Presses an Inline Button in the chat.

        Args:
            chat_id (:obj:`int`):
                Target chat
            message_id (:obj:`int`):
                Message which the button is attached to
            button_data (:obj:`str`):
                Button data

        Returns:
            AsyncResult
        """

        button = CallbackQueryPayloadData(data=button_data)
        data = GetCallbackQueryAnswer(chat_id, message_id, button)

        return self.send(data)

    def send_photo(self, chat_id: int, photo: str, caption="", reply_to_message_id=0, disable_notification=False,
                   from_background=False, scheduling_state=False, markup=None, parse_mode=None):
        """
        Sends a photo to a chat. The chat must be in the tdlib's database.
        If there is no chat in the DB, tdlib returns an error.
        Chat is being saved to the database when the client receives a message or when you call the `get_chats` method.

        Args:
            chat_id (:obj:`int`):
                Target chat
            photo (:obj:`str`):
                Path of photo to send
            caption (:obj:`str`):
                Caption of message to send
            reply_to_message_id (:obj:`int`):
                Identifier of the message to reply to or 0
            disable_notification (:obj:`bool`):
                Pass true to disable notification for the message
                Not supported in secret chats
            from_background (:obj:`bool`):
                Pass true if the message is sent from the background
            scheduling_state (:class:`pytglib.api.types.MessageSchedulingState`):
                Pass a MessageSchedulingState if you want message to be scheduled
            markup (:class:`pytglib.api.types.ReplyMarkup`):
                Markup for replying to the message; for bots only
            parse_mode (:obj:`str`):
                Text parse mode
                MarkDown, HTML or None

        Returns:
            AsyncResult
        """

        data = SendMessage(chat_id, options=SendMessageOptions(disable_notification, from_background, scheduling_state),
                           reply_markup=markup,
                           input_message_content=InputMessagePhoto(added_sticker_file_ids=[0],
                                                                   caption=FormattedText(caption, []), height=0,
                                                                   width=0, photo=InputFileLocal(photo),
                                                                   thumbnail=InputThumbnail(height=0, width=0,
                                                                                            thumbnail=InputFileLocal(
                                                                                                photo)), ttl=0),
                           reply_to_message_id=reply_to_message_id)

        return self.send(data)

    def get_chat(self, chat_id: int):
        """
        This is offline request, if there is no chat in your database it will not be found
        tdlib saves chat to the database when it receives a new message or when you call `get_chats` method.

        Args:
            chat_id (:obj:`int`):
                Target chat id

        Returns:
            AsyncResult
        """
        data = GetChat(chat_id)

        return self.send(data)

    def get_me(self):
        """
        Requests information of the current user (getMe method)

        Returns:
            AsyncResult
        """

        return self.send(GetMe())

    def get_chats(
            self, chat_list: ChatList, offset_order: int = 2 ** 63 - 1, offset_chat_id: int = 0, limit: int = 10000
    ):
        """
            Returns an ordered list of chats. Chats are sorted newest to oldest.
            Don't send the values and it'll return full chats.

            chat_list (:class:`pytglib.api.types.ChatList`):
                ChatListMain or ChatListArchive
            offset_order (:obj:`int`):
                Chat order to return chats from
            offset_chat_id (:obj:`int`):
                Chat identifier to return chats from
            limit (:obj:`int`):
                The maximum number of chats to be returned
                It is possible that fewer chats than the limit are returned even if the end of the list is not reached

            Returns:
                AsyncResult
        """
        return self.send(GetChats(chat_list, offset_order, offset_chat_id, limit))

    def get_chat_history(
            self,
            chat_id: int,
            limit: int = 1000,
            from_message_id: int = 0,
            offset: int = 0,
            only_local: bool = False,
    ):
        """
            Returns messages in a chat. The messages are returned in a reverse chronological order
             (i.e., in order of decreasing message_id).
            For optimal performance the number of returned messages is chosen by the library.
             This is an offline request if only_local is true

            Args:
                chat_id (:obj:`int`):
                    Chat identifier
                from_message_id (:obj:`int`):
                    Identifier of the message starting from which history must be fetched;
                     use 0 to get results from the last message
                offset (:obj:`int`):
                    Specify 0 to get results from exactly the from_message_id
                    or a negative offset to get the specified message and some newer messages
                limit (:obj:`int`):
                    The maximum number of messages to be returned; must be positive and can't be greater than 100
                    If the offset is negative,
                    the limit must be greater than -offsetFewer messages may be returned than specified by the limit,
                    Even if the end of the message history has not been reached
                only_local (:obj:`bool`):
                    If true, returns only messages that are available locally without sending network requests

            Returns:
                AsyncResult
        """
        return self.send(
            GetChatHistory(chat_id, limit=limit, from_message_id=from_message_id, offset=offset, only_local=only_local))

    def get_inline_query_results(self, bot_user_id, chat_id, query, offset, user_location=Location(0, 0)):
        """
        Sends an inline query to a bot and returns its results.
         Returns an error with code 502 if the bot fails to answer the query before the query timeout expires

        Args:
            bot_user_id (:obj:`int`):
                The identifier of the target bot
            chat_id (:obj:`int`):
                Identifier of the chat, where the query was sent
            query (:obj:`str`):
                Text of the query
            offset (:obj:`str`):
                Offset of the first entry to return
            user_location (:class:`pytglib.api.types.location`):
                Location of the user, only if needed

        Returns:
            AsyncResult
        """
        return self.send(GetInlineQueryResults(bot_user_id, chat_id, user_location, query, offset))

    def send_inline_query_result(self, chat_id, query_id, result_id, reply_to_message_id=0, disable_notification=False,
                                 from_background=False):
        """
        Sends the result of an inline query as a message. Returns the sent message. Always clears a chat draft message

        Args:
            chat_id (:obj:`int`):
                Target chat
            query_id (:obj:`int`):
                Identifier of the inline query
            result_id (:obj:`str`):
                Identifier of the inline result
            reply_to_message_id (:obj:`int`):
                Identifier of a message to reply to or 0
            disable_notification (:obj:`bool`):
                Pass true to disable notification for the messageNot supported in secret chats
            from_background (:obj:`bool`):
                Pass true if the message is sent from background

        Returns:
            AsyncResult
        """
        return self.send(SendInlineQueryResultMessage(chat_id, reply_to_message_id, disable_notification,
                                                      from_background, query_id, result_id))

    def send_chat_action(self, chat_id, action=ChatActionTyping()):
        """
            Sends a notification about user activity in a chat

            Args:
                chat_id (:obj:`int`):
                    Chat identifier
                action (:class:`pytglib.api.types.ChatAction`):
                    The action description (Default: Typing)

            Returns:
                AsyncResult
        """
        return self.send(SendChatAction(chat_id, action))

    def forward_messages(self, chat_id, from_chat_id, message_ids, disable_notification=False, from_background=False,
                         as_album=False):
        """
        Forwards previously sent messages.
         Returns the forwarded messages in the same order as the message identifiers passed in message_ids.
        If a message can't be forwarded, null will be returned instead of the message

        Args:
            chat_id (:obj:`int`):
                Identifier of the chat to which to forward messages
            from_chat_id (:obj:`int`):
                Identifier of the chat from which to forward messages
            message_ids (List of :obj:`int`):
                Identifiers of the messages to forward
            disable_notification (:obj:`bool`):
                Pass true to disable notification for the message,
                 doesn't work if messages are forwarded to a secret chat
            from_background (:obj:`bool`):
                Pass true if the message is sent from the background
            as_album (:obj:`bool`):
                True, if the messages should be grouped into an album after forwarding
                For this to work, no more than 10 messages may be forwarded,
                 and all of them must be photo or video messages

        Returns:
            AsyncResult
        """
        return self.send(
            ForwardMessages(chat_id, from_chat_id, message_ids, disable_notification, from_background, as_album))

    def delete_messages(self, chat_id, message_ids, revoke=True):
        """
            Deletes messages

            Args:
                chat_id (:obj:`int`):
                    Chat identifier
                message_ids (List of :obj:`int`):
                    Identifiers of the messages to be deleted
                revoke (:obj:`bool`):
                    Pass true to try to delete outgoing messages for all chat members (may fail if messages are too old)
                    Always true for supergroups, channels and secret chats

            Returns:
                AsyncResult
        """
        return self.send(DeleteMessages(chat_id, message_ids, revoke))

    def edit_message_text(self, chat_id, message_id, text, markup=None, parse_mode=None):
        """
            Edits the text of a message (or a text of a game message).
            Returns the edited message after the edit is completed on the server side

            Args:
                chat_id (:obj:`int`):
                    The chat the message belongs to
                message_id (:obj:`int`):
                    Identifier of the message
                text (:obj:`str`):
                    New message text
                markup (:class:`pytglib.api.types.ReplyMarkup`):
                    The new message reply markup; for bots only
                parse_mode (:obj:`str`):
                    Text parse mode.
                    Markdown, HTML or None

            Returns:
                AsyncResult
        """
        if parse_mode is not None:
            parse_mode = TextParseModeMarkdown(version=1) if parse_mode.lower() in ["md",
                                                                                    "markdown"] else TextParseModeHTML()
            msg_text = self.execute(ParseTextEntities(text, parse_mode))
        else:
            msg_text = FormattedText(text, [])
        return self.send(EditMessageText(chat_id, message_id, markup, msg_text))

    def send_document(self, chat_id: int, document: str, caption=None, reply_to_message_id=0,
                      disable_notification=False,
                      from_background=False,
                      markup=None, parse_mode=None):
        """
        Sends a document to a chat. The chat must be in the tdlib's database.
        If there is no chat in the DB, tdlib returns an error.
        Chat is being saved to the database when the client receives a message or when you call the `get_chats` method.

        Args:
            chat_id (:obj:`int`):
                Target chat
            document (:obj:`str`):
                Document path in system
            caption (:obj:`str`):
                Document caption
            reply_to_message_id (:obj:`int`):
                Identifier of the message to reply to or 0
            disable_notification (:obj:`bool`):
                Pass true to disable notification for the message
                Not supported in secret chats
            from_background (:obj:`bool`):
                Pass true if the message is sent from the background
            markup (:class:`pytglib.api.types.ReplyMarkup`):
                Markup for replying to the message; for bots only
            parse_mode (:obj:`str`):
                Caption parse mode
                MarkDown, HTML or None
        Returns:
            AsyncResult
        """
        if parse_mode is not None:
            parse_mode = TextParseModeMarkdown(version=1) if parse_mode.lower() in ["md",
                                                                                    "markdown"] else TextParseModeHTML()
            caption = self.execute(ParseTextEntities(caption, parse_mode))
        else:
            caption = FormattedText(caption, [])
        data = SendMessage(chat_id, reply_to_message_id, disable_notification, from_background, markup,
                           InputMessageDocument(InputFileLocal(document), None, caption))

        return self.send(data)

    def join_chat(self, invite_link):
        """
            Uses an invite link to add the current user to the chat if possible.
            The new member will not be added until the chat state has been synchronized with the server

            Args:
                invite_link (:obj:`str`):
                    Invite link to import.
                    Should begin with "https://t.me/joinchat/", "https://pytglib.me/joinchat/", or "https://pytglib.dog/joinchat/"

            Returns:
                AsyncResult
        """
        return self.send(JoinChatByInviteLink(invite_link))

    def check_chat_invite_link(self, invite_link):
        """
            Checks the validity of an invite link for a chat and returns information about the corresponding chat

            Args:
                invite_link (:obj:`str`):
                    Invite link to import.
                    Should begin with "https://t.me/joinchat/", "https://pytglib.me/joinchat/", or "https://pytglib.dog/joinchat/"

            Returns:
                    AsyncResult
        """
        return self.send(CheckChatInviteLink(invite_link))

    def leave_chat(self, chat_id):
        """
            Removes current user from chat members. Private and secret chats can't be left using this method

            Args:
                chat_id (:obj:`int`):
                    Chat identifier

            Returns:
                AsyncResult
        """
        return self.send(LeaveChat(chat_id))

    def get_chat_members(self, chat_id, offset=0, limit=200, filter=SupergroupMembersFilterRecent()):
        """
            Returns information about members or banned users in a supergroup or channel.
            Can be used only if SupergroupFullInfo.can_get_members == true;
            Additionally, administrator privileges may be required for some filters

            Args:
                chat_id (:obj:`int`):
                    Identifier of the supergroup or channel
                filter (:class:`pytglib.api.types.SupergroupMembersFilter`):
                    The type of users to return
                    By default, supergroupMembersRecent
                offset (:obj:`int`):
                    Number of users to skip
                limit (:obj:`int`):
                    The maximum number of users be returned; up to 200

            Returns:
                AsyncResult
        """
        return self.send(GetSupergroupMembers(chat_id, filter, offset, limit))

    def add_contact(self, phone_number, first_name, last_name, vcard="", user_id=0):
        """
            Adds new contact or edits existing contact; contact's user identifiers are ignored

            phone_number (:obj:`str`):
                Phone number of the user
            first_name (:obj:`str`):
               First name of the user; 1-255 characters in length
            last_name (:obj:`str`):
                Last name of the user
            vcard (:obj:`str`):
               Additional data about the user in a form of vCard; 0-2048 bytes in length
            user_id (:obj:`int`):
                Identifier of the user, if known; otherwise 0

            Returns:
                AsyncResult
        """
        return self.send(ImportContacts([Contact(phone_number, first_name, last_name, vcard, user_id)]))

    def view_messages(self, chat_id, latest_message_id):
        """
        Marks the incomming messages as "READ"

        Returns:
            AsyncResult
        """
        return self.send(ViewMessages(chat_id, [latest_message_id], True))

    def get_contacts(self):
        """
        Returns all user contacts

        Returns:
            AsyncResult
        """
        return self.send(GetContacts())
