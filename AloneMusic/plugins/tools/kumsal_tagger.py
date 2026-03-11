import random
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from AloneMusic import app  # Assuming this imports the 'app' instance from AloneMusic
from config import LOGGER_ID, OWNER_ID  # Configuration for logging group and owner ID
from AloneMusic.plugins.tools.oner import *  # Assuming this imports the necessary messages like mani, slapmessage, sarki1, etc.

#  ~~~~~~~~~~~~~~~~ OYUN KOMUTLARI ~~~~~~~~~~~~~~~~
DICE_EMOJI = {
    "zar": "🎲",
    "dart": "🎯",
    "basket": "🏀",
    "futbol": "⚽",
    "bowling": "🎳",
    "slot": "🍒"
}

@app.on_message(filters.command(list(DICE_EMOJI.keys()) + ["para", "mani", "saka"]))
async def games(client, message: Message):
    command = message.command[0]

    if command in DICE_EMOJI:
        await client.send_dice(
            message.chat.id,
            emoji=DICE_EMOJI[command],
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Tekrar Oyna ♻️", callback_data=command)]]
            )
        )
    elif command == "para":
        await message.reply("**Yazı 🪙**" if random.randint(0, 1) == 0 else "**Tura 🪙**")
    elif command == "mani":
        await message.reply_text(random.choice(mani))
    elif command == "saka":
        await message.reply_text(f"**{random.choice(espri)}**")


#  ~~~~~~~~~~~~~~~~ Tekrar Oyna Callback ~~~~~~~~~~~~~~~~
@app.on_callback_query(filters.regex("|".join(DICE_EMOJI.keys())))
async def play_again(client, query: CallbackQuery):
    command = query.data
    await client.send_dice(
        query.message.chat.id,
        emoji=DICE_EMOJI[command],
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Tekrar Oyna ♻️", callback_data=command)]]
        )
    )


#  ~~~~~~~~~~~~~~~~ Slap / Sille Komutu ~~~~~~~~~~~~~~~~
@app.on_message(filters.command(["slap", "sille"]) & filters.group)
async def slap(bot, message: Message):
    if not message.reply_to_message:
        await message.reply_text("⚠️ Bir kullanıcıya cevap verin!")
        return

    if message.reply_to_message.from_user.id == OWNER_ID:
        await message.reply_text(f"{random.choice(dontslapown)}")
        return

    if message.reply_to_message.from_user.id == bot.id:
        await message.reply_text(f"{random.choice(dontslapme)}")
        return

    atan = message.from_user
    yiyen = message.reply_to_message.from_user
    atan_mesaj = f"@{atan.username}" if atan.username else atan.mention
    yiyen_mesaj = f"@{yiyen.username}" if yiyen.username else yiyen.mention
    text = random.choice(slapmessage).format(atan_mesaj, yiyen_mesaj)
    await message.reply_text(text)

    await bot.send_message(
        LOGGER_ID,
        f"""
⚡ Kullanan: {atan_mesaj}  
👤 Kullanıcı Id: {atan.id}  
📱 Kullanılan Grup: {message.chat.title}  
📍 Grup ID: {message.chat.id}  
🔗 Grup Link: @{message.chat.username}  
⚙️ Kullanılan Modül: Slap
"""
    )


#  ~~~~~~~~~~~~~~~~ Şarkı Öner Komutu ~~~~~~~~~~~~~~~~
@app.on_message(filters.command(["oner"]) & filters.group)
async def oner(bot, message: Message):
    if not message.reply_to_message:
        await message.reply_text("⚠️ Bir kullanıcıya cevap verin!")
        return

    if message.reply_to_message.from_user.id == OWNER_ID:
        await message.reply_text(f"{random.choice(sarki1)}")
        return

    if message.reply_to_message.from_user.id == bot.id:
        await message.reply_text(f"{random.choice(sarki2)}")
        return

    atan = message.from_user
    yiyen = message.reply_to_message.from_user
    atan_mesaj = f"@{atan.username}" if atan.username else atan.mention
    yiyen_mesaj = f"@{yiyen.username}" if yiyen.username else yiyen.mention
    text = random.choice(sarkilar).format(atan_mesaj, yiyen_mesaj)
    await message.reply_text(text)

    await bot.send_message(
        LOGGER_ID,
        f"""
⚡ Kullanan: {atan_mesaj}  
👤 Kullanıcı Id: {atan.id}  
📱 Kullanılan Grup: {message.chat.title}  
📍 Grup ID: {message.chat.id}  
🔗 Grup Link: @{message.chat.username}  
🎶 Kullanılan Modül: Şarkı Öneri
"""
    )