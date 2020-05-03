

from telegram import Update, Bot, ParseMode
from time import sleep
from telegram.ext import run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.chat_status import is_user_admin, user_admin


@run_async
def police(bot: Bot, update: Update):
    message = update.effective_message.reply_text('/police')
    

    animation_chars = [
                "🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵",

                "🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴",

                "🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵",

                "🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴",

                "🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵",    

                "🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴",

                "🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵",

                "🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴",

                "*Police iz Here*"
    ]
    for i in animation_chars:
        message.edit_text(i)
        sleep(0.5)

@run_async
def moon(bot: Bot, update: Update):
    message = update.effective_message.reply_text('/moon')
    

    animation_chars = [
                "🌗🌘🌑🌒🌓🌔🌕🌖",

                "🌘🌑🌒🌓🌔🌕🌖🌗",

                "🌑🌒🌓🌔🌕🌖🌗🌘",

                "🌒🌓🌔🌕🌖🌗🌘🌑",

                "🌓🌔🌕🌖🌗🌘🌑🌒",    

                "🌔🌕🌖🌗🌘🌑🌒🌓",

                "🌕🌖🌗🌘🌑🌒🌓🌔",

                "🌖🌗🌘🌑🌒🌓🌔🌕",

                "🌗🌘🌑🌒🌓🌔🌕🌖",

                "🌘🌑🌒🌓🌔🌕🌖🌗",

                "🌑🌒🌓🌔🌕🌖🌗🌘",

                "🌒🌓🌔🌕🌖🌗🌘🌑",

                "🌓🌔🌕🌖🌗🌘🌑🌒",    

                "🌔🌕🌖🌗🌘🌑🌒🌓",

                "🌕🌖🌗🌘🌑🌒🌓🌔",

                "🌖🌗🌘🌑🌒🌓🌔🌕",

    ]
    for i in animation_chars:
        message.edit_text(i)
        sleep(0.2)


__help__ = """
 - /police : *Sirens* Polize iz here
 - /moon : Cycles all the phases of the moon emojis.
"""

POLICE_HANDLER = DisableAbleCommandHandler(["police"], police)
MOON_HANDLER = DisableAbleCommandHandler(["moon"], moon)

dispatcher.add_handler(POLICE_HANDLER)
dispatcher.add_handler(MOON_HANDLER)

__mod_name__ = "Parser"
__command_list__ = ["police", "moon"]
__handlers__ = [POLICE_HANDLER, MOON_HANDLER]
