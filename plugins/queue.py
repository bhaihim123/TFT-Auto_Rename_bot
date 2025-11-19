from pyrogram import Client, filters
from utils import check_verification, get_token
from config import VERIFY, VERIFY_TUTORIAL, BOT_USERNAME
from pyrogram.errors import FloodWait
from pyrogram.types import (
    InlineKeyboardButton,
    InputMediaDocument,
    InlineKeyboardMarkup,
    ForceReply,
    CallbackQuery,
    Message,
    InputMediaPhoto,
)
from plugins.file_rename import auto_rename_files
from helper.database import TFTBOTS
from config import *
import os
import time
import re
import subprocess
import asyncio
from datetime import datetime

queue = {}  # Dictionary to manage user queues
pending_tokens = {}


@Client.on_message(filters.private & (filters.document | filters.video | filters.audio))
async def handle_document(client: Client, message: Message):
    global queue_size
    user_id = message.from_user.id
    if TOKEN_VERIFY:
        is_verified = await check_verification(client, message.from_user.id)
        if not is_verified:
            message.delete()
            if user_id in pending_tokens:
                verification_url = pending_tokens[user_id]
            else:

                verification_url = await get_token(client, message.from_user.id, f"https://t.me/{BOT_USERNAME}?start=")
                pending_tokens[user_id] = verification_url
            await message.reply_text(
             f"<blockquote>⚠️You need to verify your account before you can use The Bot⚡. \n\n Please verify your account using the following link👇 \n\n If You Verify You Can use Our Bot without any limit for {USER_LIMIT_TIME} hour 💫</blockquote>",
             reply_markup=InlineKeyboardMarkup([
                 [InlineKeyboardButton('🔗 Verify Now ☘️', url=verification_url)]
              ])
          )
        return
    
    _bool_queue = await TFTBOTS.get_queue(user_id)
    if _bool_queue:

        if user_id not in queue:
            queue[user_id] = {"messages": [], "queue_size": 0}
    
        # Add the message to the user's queue
        queue[user_id]["messages"].append(message)
    
        if len(queue[user_id]["messages"]) > 1:
            queue[user_id]["queue_size"] += 1
            await message.reply_text(text=f"<blockquote>File added to Queue ✅ </blockquote>\n Position:{queue[user_id]['queue_size']}")
    
        if len(queue[user_id]["messages"]) == 1:
            await process_queue(client, user_id)
    else:
        await auto_rename_files(client, message)
    
    

async def process_queue(client, user_id):
    while queue.get(user_id) and queue[user_id]["messages"]:
        msg = queue[user_id]["messages"][0]
        await auto_rename_files(client, msg)
        queue[user_id]["messages"].pop(0)
        if queue[user_id]["queue_size"]>0:
            queue[user_id]["queue_size"] -= 1
        await asyncio.sleep(2)  # Short delay between tasks


@Client.on_message(filters.private & filters.command("clear_queue"))
async def clear_entire_queue(client: Client, message: Message):
    user_id = message.from_user.id

    if user_id in queue and queue[user_id]["messages"]:
        if len(queue[user_id]["messages"]) >=1:
            queue[user_id]["messages"].clear()   # Clear messages
            queue[user_id]["queue_size"] = 0      # Reset queue size
            await message.reply_text("✅ All files in your queue have been cleared!")
        else:
            await message.reply_text("Failed to clear the queue")
    else:
        await message.reply_text("⚠️ Your queue is already empty.")

@Client.on_message(filters.private & filters.command("clear"))
async def clear_one_queue(client: Client, message: Message):
    user_id = message.from_user.id
    try:
        index = int(message.text.split(" ")[1])  # convert to int
    except (IndexError, ValueError):
        await message.reply_text("⚠️ Please provide a valid index number! Example: `/clear 2`", parse_mode="markdown")
        return

    if user_id in queue and queue[user_id]["messages"]:
        if 0 <= index < len(queue[user_id]["messages"]):
            queue[user_id]["messages"].pop(index)
            queue[user_id]["queue_size"] -= 1  # Decrease queue size manually
            await message.reply_text(f"✅ File at position {index} has been removed from your queue!")
        else:
            await message.reply_text(f"⚠️ No file at position {index}. Your queue has {len(queue[user_id]['messages'])} files.")
    else:
        await message.reply_text("⚠️ Your queue is already empty.")
