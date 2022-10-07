from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re


API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
STRING = os.environ.get("STRING", None) 
MONGO_URL = os.environ.get("MONGO_URL", None)


bot = Client(STRING, API_ID, API_HASH)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]


@bot.on_message(filters.command("Hii"))
async def start(client, message):
        await message.reply_text("ᴇʟʟᴏ ᴍᴀɪɴ sᴜᴋᴜɴ ʜᴏ ᴀᴀᴘ ᴋᴏɴ ʜᴏ ᴀᴜʟ ᴍsɢ ᴋʏᴜ ᴋᴀʟ ʟᴀʜᴇ ʜᴏ")


@bot.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    TeamSukunAIdb = MongoClient(MONGO_URL)
    TeamSukunAI = TeamSukunAIdb["TeamSukunAIDb"]["TeamSukunAI"] 
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                "ᴜʜ ᴀᴅᴍɪɴ ɴᴏɪ ʜᴏᴛɪ"
            )
    is_TeamSukunAI = TeamSukunAI.find_one({"chat_id": message.chat.id})
    if not is_TeamSukunAI:
        TeamSukunAI.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"ᴏᴏʏᴇ ᴄʜᴀᴛʙᴏᴛ ᴅɪsᴀʙʟᴇᴅ ʜᴏ ɢʏᴀ ʏᴀᴀʟ!\n @TeamSukun")
    if is_TeamSukunAI:
        await message.reply_text(f"ᴄʜᴀᴛʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ ʜ ʏᴀᴀʟ")


@bot.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    TeamSukunAIdb = MongoClient(MONGO_URL)  
    TeamSukunAI = TeamSukunAIdb["TeamSukunAIDb"]["TeamSukunAI"] 
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "ᴜʜ ᴀᴅᴍɪɴ ɴᴏɪ ʜᴏɪ."
            )
    is_TeamSukunAI = TeamSukunAI.find_one({"chat_id": message.chat.id})
    if not is_TeamSukunAI:
        await message.reply_text(f"ᴏᴏʏᴇ ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ ʜᴏ ɢʏᴀ ʏᴀᴀʟ!\n @TeamSukun")
    if is_TeamSukunAI:
        TeamSukunAI.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"ᴄʜᴀᴛʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ ʜ ʏᴀᴀʟ")


@bot.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**Usage:**\n/chatbot [on|off] only group")




























































































































































































































