# ===========================================
# 💙 Kumsal Bots - Aşk Kuşları Modülü
# Özellikler: Sanal Hediye Sistemi + Aşk Hikayesi Üretici (MongoDB)
# Çeviri ve Düzenleme: Kumsal Music 💫
# Orijinal: Nand Yaduwanshi (NoxxOP)
# ===========================================

import random
from pyrogram import filters
from AloneMusic import app
from AloneMusic.core.mongo import mongodb
from config import MONGO_DB_URI

# MongoDB koleksiyonları
lovebirds_db = mongodb.lovebirds
users_collection = lovebirds_db.users
gifts_collection = lovebirds_db.gifts

# 🎁 Hediye Listesi
GIFTS = {
    "🌹": {"name": "Gül", "cost": 10, "emoji": "🌹"},
    "🍫": {"name": "Çikolata", "cost": 20, "emoji": "🍫"},
    "🧸": {"name": "Oyuncak Ayı", "cost": 30, "emoji": "🧸"},
    "💍": {"name": "Yüzük", "cost": 50, "emoji": "💍"},
    "❤️": {"name": "Kalp", "cost": 5, "emoji": "❤️"},
    "🌺": {"name": "Çiçek Buketi", "cost": 25, "emoji": "🌺"},
    "💎": {"name": "Elmas", "cost": 100, "emoji": "💎"},
    "🎀": {"name": "Hediye Kutusu", "cost": 40, "emoji": "🎀"},
    "🌙": {"name": "Ay", "cost": 35, "emoji": "🌙"},
    "⭐": {"name": "Yıldız", "cost": 15, "emoji": "⭐"},
    "🦋": {"name": "Kelebek", "cost": 18, "emoji": "🦋"},
    "🕊️": {"name": "Güvercin", "cost": 22, "emoji": "🕊️"},
    "🏰": {"name": "Şato", "cost": 80, "emoji": "🏰"},
    "🎂": {"name": "Pasta", "cost": 28, "emoji": "🎂"},
    "🍓": {"name": "Çilek", "cost": 12, "emoji": "🍓"}
}


# ───────────────────────────────
# 🔹 Kullanıcı bilgisi çekme veya oluşturma
# ───────────────────────────────
# 🔹 Kullanıcı bilgisi çekme veya oluşturma
async def get_user_data(user_id):
    if not user_id:
        return None

    user_data = await users_collection.find_one({"user_id": user_id})

    if not user_data:
        new_user = {
            "user_id": user_id,
            "coins": 50,  # Başlangıç bonusu
            "total_gifts_received": 0,
            "total_gifts_sent": 0,
            "created_at": "2025"
        }
        await users_collection.insert_one(new_user)
        return new_user

    return user_data


# 🔹 Coin güncelleme
async def update_user_coins(user_id, amount):
    if not user_id:
        return

    await users_collection.update_one(
        {"user_id": user_id},
        {"$inc": {"coins": amount}},
        upsert=True
    )


# 🔹 Kullanıcı bilgisi al (GÜVENLİ)
def get_user_info(message):

    if not message or not message.from_user:
        return None, "Bilinmeyen"

    user_id = message.from_user.id

    username = (
        message.from_user.username
        or message.from_user.first_name
        or "Kullanıcı"
    )

    return user_id, username

# ───────────────────────────────
# 💰 Bakiye Komutu
# ───────────────────────────────
@app.on_message(filters.command(["bakiye", "bal"], prefixes=["/", "!", "."]))
async def balance(_, message):
    uid, username = get_user_info(message)
    user_data = await get_user_data(uid)

    coins = user_data["coins"]
    gifts_received = await gifts_collection.count_documents({"receiver_id": uid})
    gifts_sent = await gifts_collection.count_documents({"sender_id": uid})

    balance_text = f"""
💰 <b>{username} Hesabı</b>
💸 <b>Bakiye:</b> {coins} coin
🎁 <b>Alınan Hediyeler:</b> {gifts_received}
📤 <b>Gönderilen Hediyeler:</b> {gifts_sent}

💡 <b>İpucu:</b> Sohbette aktif oldukça coin kazanırsın!
    """
    await message.reply_text(balance_text)


# ───────────────────────────────
# 🎁 Hediye Listesi
# ───────────────────────────────
@app.on_message(filters.command("hediyeler", prefixes=["/", "!", "."]))
async def gift_list(_, message):
    text = "🎁 <b>Mevcut Hediyeler:</b>\n\n"
    sorted_gifts = sorted(GIFTS.items(), key=lambda x: x[1]["cost"])

    for emoji, gift_info in sorted_gifts:
        text += f"{emoji} <b>{gift_info['name']}</b> - {gift_info['cost']} coin\n"

    text += "\n📝 <b>Kullanım:</b> /hediyegonder @kullanici 🌹"
    text += "\n💡 <b>Örnek:</b> /hediyegonder @ahmet 🍫"

    await message.reply_text(text)


# ───────────────────────────────
# 💌 Hediye Gönderme
# ───────────────────────────────
@app.on_message(filters.command("hediyegonder", prefixes=["/", "!", "."]))
async def send_gift(_, message):
    try:
        parts = message.text.split(" ")
        if len(parts) < 3:
            return await message.reply_text("❌ <b>Kullanım:</b> /hediyegonder @kullanici 🌹")

        hedef = parts[1].replace("@", "")
        gift_emoji = parts[2]

        sender_id, sender_name = get_user_info(message)
        sender_data = await get_user_data(sender_id)

        if gift_emoji not in GIFTS:
            return await message.reply_text("❌ <b>Geçersiz hediye!</b> Tüm hediyeleri görmek için /hediyeler yaz.")

        gift_info = GIFTS[gift_emoji]
        cost = gift_info["cost"]

        if sender_data["coins"] < cost:
            return await message.reply_text(f"😢 <b>Yetersiz coin!</b>\n💰 Gerekli: {cost}, Mevcut: {sender_data['coins']}")

        await users_collection.update_one(
            {"user_id": sender_id},
            {"$inc": {"coins": -cost, "total_gifts_sent": 1}}
        )

        gift_record = {
            "sender_id": sender_id,
            "sender_name": sender_name,
            "receiver_name": hedef,
            "receiver_id": None,
            "gift_name": gift_info["name"],
            "gift_emoji": gift_emoji,
            "cost": cost,
            "timestamp": "2025",
            "claimed": False
        }

        await gifts_collection.insert_one(gift_record)
        updated_sender = await get_user_data(sender_id)

        success_msg = f"""
🎉 <b>Hediye Gönderildi!</b>

{gift_emoji} <b>{sender_name}</b>, <b>@{hedef}</b> kullanıcısına <b>{gift_info['name']}</b> gönderdi!

💝 <b>Detaylar:</b>
• Hediye: {gift_emoji} {gift_info['name']}
• Fiyat: {cost} coin
• Gönderen: {sender_name}
• Alıcı: @{hedef}

💰 <b>Kalan Bakiye:</b> {updated_sender['coins']} coin
💕 <i>Aşk havada uçuşuyor!</i>
        """

        await message.reply_text(success_msg)

    except Exception as e:
        await message.reply_text(f"⚠️ <b>Hata:</b> {str(e)}")


# ───────────────────────────────
# 💕 Aşk Hikayesi Üretici
# ───────────────────────────────
@app.on_message(filters.command("hikaye", prefixes=["/", "!", "."]))
async def love_story(_, message):
    try:
        parts = message.text.split(" ", 2)
        if len(parts) < 3:
            return await message.reply_text("❌ <b>Kullanım:</b> /hikaye İsim1 İsim2\n💡 <b>Örnek:</b> /hikaye Ali Ayşe")

        isim1, isim2 = parts[1], parts[2]

        hikayeler = [
            f"Bir gün <b>{isim1}</b>, <b>{isim2}</b> ile bir kafede tanıştı ☕. Göz göze geldiler ve kader hikayelerini yazdı ❤️✨",
            f"<b>{isim1}</b> yağmur altında yürürken 🌧️, <b>{isim2}</b> şemsiyesini uzattı ☂️. O anda aşk filizlendi 🌸",
            f"<b>{isim1}</b> ve <b>{isim2}</b> aynı kitabı almak için uzandı 📚. Parmakları değdi, kalpleri ısındı 💫💕",
            f"Bir konser sırasında 🎵, <b>{isim1}</b> ve <b>{isim2}</b> aynı şarkıyı söyledi. Kalpleri aynı ritimde attı 🎶❤️",
            f"<b>{isim1}</b> parkta kuşlara yem veriyordu 🐦, <b>{isim2}</b> de katıldı. O an sessizlik bile güzelleşti 💕"
        ]

        sonlar = [
            "\n\n💕 <i>Ve sonsuza dek mutlu yaşadılar...</i>",
            "\n\n❤️ <i>Gerçek aşk her zaman yolunu bulur...</i>",
            "\n\n🌹 <i>Her aşk hikayesi güzeldir, ama onlarınki en özeldi...</i>",
        ]

        hikaye = random.choice(hikayeler) + random.choice(sonlar)
        baslik = random.choice(["💕 <b>Aşk Hikayesi</b> 💕", "🌸 <b>Romantik Hikaye</b> 🌸", "❤️ <b>Aşk Masalı</b> ❤️"])

        await message.reply_text(f"{baslik}\n\n{hikaye}")

        uid, _ = get_user_info(message)
        await update_user_coins(uid, 5)

    except Exception as e:
        await message.reply_text(f"⚠️ <b>Hata:</b> {str(e)}")


# ───────────────────────────────
# 🎁 Alınan Hediyeler
# ───────────────────────────────
@app.on_message(filters.command(["hediyem", "aldiklarim"], prefixes=["/", "!", "."]))
async def my_gifts(_, message):
    uid, username = get_user_info(message)
    await get_user_data(uid)

    gifts_received = await gifts_collection.find({"receiver_id": uid}).to_list(length=10)

    if not gifts_received:
        await message.reply_text(f"📭 <b>{username}</b>, henüz hiç hediye almadın!\n💡 Arkadaşlarından /hediyegonder ile iste 🎀")
        return

    text = f"🎁 <b>{username}’in Hediyeleri:</b>\n\n"
    for i, gift in enumerate(gifts_received, 1):
        text += f"{i}. {gift['gift_emoji']} <b>{gift['gift_name']}</b> - <b>{gift['sender_name']}</b>\n"

    toplam = await gifts_collection.count_documents({"receiver_id": uid})
    text += f"\n💝 <b>Toplam Hediye:</b> {toplam}"

    await message.reply_text(text)


# ───────────────────────────────
# 🏆 Liderlik Tablosu
# ───────────────────────────────
@app.on_message(filters.command(["liderlik", "zirve"], prefixes=["/", "!", "."]))
async def leaderboard(_, message):
    try:
        top_users = await users_collection.find().sort("coins", -1).limit(10).to_list(length=10)
        if not top_users:
            return await message.reply_text("📊 Henüz hiç kullanıcı yok!")

        text = "🏆 <b>En Zengin 10 Kullanıcı</b>\n\n"
        madalyalar = ["🥇", "🥈", "🥉"] + ["🏅"] * 7

        for i, user in enumerate(top_users):
            madalya = madalyalar[i] if i < len(madalyalar) else "🏅"
            text += f"{madalya} <b>Kullanıcı {user['user_id']}</b> — {user['coins']} coin\n"

        await message.reply_text(text)
    except Exception as e:
        await message.reply_text(f"⚠️ <b>Hata:</b> {str(e)}")


# ───────────────────────────────
# 💬 Mesajla Coin Kazan + Hediyeleri Talep Et
# ───────────────────────────────
@app.on_message(filters.text & ~filters.regex(r"^[/!.\-]"))
async def give_coins_and_claim_gifts(_, message):
    uid, username = get_user_info(message)
    await get_user_data(uid)

    # %20 ihtimalle coin kazan
    if random.randint(1, 100) <= 20:
        await update_user_coins(uid, 1)