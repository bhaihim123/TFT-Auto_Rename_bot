from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ForceReply,
    CallbackQuery,
    Message,
)

from bot import user   # 🔥 USER SESSION (4GB+)
from PIL import Image
from datetime import datetime
from helper.utils import progress_for_pyrogram, humanbytes, convert
from helper.database import TFTBOTS
from config import Config
import os, time, re, asyncio

renaming_operations = {}

# ================= REGEX =================
pattern1 = re.compile(r'S(\d+)(?:E|EP)(\d+)', re.I)
pattern2 = re.compile(r'S(\d+)\s*(?:E|EP|-\s*EP)(\d+)', re.I)
pattern3 = re.compile(r'(?:E|EP)\s*(\d+)', re.I)
pattern4 = re.compile(r'S(\d+)[^\d]*(\d+)', re.I)
patternX = re.compile(r'(\d+)')

pattern5 = re.compile(r'(\d{3,4}p)', re.I)
pattern6 = re.compile(r'4k', re.I)
pattern7 = re.compile(r'2k', re.I)
pattern8 = re.compile(r'HdRip', re.I)

# ================= UTILS =================
def extract_episode(filename):
    for p in (pattern1, pattern2, pattern3, pattern4, patternX):
        m = p.search(filename)
        if m:
            return m.groups()[-1]
    return None

def extract_quality(filename):
    for p in (pattern5, pattern6, pattern7, pattern8):
        m = p.search(filename)
        if m:
            return m.group(0)
    return "Unknown"

# ================= MAIN =================
async def auto_rename_files(client: Client, message: Message):
    user_id = message.from_user.id
    format_template = await TFTBOTS.get_format_template(user_id)
    media_pref = await TFTBOTS.get_media_preference(user_id)

    if not format_template:
        return await message.reply_text("আগে /autorename দিয়ে format set করো")

    if message.document:
        file_name = message.document.file_name
        media_type = media_pref or "document"
        file_size = message.document.file_size
    elif message.video:
        file_name = message.video.file_name or "video.mp4"
        media_type = media_pref or "video"
        file_size = message.video.file_size
    elif message.audio:
        file_name = message.audio.file_name or "audio.mp3"
        media_type = media_pref or "audio"
        file_size = message.audio.file_size
    else:
        return

    if file_name in renaming_operations:
        return
    renaming_operations[file_name] = True

    ep = extract_episode(file_name)
    quality = extract_quality(file_name)

    if ep:
        format_template = format_template.replace("{episode}", ep)
    format_template = format_template.replace("{quality}", quality)

    _, ext = os.path.splitext(file_name)
    new_name = f"{format_template}{ext}"
    os.makedirs("downloads", exist_ok=True)
    path = f"downloads/{new_name}"

    msg = await message.reply_text("⬇️ Downloading...")

    try:
        # 🔥 DOWNLOAD WITH USER (NO 2GB LIMIT)
        await user.download_media(
            message,
            file_name=path,
            progress=progress_for_pyrogram,
            progress_args=("Downloading", msg, time.time()),
        )

        msg = await msg.edit("⬆️ Uploading...")

        caption = f"**{new_name}**\n📦 {humanbytes(file_size)}"

        # 🔥 UPLOAD WITH USER (NO 2GB LIMIT)
        if media_type == "document":
            sent = await user.send_document(
                message.chat.id,
                document=path,
                caption=caption,
                progress=progress_for_pyrogram,
                progress_args=("Uploading", msg, time.time()),
            )
        elif media_type == "video":
            sent = await user.send_video(
                message.chat.id,
                video=path,
                caption=caption,
                progress=progress_for_pyrogram,
                progress_args=("Uploading", msg, time.time()),
            )
        else:
            sent = await user.send_audio(
                message.chat.id,
                audio=path,
                caption=caption,
                progress=progress_for_pyrogram,
                progress_args=("Uploading", msg, time.time()),
            )

        await msg.delete()

        if Config.DUMB_CHANNEL:
            await sent.forward(Config.DUMB_CHANNEL)

    except FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception as e:
        await msg.edit(f"❌ Error: `{e}`")
    finally:
        if os.path.exists(path):
            os.remove(path)
        renaming_operations.pop(file_name, None)
