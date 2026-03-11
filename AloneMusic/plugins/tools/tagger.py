from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from AloneMusic import app
from asyncio import sleep

running_tags = {}
MAX_MSG_LEN = 4000


async def safe_send(client: Client, chat_id: int, text: str, reply_id: int = None):
    try:
        await client.send_message(chat_id, text, reply_to_message_id=reply_id)
    except FloodWait as e:
        await sleep(e.value)
        await client.send_message(chat_id, text, reply_to_message_id=reply_id)


# ===== HERKESİ ETİKETLE =====
@app.on_message(filters.command(["utag"]) & filters.group)
async def tag_all(client: Client, message: Message):

    chat_id = message.chat.id

    if not message.reply_to_message:
        await message.reply("Bir mesaja cevap ver.")
        return

    reply_id = message.reply_to_message.id

    if chat_id in running_tags:
        return

    running_tags[chat_id] = True

    body = ""
    count = 0

    async for member in client.get_chat_members(chat_id):

        if chat_id not in running_tags:
            break

        user = member.user

        if user.is_bot or not user.username:
            continue

        body += f"@{user.username}\n"
        count += 1

        if count % 5 == 0 or len(body) > MAX_MSG_LEN:
            await safe_send(client, chat_id, body, reply_id)
            body = ""
            await sleep(2)

    if body:
        await safe_send(client, chat_id, body, reply_id)

    running_tags.pop(chat_id, None)


# ===== TEK TEK TAG =====
@app.on_message(filters.command(["tag"]) & filters.group)
async def single_tag(client: Client, message: Message):

    chat_id = message.chat.id

    if not message.reply_to_message:
        await message.reply("Bir mesaja cevap ver.")
        return

    reply_id = message.reply_to_message.id

    if chat_id in running_tags:
        return

    running_tags[chat_id] = True

    async for member in client.get_chat_members(chat_id):

        if chat_id not in running_tags:
            break

        user = member.user

        if user.is_bot or not user.username:
            continue

        await safe_send(client, chat_id, f"@{user.username}", reply_id)
        await sleep(2)

    running_tags.pop(chat_id, None)


# ===== ADMİN TAG =====
@app.on_message(filters.command(["admintag"]) & filters.group)
async def admin_tag(client: Client, message: Message):

    chat_id = message.chat.id

    if not message.reply_to_message:
        await message.reply("Bir mesaja cevap ver.")
        return

    reply_id = message.reply_to_message.id

    body = ""

    async for member in client.get_chat_members(chat_id, filter="administrators"):

        user = member.user

        if user.is_bot or not user.username:
            continue

        body += f"@{user.username}\n"

    if body:
        await safe_send(client, chat_id, body, reply_id)


# ===== CANCEL =====
@app.on_message(filters.command(["cancel"]) & filters.group)
async def cancel_tag(client: Client, message: Message):

    chat_id = message.chat.id

    if chat_id in running_tags:
        running_tags.pop(chat_id, None)
        await message.reply("Etiketleme iptal edildi.")