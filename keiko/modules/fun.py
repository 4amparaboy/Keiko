import html
import random
import time
from typing import List
import random, re, string, io, asyncio
from PIL import Image
from io import BytesIO
import base64
from zalgo_text import zalgo
import os
from pathlib import Path
import glob
import requests
import nekos

import nltk # shitty lib, but it does work
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from typing import Optional, List
from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async
from deeppyer import deepfry

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

import keiko.modules.fun_strings as fun_strings
from keiko import dispatcher
from keiko.modules.disable import DisableAbleCommandHandler
from keiko.modules.helper_funcs.chat_status import is_user_admin
from keiko.modules.helper_funcs.extraction import extract_user
from keiko.modules.disable import DisableAbleCommandHandler, DisableAbleRegexHandler

WIDE_MAP = dict((i, i + 0xFEE0) for i in range(0x21, 0x7F))
WIDE_MAP[0x20] = 0x3000

@run_async
def runs(bot: Bot, update: Update):
    update.effective_message.reply_text(random.choice(fun_strings.RUN_STRINGS))
# D A N K modules by @deletescape vvv


@run_async
def slap(bot: Bot, update: Update, args: List[str]):
def owo(bot: Bot, update: Update):
    message = update.effective_message
    chat = update.effective_chat

    reply_text = message.reply_to_message.reply_text if message.reply_to_message else message.reply_text
    if not message.reply_to_message:
        message.reply_text("I need a message to meme.")
    else:
        faces = ['(・`ω´・)',';;w;;','owo','UwU','>w<','^w^','\(^o\) (/o^)/','( ^ _ ^)∠☆','(ô_ô)','~:o',';____;', '(*^*)', '(>_', '(♥_♥)', '*(^O^)*', '((+_+))']
        reply_text = re.sub(r'[rl]', "w", message.reply_to_message.text)
        reply_text = re.sub(r'[ｒｌ]', "ｗ", message.reply_to_message.text)
        reply_text = re.sub(r'[RL]', 'W', reply_text)
        reply_text = re.sub(r'[ＲＬ]', 'Ｗ', reply_text)
        reply_text = re.sub(r'n([aeiouａｅｉｏｕ])', r'ny\1', reply_text)
        reply_text = re.sub(r'ｎ([ａｅｉｏｕ])', r'ｎｙ\1', reply_text)
        reply_text = re.sub(r'N([aeiouAEIOU])', r'Ny\1', reply_text)
        reply_text = re.sub(r'Ｎ([ａｅｉｏｕＡＥＩＯＵ])', r'Ｎｙ\1', reply_text)
        reply_text = re.sub(r'\!+', ' ' + random.choice(faces), reply_text)
        reply_text = re.sub(r'！+', ' ' + random.choice(faces), reply_text)
        reply_text = reply_text.replace("ove", "uv")
        reply_text = reply_text.replace("ｏｖｅ", "ｕｖ")
        reply_text += ' ' + random.choice(faces)
        message.reply_to_message.reply_text(reply_text)

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == bot.id:
        temp = random.choice(fun_strings.SLAP_SAITAMA_TEMPLATES)
@run_async
def stretch(bot: Bot, update: Update):
    message = update.effective_message
    if not message.reply_to_message:
        message.reply_text("I need a message to meme.")
    else:
        count = random.randint(3, 10)
        reply_text = re.sub(r'([aeiouAEIOUａｅｉｏｕＡＥＩＯＵ])', (r'\1' * count), message.reply_to_message.text)
        message.reply_to_message.reply_text(reply_text)

        if isinstance(temp, list):
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):
                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(chat.id, message.from_user.id, until_date=mutetime, can_send_messages=False)
            reply_text(temp[0])
@run_async
def vapor(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    if not message.reply_to_message:
        if not args:
            message.reply_text("I need a message to convert to vaporwave text.")
        else:
            reply_text(temp)
        return
            noreply = True
            data = message.text.split(None, 1)[1]
    elif message.reply_to_message:
        noreply = False
        data = message.reply_to_message.text
    else:
        data = ''

    if user_id:
    reply_text = str(data).translate(WIDE_MAP)
    if noreply:
        message.reply_text(reply_text)
    else:
        message.reply_to_message.reply_text(reply_text)

        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(slapped_user.first_name)


@run_async
def kan(bot: Bot, update: Update):
    msg = update.effective_message
    if not msg.reply_to_message:
        msg.reply_text("need to reply to a message to kannify.")
    else:
        user1 = bot.first_name
        user2 = curr_user
        text = msg.reply_to_message.text
        r = requests.get(f"https://nekobot.xyz/api/imagegen?type=kannagen&text={text}").json()
        url = r.get("message")
        if not url:
            msg.reply_text("No URL was received from the API!")
            return
        with open("temp.png","wb") as f:
            f.write(requests.get(url).content)
        img = Image.open("temp.png")
        img.save("temp.webp","webp")
        msg.reply_document(open("temp.webp","rb"))
        os.remove("temp.webp")

    temp = random.choice(fun_strings.SLAP_TEMPLATES)
    item = random.choice(fun_strings.ITEMS)
    hit = random.choice(fun_strings.HIT)
    throw = random.choice(fun_strings.THROW)
@run_async
def eightball(bot: Bot, update: Update):
    msg = update.effective_message
    target = '8ball'
    with open("temp.png","wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp","webp")
    msg.reply_document(open("temp.webp","rb"))
    os.remove("temp.webp")

    reply = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw)
@run_async
def changemymind(bot: Bot, update: Update):
    msg = update.effective_message
    if not msg.reply_to_message:
        msg.reply_text("need to reply to a message to stickerize.")
    else:
        text = msg.reply_to_message.text
        r = requests.get(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}").json()
        url = r.get("message")
        if not url:
            msg.reply_text("No URL was received from the API!")
            return
        with open("temp.png","wb") as f:
            f.write(requests.get(url).content)
        img = Image.open("temp.png")
        img.save("temp.webp","webp")
        msg.reply_document(open("temp.webp","rb"))
        os.remove("temp.webp")

    reply_text(reply, parse_mode=ParseMode.HTML)
@run_async
def trumptweet(bot: Bot, update: Update):
    msg = update.effective_message
    if not msg.reply_to_message:
        msg.reply_text("need to reply to a message to tweet")
    else:
        text = msg.reply_to_message.text
        r = requests.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}").json()
        url = r.get("message")
        if not url:
            msg.reply_text("No URL was received from the API!")
            return
        with open("temp.png","wb") as f:
            f.write(requests.get(url).content)
        img = Image.open("temp.png")
        img.save("temp.webp","webp")
        msg.reply_document(open("temp.webp","rb"))
        os.remove("temp.webp")


@run_async
def roll(bot: Bot, update: Update):
    update.message.reply_text(random.choice(range(1, 7)))
def zalgotext(bot: Bot, update: Update):
    message = update.effective_message
    if message.reply_to_message:
        data = message.reply_to_message.text
    else:
        data = str('Insolant human, you must reply to something to zalgofy it!')

    reply_text = zalgo.zalgo().zalgofy(data)
    message.reply_text(reply_text)

# Less D A N K modules by @skittles9823 # holi fugg I did some maymays ^^^
# shitty maymay modules made by @divadsn vvv

@run_async
def toss(bot: Bot, update: Update):
    update.message.reply_text(random.choice(fun_strings.TOSS))
def forbesify(bot: Bot, update: Update):
    message = update.effective_message
    if message.reply_to_message:
        data = message.reply_to_message.text
    else:
        data = ''

    data = data.lower()
    accidentals = ['VB', 'VBD', 'VBG', 'VBN']
    reply_text = data.split()
    offset = 0

@run_async
def abuse(bot: Bot, update: Update):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text(random.choice(fun_strings.ABUSE_STRINGS))
    # use NLTK to find out where verbs are
    tagged = dict(nltk.pos_tag(reply_text))

    # let's go through every word and check if it's a verb
    # if yes, insert ACCIDENTALLY and increase offset
    for k in range(len(reply_text)):
        i = reply_text[k + offset]
        if tagged.get(i) in accidentals:
            reply_text.insert(k + offset, 'accidentally')
            offset += 1

@run_async
def shrug(bot: Bot, update: Update):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text(r"¯\_(ツ)_/¯")
    reply_text = string.capwords(' '.join(reply_text))
    message.reply_to_message.reply_text(reply_text)


@run_async
def bluetext(bot: Bot, update: Update):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text("/BLUE /TEXT\n/MUST /CLICK\n/I /AM /A /STUPID /ANIMAL /THAT /IS /ATTRACTED /TO /COLORS")
def deepfryer(bot: Bot, update: Update):
    message = update.effective_message
    if message.reply_to_message:
        data = message.reply_to_message.photo
        data2 = message.reply_to_message.sticker
    else:
        data = []
        data2 = []

    # check if message does contain media and cancel when not
    if not data and not data2:
        message.reply_text("What am I supposed to do with this?!")
        return

@run_async
def rlg(bot: Bot, update: Update):
    eyes = random.choice(fun_strings.EYES)
    mouth = random.choice(fun_strings.MOUTHS)
    ears = random.choice(fun_strings.EARS)
    # download last photo (highres) as byte array
    if data:
        photodata = data[len(data) - 1].get_file().download_as_bytearray()
        image = Image.open(io.BytesIO(photodata))
    elif data2:
        sticker = bot.get_file(data2.file_id)
        sticker.download('sticker.png')
        image = Image.open("sticker.png")

    if len(eyes) == 2:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[1] + ears[1]
    else:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[0] + ears[1]
    update.message.reply_text(repl)
    # the following needs to be executed async (because dumb lib)
    loop = asyncio.new_event_loop()
    loop.run_until_complete(process_deepfry(image, message.reply_to_message, bot))
    loop.close()


@run_async
def decide(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.DECIDE))
async def process_deepfry(image: Image, reply: Message, bot: Bot):
    # DEEPFRY IT
    image = await deepfry(
        img=image,
        token=os.getenv('DEEPFRY_TOKEN', ''),
        url_base='westeurope'
    )

    bio = BytesIO()
    bio.name = 'image.jpeg'
    image.save(bio, 'JPEG')

    # send it back
    bio.seek(0)
    reply.reply_photo(bio)
    if Path("sticker.png").is_file():
        os.remove("sticker.png")

# shitty maymay modules made by @divadsn ^^^


@run_async
def table(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.TABLE))
def shout(bot: Bot, update: Update, args):
    if len(args) == 0:
        update.effective_message.reply_text("Where is text?")
        return

    msg = "```"
    text = " ".join(args)
    result = []
    result.append(' '.join([s for s in text]))
    for pos, symbol in enumerate(text[1:]):
        result.append(symbol + ' ' + '  ' * pos + symbol)
    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return update.effective_message.reply_text(msg, parse_mode="MARKDOWN")


# no help string
__help__ = """
 - /runs: reply a random string from an array of replies.
 - /slap: slap a user, or get slapped if not a reply.
 - /shrug : get shrug XD.
 - /table : get flip/unflip :v.
 - /decide : Randomly answers yes/no/maybe
 - /toss : Tosses A coin
 - /bluetext : check urself :V
 - /roll : Roll a dice.
 - /rlg : Join ears,nose,mouth and create an emo ;-;
Some memes command, find it all out yourself!
- /owo: OWO de text
- /stretch: STRETCH de text
- /vapor: owo vapor dis
- /mock: mocks a spongebob image with text
- /shout: Write anything that u want it to should
- /zalgofy: reply to a message to g̫̞l̼̦i̎͡tͫ͢c̘ͭh̛̗ it out!
- /kan: reply a text to kannafy.
- /changemymind: reply a text to stickerize.
- /trumptweet: reply a text for trump tweet.
- /eightball: shakes 8ball.
"""

RUNS_HANDLER = DisableAbleCommandHandler("runs", runs)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap, pass_args=True)
ROLL_HANDLER = DisableAbleCommandHandler("roll", roll)
TOSS_HANDLER = DisableAbleCommandHandler("toss", toss)
SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug)
BLUETEXT_HANDLER = DisableAbleCommandHandler("bluetext", bluetext)
RLG_HANDLER = DisableAbleCommandHandler("rlg", rlg)
DECIDE_HANDLER = DisableAbleCommandHandler("decide", decide)
TABLE_HANDLER = DisableAbleCommandHandler("table", table)

dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(ROLL_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(BLUETEXT_HANDLER)
dispatcher.add_handler(RLG_HANDLER)
dispatcher.add_handler(DECIDE_HANDLER)
dispatcher.add_handler(TABLE_HANDLER)

__mod_name__ = "FUN"
__command_list__ = ["runs", "slap", "roll", "toss", "shrug", "bluetext", "rlg", "decide", "table"]
__handlers__ = [RUNS_HANDLER, SLAP_HANDLER, ROLL_HANDLER, TOSS_HANDLER, SHRUG_HANDLER, BLUETEXT_HANDLER, RLG_HANDLER,
                DECIDE_HANDLER, TABLE_HANDLER]
__mod_name__ = "Memes"

OWO_HANDLER = DisableAbleCommandHandler("owo", owo, admin_ok=True)
STRETCH_HANDLER = DisableAbleCommandHandler("stretch", stretch)
VAPOR_HANDLER = DisableAbleCommandHandler("vapor", vapor, pass_args=True, admin_ok=True)
ZALGO_HANDLER = DisableAbleCommandHandler("zalgofy", zalgotext)
DEEPFRY_HANDLER = DisableAbleCommandHandler("deepfry", deepfryer, admin_ok=True)
SHOUT_HANDLER = DisableAbleCommandHandler("shout", shout, pass_args=True)
KAN_HANDLER = DisableAbleCommandHandler("kan", kan)
CHANGEMYMIND_HANDLER = DisableAbleCommandHandler("changemymind", changemymind)
TRUMPTWEET_HANDLER = DisableAbleCommandHandler("trumptweet", trumptweet)
EIGHTBALL_HANDLER = DisableAbleCommandHandler("eightball", eightball)

dispatcher.add_handler(SHOUT_HANDLER)
dispatcher.add_handler(OWO_HANDLER)
dispatcher.add_handler(STRETCH_HANDLER)
dispatcher.add_handler(VAPOR_HANDLER)
dispatcher.add_handler(ZALGO_HANDLER)
dispatcher.add_handler(DEEPFRY_HANDLER)
dispatcher.add_handler(KAN_HANDLER)
dispatcher.add_handler(CHANGEMYMIND_HANDLER)
dispatcher.add_handler(TRUMPTWEET_HANDLER)
dispatcher.add_handler(EIGHTBALL_HANDLER)
