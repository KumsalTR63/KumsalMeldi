import requests
from pyrogram import filters

from AloneMusic import app


@app.on_message(filters.command(["ig", "instagram", "reel"]))
async def download_instagram_video(client, message):
    if len(message.command) < 2:
        await message.reply_text(
            "Lütfen komuttan sonra bir Instagram reel bağlantısı giriniz."
        )
        return
    a = await message.reply_text("İşleniyor...")
    url = message.text.split()[1]
    api_url = (
        f"https://nodejs-1xn1lcfy3-jobians.vercel.app/v2/downloader/instagram?url={url}"
    )

    response = requests.get(api_url)
    data = response.json()

    if data["status"]:
        video_url = data["data"][0]["url"]
        await a.delete()
        await client.send_video(message.chat.id, video_url)
    else:
        await a.edit("Reel indirilemedi ❌")


__MODULE__ = "Instagram"
__HELP__ = """
/reel [Instagram reel bağlantısı] - Bot ile reel indirir.
/ig [Instagram reel bağlantısı] - Bot ile reel indirir.
/instagram [Instagram reel bağlantısı] - Bot ile reel indirir.
"""