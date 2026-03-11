from io import BytesIO

from httpx import AsyncClient, Timeout
from pyrogram import filters
from pyrogram.types import Message

from AloneMusic import app

fetch = AsyncClient(
    http2=True,
    verify=False,
    headers={
        "Accept-Language": "tr-TR",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edge/107.0.1418.42",
    },
    timeout=Timeout(20),
)


class QuotlyException(Exception):
    pass


# Buradan sonrası fonksiyonlar (değişmedi, sadece mesajlar çevrildi)


@app.on_message(filters.command(["q", "r"]) & filters.reply)
async def msg_quotly_cmd(self: app, ctx: Message):
    ww = await ctx.reply_text("⏳ Lütfen bekleyin...")
    is_reply = False
    if ctx.command[0].endswith("r"):
        is_reply = True
    if len(ctx.text.split()) > 1:
        check_arg = isArgInt(ctx.command[1])
        if check_arg[0]:
            if check_arg[1] < 2 or check_arg[1] > 10:
                await ww.delete()
                return await ctx.reply_msg(
                    "Geçersiz aralık! (2-10 arasında olmalı)", del_in=6
                )
            try:
                messages = [
                    i
                    for i in await self.get_messages(
                        chat_id=ctx.chat.id,
                        message_ids=range(
                            ctx.reply_to_message.id,
                            ctx.reply_to_message.id + (check_arg[1] + 5),
                        ),
                        replies=-1,
                    )
                    if not i.empty and not i.media
                ]
            except Exception:
                return await ctx.reply_text("🤷🏻‍♂️ Hata oluştu.")
            try:
                make_quotly = await pyrogram_to_quotly(messages, is_reply=is_reply)
                bio_sticker = BytesIO(make_quotly)
                bio_sticker.name = "alinti_sticker.webp"
                await ww.delete()
                return await ctx.reply_sticker(bio_sticker)
            except Exception:
                await ww.delete()
                return await ctx.reply_msg("🤷🏻‍♂️ Alıntı oluşturulamadı.")
    try:
        messages_one = await self.get_messages(
            chat_id=ctx.chat.id, message_ids=ctx.reply_to_message.id, replies=-1
        )
        messages = [messages_one]
    except Exception:
        await ww.delete()
        return await ctx.reply_msg("🤷🏻‍♂️ Hata oluştu.")
    try:
        make_quotly = await pyrogram_to_quotly(messages, is_reply=is_reply)
        bio_sticker = BytesIO(make_quotly)
        bio_sticker.name = "alinti_sticker.webp"
        await ww.delete()
        return await ctx.reply_sticker(bio_sticker)
    except Exception as e:
        await ww.delete()
        return await ctx.reply_msg(f"HATA: {e}")


__HELP__ = """
**Alıntı Oluşturma Komutları**

Bu komutları kullanarak mesajlardan **alıntı stickerları** oluşturabilirsiniz:

- `/q` : Yalnızca yanıtladığınız bir mesajdan alıntı oluşturur.  
- `/r` : Yanıtladığınız mesaj ve ona verilen cevabı birlikte alıntılar.  

**Örnekler:**
- `/q` : Yanıtladığınız mesajdan alıntı oluşturur.  
- `/r` : Yanıtladığınız mesaj + cevabı alıntılar.  

**Not:**  
Alıntı komutunun çalışması için mutlaka bir mesaja yanıt vermeniz gerekir.
"""

__MODULE__ = "Alıntı"
