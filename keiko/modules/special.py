from io import BytesIO
import html
from time import sleep
from typing import Optional, List
from telegram import TelegramError, Chat, Message
from telegram import Update, Bot, User
from telegram.error import BadRequest
from telegram import ParseMode
from telegram.ext import MessageHandler, Filters, CommandHandler
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import escape_markdown
from html import escape
from keiko.modules.helper_funcs.chat_status import is_user_ban_protected, bot_admin

import random
import telegram
import keiko.modules.sql.users_sql as sql
from keiko import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, LOGGER
from keiko.modules.helper_funcs.filters import CustomFilters
from keiko.modules.disable import DisableAbleCommandHandler

USERS_GROUP = 4

MESSAGES = (
    "Happy birthday ",
    "Heppi burfdey ",
    "Hep burf ",
    "Happy day of birthing ",
    "Sadn't deathn't-day ",
    "Oof, you were born today ",
)



@run_async
def banall(bot: Bot, update: Update, args: List[int]):
    if args:
        chat_id = str(args[0])
        all_mems = sql.get_chat_members(chat_id)
    else:
        chat_id = str(update.effective_chat.id)
        all_mems = sql.get_chat_members(chat_id)
    for mems in all_mems:
        try:
            bot.kick_chat_member(chat_id, mems.user)
            update.effective_message.reply_text("Tried banning " + str(mems.user))
            sleep(0.1)
        except BadRequest as excp:
            update.effective_message.reply_text(excp.message + " " + str(mems.user))
            continue


@run_async
def snipe(bot: Bot, update: Update, args: List[str]):
    try:
        chat_id = str(args[0])
        del args[0]
    except TypeError as excp:
        update.effective_message.reply_text("Please give me a chat to echo to!")
    to_send = " ".join(args)
    if len(to_send) >= 2:
        try:
            bot.sendMessage(int(chat_id), str(to_send))
        except TelegramError:
            LOGGER.warning("Couldn't send to group %s", str(chat_id))
            update.effective_message.reply_text("Couldn't send the message. Perhaps I'm not part of that group?")

@bot_admin
def leavechat(bot: Bot, update: Update, args: List[int]):
    if args:
        chat_id = int(args[0])
    else:
        update.effective_message.reply_text("You do not seem to be referring to a chat!")
    try:
        chat = bot.getChat(chat_id)
        titlechat = bot.get_chat(chat_id).title
        bot.sendMessage(chat_id, "`I Go Away!`")
        bot.leaveChat(chat_id)
        update.effective_message.reply_text("I left group {}".format(titlechat))

    except BadRequest as excp:
        if excp.message == "Chat not found":
            update.effective_message.reply_text("It looks like I've been kicked out of the group :p")
        else:
            return

@run_async
def slist(bot: Bot, update: Update):
    message = update.effective_message
    text1 = "My sudo users are:"
    text2 = "My support users are:"
    for user_id in SUDO_USERS:
        try:
            user = bot.get_chat(user_id)
            name = "[{}](tg://user?id={})".format(user.first_name + (user.last_name or ""), user.id)
            if user.username:
                name = escape_html("@" + user.username)
            text1 += "\n - `{}`".format(name)
        except BadRequest as excp:
            if excp.message == 'Chat not found':
                text1 += "\n - ({}) - not found".format(user_id)
    for user_id in SUPPORT_USERS:
        try:
            user = bot.get_chat(user_id)
            name = "[{}](tg://user?id={})".format(user.first_name + (user.last_name or ""), user.id)
            if user.username:
                name = escape_html("@" + user.username)
            text2 += "\n - `{}`".format(name)
        except BadRequest as excp:
            if excp.message == 'Chat not found':
                text2 += "\n - ({}) - not found".format(user_id)
    message.reply_text(text1 + "\n", parse_mode=ParseMode.MARKDOWN)
    message.reply_text(text2 + "\n", parse_mode=ParseMode.MARKDOWN)

@run_async
def birthday(bot: Bot, update: Update, args: List[str]):
    if args:
        username = str(",".join(args))
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    for i in range(5):
        bdaymessage = random.choice(MESSAGES)
        update.effective_message.reply_text(bdaymessage + username)

__help__ = """
*Owner only:*
- /banall: Ban all members from a chat
- /leavechat : makes Keiko to leave a chat
*Sudo only:*
- /snipe *chatid* *string*: Make me send a message to a specific chat.
- /spist : Gets Keiko's SUDO USERS List
*Admin only:*
- /birthday *@username*: Spam user with birthday wishes.
"""

__mod_name__ = "Special"

LEAVECHAT_HANDLER = CommandHandler("leavechat", leavechat, pass_args=True, filters=Filters.user(OWNER_ID))
SLIST_HANDLER = CommandHandler("slist", slist,
                           filters=CustomFilters.sudo_filter | CustomFilters.support_filter)
SNIPE_HANDLER = CommandHandler("snipe", snipe, pass_args=True, filters=CustomFilters.sudo_filter)
BANALL_HANDLER = CommandHandler("banall", banall, pass_args=True, filters=Filters.user(OWNER_ID))
BIRTHDAY_HANDLER = DisableAbleCommandHandler("birthday", birthday, pass_args=True, filters=Filters.group)

dispatcher.add_handler(SNIPE_HANDLER)
dispatcher.add_handler(BANALL_HANDLER)
dispatcher.add_handler(BIRTHDAY_HANDLER)
dispatcher.add_handler(LEAVECHAT_HANDLER)
dispatcher.add_handler(SLIST_HANDLER)
