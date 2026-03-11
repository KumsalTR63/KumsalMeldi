import asyncio
import random
from datetime import datetime, timedelta
from pyrogram import filters
from pyrogram.types import Message
from AloneMusic import app  # Assuming this is the bot's app instance
from AloneMusic.core.mongo import mongodb   # ✅ MongoDB connection

db = mongodb.games  # Accessing the 'games' collection from MongoDB
initial_balance = 25000  # Initial balance for users

# 🔹 Retrieve user balance
async def get_balance(user_id: int) -> int:
    user = await db.find_one({"_id": user_id})
    if user:
        return user.get("balance", initial_balance)
    return initial_balance

# 🔹 Update user balance
async def update_balance(user_id: int, amount: int):
    current_balance = await get_balance(user_id)
    new_balance = max(current_balance + amount, 0)  # Prevent negative balance
    await db.update_one(
        {"_id": user_id},
        {"$set": {"balance": new_balance}},
        upsert=True,
    )
    return new_balance

# 🎰 Slot game
@app.on_message(filters.command("cash") & filters.group)
async def play_slot(_, message: Message):
    user_id = message.from_user.id
    if len(message.command) < 2:
        return await message.reply("Kullanım: /cash [miktar] [opsiyonel çarpan] 🎰")

    try:
        amount = int(message.command[1])
        multiplier = 1
        if len(message.command) > 2 and message.command[2].endswith("x"):
            multiplier = int(message.command[2][:-1])
            if multiplier < 1 or multiplier > 6:
                return await message.reply("Çarpan 1x ile 6x arası olmalı.")
    except:
        return await message.reply("Geçerli bir miktar giriniz. Örnek: /cash 50 2x")

    balance = await get_balance(user_id)
    if amount > balance:
        return await message.reply("Bakiyeniz yetersiz. 😢")

    win_amount = amount * multiplier if random.random() < 0.5 else -amount * multiplier
    new_balance = await update_balance(user_id, win_amount)
    result = "kazandınız 🎉" if win_amount > 0 else "kaybettiniz 🥹"

    await message.reply(
        f"{win_amount} TL {result}!\n💰 Güncel bakiyeniz: {new_balance} TL"
    )

# 🏀 Basketball game
@app.on_message(filters.command("bcash") & filters.group)
async def play_basket(_, message: Message):
    user_id = message.from_user.id
    if len(message.command) < 2:
        return await message.reply("Kullanım: /bcash [miktar] [opsiyonel çarpan] 🏀")

    try:
        amount = int(message.command[1])
        multiplier = 1
        if len(message.command) > 2 and message.command[2].endswith("x"):
            multiplier = int(message.command[2][:-1])
            if multiplier < 1 or multiplier > 6:
                return await message.reply("Çarpan 1x ile 6x arası olmalı.")
    except:
        return await message.reply("Geçerli bir miktar giriniz.")

    balance = await get_balance(user_id)
    if amount > balance:
        return await message.reply("Bakiyeniz yetersiz.")

    dice = await app.send_dice(message.chat.id, emoji="🏀")
    await asyncio.sleep(3)

    if dice.dice.value >= 4:
        win_amount = amount * multiplier
        text = f"🏀 Tebrikler! Potaya girdi. +{win_amount} TL"
    else:
        win_amount = -amount * multiplier
        text = f"🏀 Üzgünüm, kaçırdınız. {amount * multiplier} TL kaybettiniz."

    new_balance = await update_balance(user_id, win_amount)
    await message.reply(f"{text}\n💰 Güncel bakiyeniz: {new_balance} TL")

# ⚽ Football game
@app.on_message(filters.command("fcash") & filters.group)
async def play_football(_, message: Message):
    user_id = message.from_user.id
    if len(message.command) < 2:
        return await message.reply("Kullanım: /fcash [miktar] [opsiyonel çarpan] ⚽")

    try:
        amount = int(message.command[1])
        multiplier = 1
        if len(message.command) > 2 and message.command[2].endswith("x"):
            multiplier = int(message.command[2][:-1])
            if multiplier < 1 or multiplier > 6:
                return await message.reply("Çarpan 1x ile 6x arası olmalı.")
    except:
        return await message.reply("Geçerli bir miktar giriniz.")

    balance = await get_balance(user_id)
    if amount > balance:
        return await message.reply("Bakiyeniz yetersiz.")

    dice = await app.send_dice(message.chat.id, emoji="⚽")
    await asyncio.sleep(3)

    if dice.dice.value >= 3:
        win_amount = amount * multiplier
        text = f"⚽ Gooool! +{win_amount} TL"
    else:
        win_amount = -amount * multiplier
        text = f"⚽ Kaçırdınız. {amount * multiplier} TL kaybettiniz."

    new_balance = await update_balance(user_id, win_amount)
    await message.reply(f"{text}\n💰 Güncel bakiyeniz: {new_balance} TL")

# 💰 Check balance
@app.on_message(filters.command("bakiye"))
async def check_balance(_, message: Message):
    user_id = message.from_user.id
    balance = await get_balance(user_id)
    await message.reply(f"Güncel bakiyeniz: {balance} TL 💰")

# 🎁 Daily bonus
@app.on_message(filters.command(["gunluk", "günlük"]))
async def daily_bonus(_, message: Message):
    user_id = message.from_user.id
    now = datetime.utcnow()

    user = await db.find_one({"_id": user_id})
    last_bonus = user.get("last_bonus") if user else None

    if last_bonus and now - last_bonus < timedelta(hours=5):
        return await message.reply("Günlük bonus için biraz daha bekle ⏳")

    await db.update_one(
        {"_id": user_id},
        {"$inc": {"balance": 50000}, "$set": {"last_bonus": now}},
        upsert=True,
    )

    balance = await get_balance(user_id)
    await message.reply(f"🎁 Günlük bonus aldınız: 50.000 TL\n💰 Güncel bakiyeniz: {balance} TL")

# 🏆 Rich List
@app.on_message(filters.command("zenginler"))
async def rich_list(_, message: Message):
    cursor = db.find().sort("balance", -1).limit(10)
    users = await cursor.to_list(length=10)

    if not users:
        return await message.reply("Henüz hiç kullanıcı oynamadı.")

    text = "💰 **Zenginler Listesi:**\n\n"
    for i, user in enumerate(users, start=1):
        try:
            tg_user = await app.get_users(user["_id"])
            name = tg_user.first_name
        except:
            name = f"User-{user['_id']}"
        text += f"{i}. {name} — {user['balance']} TL\n"

    await message.reply(text)