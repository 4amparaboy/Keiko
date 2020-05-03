import requests
import datetime
from telegram import Update, Bot, ParseMode
from telegram.ext import run_async
import wikipedia

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

@run_async
def wiki(bot: Bot, update: Update):
    message = update.effective_message
    search_str = message.text.split(' ', 1)
    if len(text) == 1:
        searchterm = 'Usage: /wiki [search terms]'
        message.reply_text(searchterm, parse_mode=ParseMode.MARKDOWN)
    results = wikipedia.search(search_str)
    if not results:
        error = 'There were no results matching the query.'
        message.reply_text(error, parse_mode=ParseMode.MARKDOWN)
    else:
        summary = wikipedia.summary(search_str)
        reply_text = (summary)
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


__help__ = """
 - /wiki oogabooga
 - /wikipedia oogabooga
"""

WIKI_HANDLER = DisableAbleCommandHandler(["wiki", "wikipedia"], wiki)

dispatcher.add_handler(WIKI_HANDLER)

__mod_name__ = "Wikipedia"