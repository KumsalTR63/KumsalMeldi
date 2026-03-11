import asyncio
import random
from typing import Union
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    CallbackQuery,
)
from AloneMusic import app
from config import LOGGER_ID
from AloneMusic.plugins.tools.kumsal import *

import asyncio
import random
from typing import Union
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from AloneMusic import app
from config import LOGGER_ID
from AloneMusic.plugins.tools.kumsal import *

import asyncio
import random
from typing import Union
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from AloneMusic import app
from config import LOGGER_ID
from AloneMusic.plugins.tools.kumsal import *

# Sohbet modu açık olan grupları tutuyor
chatMode = []

# Sohbet modunu açıp kapatan kullanıcıları takip etmek için
chat_mode_users = {}

@app.on_message(filters.command("chatmode") & filters.group)
async def chat_mode_controller(bot, msg: Message):
    chat_id = msg.chat.id
    chat = msg.chat
    commands = msg.command
    chat_mode_users[chat_id] = msg.from_user.id  # Komutu gönderen kullanıcıyı kaydet

    # LOG GROUP'a mesaj gönder
    await bot.send_message(
        LOGGER_ID,
        f"""
#CHATMODE KULLANILDI 👤 Kullanan : {msg.from_user.first_name} 💥 Kullanıcı Id : {msg.from_user.id} 🪐 Kullanılan Grup : {chat.title} 💡 Grup ID : {chat.id} ◀️ Grup Link : @{chat.username}"""
    )

    if len(commands) == 1:
        status = "✅ Açık" if chat_id in chatMode else "❌ Kapalı"
        await msg.reply(
            f"Durum : {status}\n\nSohbet modu kullanıcıların mesajlarına cevap verir.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Aç", callback_data="on"),
                        InlineKeyboardButton("Kapat", callback_data="off"),
                    ]
                ]
            ),
        )

@app.on_callback_query(filters.regex("^(on|off)$"))
async def chat_mode_callback(bot, cb: CallbackQuery):
    chat_id = cb.message.chat.id
    cmd = cb.data

    # Artık yetki kontrolü yok, herkes değiştirebilir
    if cmd == "on":
        if chat_id in chatMode:
            await cb.edit_message_text("Sohbet modu zaten açık.")
        else:
            chatMode.append(chat_id)
            await cb.edit_message_text("Sohbet modu açıldı.")
    elif cmd == "off":
        if chat_id not in chatMode:
            await cb.edit_message_text("Sohbet modu zaten kapalı.")
        else:
            chatMode.remove(chat_id)
            await cb.edit_message_text("Sohbet modu kapatıldı.")

    await cb.answer()

@app.on_message(filters.group & filters.text & ~filters.command("chatmode"), group=10)
async def chatModeHandler(bot, msg: Message):
    def lower(text):
        return str(text.translate({ord("I"): ord("ı"), ord("İ"): ord("i")})).lower()

    def kontrol(query: Union[str, list], text: str) -> bool:
        if isinstance(query, str):
            return query in text.split()
        elif isinstance(query, list):
            for q in query:
                if q in text.split():
                    return True
            return False
        else:
            return False

    if msg.chat.id not in chatMode or msg.from_user.is_self:
        return

    reply = None
    text = lower(msg.text)

    if text.startswith("ceyda"): # * Mesaj buse ile başlıyorsa cevap veriyoruz
        reply = random.choice(ceyda)
        await asyncio.sleep(0.06)

    elif kontrol(["selam", "slm", "sa", "selamlar", "selamm"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(slm)
        await asyncio.sleep(0.06)   
        #Bot chatmode komutları
    elif kontrol(["sahip"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sahip)
        await asyncio.sleep(0.06)   

    elif kontrol(["naber"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(naber)
        await asyncio.sleep(0.06)  

    elif kontrol(["beri"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(beri)
        await asyncio.sleep(0.06)        

    elif kontrol(["nasılsın"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nasılsın)
        await asyncio.sleep(0.06)         

    elif kontrol(["tm","tamam","tmm"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(tm)
        await asyncio.sleep(0.06)          

    elif kontrol(["sus","suuss","suss"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sus)
        await asyncio.sleep(0.06)  

    elif kontrol(["merhaba","mrb","meraba"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(merhaba)
        await asyncio.sleep(0.06)   

    elif kontrol(["yok"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(yok)
        await asyncio.sleep(0.06)   

    elif kontrol(["dur"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(dur)
        await asyncio.sleep(0.06)        

    elif kontrol(["bot", "botu"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(bott)
        await asyncio.sleep(0.06)         

    elif kontrol(["napıyorsun"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(napıyorsun)
        await asyncio.sleep(0.06)          

    elif kontrol(["takılıyorum","takılıyom"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(takılıyorum)
        await asyncio.sleep(0.06)  

    elif kontrol(["he"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(he)
        await asyncio.sleep(0.06)   

    elif kontrol(["hayır"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hayır)
        await asyncio.sleep(0.06)   

    elif kontrol(["tm"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(tm)
        await asyncio.sleep(0.06)        

    elif kontrol(["nerdesin"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nerdesin)
        await asyncio.sleep(0.06)         

    elif kontrol(["özledim"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(özledim)
        await asyncio.sleep(0.06)          

    elif kontrol(["bekle"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(bekle)
        await asyncio.sleep(0.06)  

    elif kontrol(["mustafa"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(mustafa)
        await asyncio.sleep(0.06)   

    elif kontrol(["günaydın"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(günaydın)
        await asyncio.sleep(0.06)   

    elif kontrol(["ragnar"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(ragnar)
        await asyncio.sleep(0.06)        

    elif kontrol(["konuşalım","konusalım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(konuşalım)
        await asyncio.sleep(0.06)         

    elif kontrol(["saat"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(saat)
        await asyncio.sleep(0.06)          

    elif kontrol(["geceler"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(geceler)
        await asyncio.sleep(0.06)  

    elif kontrol(["şaka"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(şaka)
        await asyncio.sleep(0.06)   

    elif kontrol(["kimsin"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(kimsin)
        await asyncio.sleep(0.06)   

    elif kontrol(["günler"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(günler)
        await asyncio.sleep(0.06)        

    elif kontrol(["tanımıyorum"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(tanımıyorum)
        await asyncio.sleep(0.06)         

    elif kontrol(["konuşma"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(konuşma)
        await asyncio.sleep(0.06)          

    elif kontrol(["teşekkürler","tesekkürler","tşkr"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(teşekkürler)
        await asyncio.sleep(0.06)  

    elif kontrol(["eyvallah","eywl"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(eyvallah)
        await asyncio.sleep(0.06)   

    elif kontrol(["sağol"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sağol)
        await asyncio.sleep(0.06)   

    elif kontrol(["amk","aq","mg","mk"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(amk)
        await asyncio.sleep(0.06)        

    elif kontrol(["yoruldum"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(yoruldum)
        await asyncio.sleep(0.06)         

    elif kontrol(["yaş"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(yaş)
        await asyncio.sleep(0.06)          

    elif kontrol(["eşşek","eşek"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(eşek)
        await asyncio.sleep(0.06)  

    elif kontrol(["canım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(canım)
        await asyncio.sleep(0.06)   

    elif kontrol(["aşkım","askım","ask"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(aşkım)
        await asyncio.sleep(0.06)   

    elif kontrol(["uyu"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(uyu)
        await asyncio.sleep(0.06)        

    elif kontrol(["nereye","nere"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nereye)
        await asyncio.sleep(0.06)         

    elif kontrol(["naber"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(naber)
        await asyncio.sleep(0.06)          

    elif kontrol(["küstüm","küsüm"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(küstüm)
        await asyncio.sleep(0.06)  

    elif kontrol(["peki"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(peki)
        await asyncio.sleep(0.06)   

    elif kontrol(["ne","nee","neee","ney"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(ne)
        await asyncio.sleep(0.06)   

    elif kontrol(["takım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(takım)
        await asyncio.sleep(0.06)        

    elif kontrol(["benimle","bnmle"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(benimle)
        await asyncio.sleep(0.06)         

    elif kontrol(["seviyormusun","seviyomusun"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(seviyormusun)
        await asyncio.sleep(0.06)          

    elif kontrol(["nediyon"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nediyon)
        await asyncio.sleep(0.06)  

    elif kontrol(["özür"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(özür)
        await asyncio.sleep(0.06)   

    elif kontrol(["niye"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(niye)
        await asyncio.sleep(0.06)   

    elif kontrol(["bilmiyorum","bilmiyom","bilmiyos"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(bilmiyorum)
        await asyncio.sleep(0.06)        

    elif kontrol(["küsme"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(küsme)
        await asyncio.sleep(0.06)         

    elif kontrol(["Cihan"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(cihan)
        await asyncio.sleep(0.06)          

    elif kontrol(["nerelisin"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nerelisin)
        await asyncio.sleep(0.06)  

    elif kontrol(["sevgilin"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sevgilin)
        await asyncio.sleep(0.06)   

    elif kontrol(["olur"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(olur)
        await asyncio.sleep(0.06)   

    elif kontrol(["olmas","olmaz"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(olmaz)
        await asyncio.sleep(0.06)        

    elif kontrol(["nasıl"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nasıl)
        await asyncio.sleep(0.06)         

    elif kontrol(["hayatım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hayatım)
        await asyncio.sleep(0.06)          

    elif kontrol(["cus"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(cus)
        await asyncio.sleep(0.06)  

    elif kontrol(["vallaha","valla","vallahi"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(vallaha)
        await asyncio.sleep(0.06)   

    elif kontrol(["yo"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(yo)
        await asyncio.sleep(0.06)   

    elif kontrol(["hayırdır"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hayırdır)
        await asyncio.sleep(0.06)        

    elif kontrol(["of"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(of)
        await asyncio.sleep(0.06)         

    elif kontrol(["aynen"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(aynen)
        await asyncio.sleep(0.06)          

    elif kontrol(["ağla"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(ağla)
        await asyncio.sleep(0.06)  

    elif kontrol(["ağlama"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(ağlama)
        await asyncio.sleep(0.06)   

    elif kontrol(["Mehmet","yaren","cihan","alya"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(yaren)
        await asyncio.sleep(0.06)   

    elif kontrol(["evet"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(evet)
        await asyncio.sleep(0.06)        

    elif kontrol(["hmm","hm","hımm","hmmm"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hmm)
        await asyncio.sleep(0.06)         

    elif kontrol(["hıhım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hıhım)
        await asyncio.sleep(0.06)          

    elif kontrol(["git"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(git)
        await asyncio.sleep(0.06)  

    elif kontrol(["komedi"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(komedi)
        await asyncio.sleep(0.06)   

    elif kontrol(["knka","kanka"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(knka)
        await asyncio.sleep(0.06)   

    elif kontrol(["ban"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(ban)
        await asyncio.sleep(0.06)        

    elif kontrol(["sen"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sen)
        await asyncio.sleep(0.06)         

    elif kontrol(["hiç"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hiç)
        await asyncio.sleep(0.06)          

    elif kontrol(["aç","ac","açç"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(aç)
        await asyncio.sleep(0.06)  

    elif kontrol(["barışalım","batısalım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(barışalım)
        await asyncio.sleep(0.06)   

    elif kontrol(["şimdi"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(şimdi)
        await asyncio.sleep(0.06)   

    elif kontrol(["varoş"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(varoş)
        await asyncio.sleep(0.06)        

    elif kontrol(["arkadaş","arkadas"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(arkadaş)
        await asyncio.sleep(0.06)         

    elif kontrol(["sus","suss","suus"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sus)
        await asyncio.sleep(0.06)          

    elif kontrol(["üzüldüm","üşüldüm"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(üzüldüm)
        await asyncio.sleep(0.06)  

    elif kontrol(["kötü"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(kötü)
        await asyncio.sleep(0.06)   

    elif kontrol(["akşamlar"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(akşamlar)
        await asyncio.sleep(0.06)   

    try:
        await msg.reply(reply)
    except Exception as e:
        print(e)

    msg.continue_propagation()  #! BURAYA DOKUNMA