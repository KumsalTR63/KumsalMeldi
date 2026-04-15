from io import BytesIO

from httpx import AsyncClient
from pyrogram import filters
from pyrogram.types import Message

from AloneMusic import app  # AloneMusic app instance

http = AsyncClient()


@app.on_message(filters.command("s") & filters.reply)
async def make_sticker(_, message: Message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply("⛔ Lütfen bir mesaja yanıt verin.")

    text = replied.text or replied.caption
    if not text:
        return await message.reply("⛔ Çıkartma yapılacak metin bulunamadı.")

    await message.reply("🛠️ Çıkartma hazırlanıyor...")

    data = {
        "type": "quote",
        "format": "webp",
        "backgroundColor": "#1e1e1e",
        "messages": [
            {
                "text": text,
                "author": {
                    "name": replied.from_user.first_name,
                    "id": replied.from_user.id,
                    "username": replied.from_user.username or "",
                },
            }
        ],
    }

    try:
        response = await http.post("https://bot.lyo.su/quote/generate.webp", json=data)
        img = BytesIO(response.content)
        img.name = "sticker.webp"
        await message.reply_sticker(img)
    except Exception as e:
        await message.reply(f"❌ Hata: {e}")
