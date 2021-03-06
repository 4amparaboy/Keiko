

from telegram import Update, Bot, ParseMode
from time import sleep
from telegram.ext import run_async

from keiko import dispatcher
from keiko.modules.disable import DisableAbleCommandHandler
from keiko.modules.helper_funcs.chat_status import is_user_admin, user_admin


@run_async
def police(bot: Bot, update: Update):
    message = update.effective_message.reply_text('/police')


    animation_chars = [
                "š“š“š“ā¬ļøā¬ļøā¬ļøšµšµšµ\nš“š“š“ā¬ļøā¬ļøā¬ļøšµšµšµ\nš“š“š“ā¬ļøā¬ļøā¬ļøšµšµšµ",

                "šµšµšµā¬ļøā¬ļøā¬ļøš“š“š“\nšµšµšµā¬ļøā¬ļøā¬ļøš“š“š“\nšµšµšµā¬ļøā¬ļøā¬ļøš“š“š“",

                "š“š“š“ā¬ļøā¬ļøā¬ļøšµšµšµ\nš“š“š“ā¬ļøā¬ļøā¬ļøšµšµšµ\nš“š“š“ā¬ļøā¬ļøā¬ļøšµšµšµ",

                "šµšµšµā¬ļøā¬ļøā¬ļøš“š“š“\nšµšµšµā¬ļøā¬ļøā¬ļøš“š“š“\nšµšµšµā¬ļøā¬ļøā¬ļøš“š“š“",

                "š“š“š“ā¬ļøā¬ļøā¬ļøšµšµšµ\nš“š“š“ā¬ļøā¬ļøā¬ļøšµšµšµ\nš“š“š“ā¬ļøā¬ļøā¬ļøšµšµšµ",

                "šµšµšµā¬ļøā¬ļøā¬ļøš“š“š“\nšµšµšµā¬ļøā¬ļøā¬ļøš“š“š“\nšµšµšµā¬ļøā¬ļøā¬ļøš“š“š“",

                "*Police iz Here*"
    ]
    for i in animation_chars:
        message.edit_text(i)
        sleep(0.5)

@run_async
def moon(bot: Bot, update: Update):
    message = update.effective_message.reply_text('/moon')

    animation_chars = [
                "šššššššš",

                "šššššššš",

                "šššššššš",

                "šššššššš",

                "šššššššš",

                "šššššššš",

                "šššššššš",

                "šššššššš",

                "~moon"
    ]
    for i in animation_chars:
        message.edit_text(i)
        sleep(0.5)

@run_async
def clock(bot: Bot, update: Update):
    message = update.effective_message.reply_text('/moon')

    animation_chars = [
                "šššššššššš",

                "šššššššššš",

                "šššššššššš",

                "šššššššššš",

                "šššššššššš",

                "šššššššššš",

                "šššššššššš",

                "šššššššššš",

                "*tick-tock*"
    ]
    for i in animation_chars:
        message.edit_text(i)
        sleep(0.5)

__help__ = """
 - /police : *Sirens* Polize iz here
 - /moon : Cycles all the phases of the moon emojis.
 - /clock : Cycles all the phases of the clock emojis.
"""

POLICE_HANDLER = DisableAbleCommandHandler(["police"], police)
MOON_HANDLER = DisableAbleCommandHandler(["moon"], moon)
CLOCK_HANDLER = DisableAbleCommandHandler(["clock"], clock)

dispatcher.add_handler(POLICE_HANDLER)
dispatcher.add_handler(MOON_HANDLER)
dispatcher.add_handler(CLOCK_HANDLER)

__mod_name__ = "Parser"
__command_list__ = ["police", "moon", "clock"]
__handlers__ = [POLICE_HANDLER, MOON_HANDLER, CLOCK_HANDLER]
