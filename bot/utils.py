# bot/utils.py
import json
import asyncio
import random
from telethon import TelegramClient
from bot.config import api_id, api_hash, session_name, groups_file
from bot.messages import message_list

async def send_to_all_groups(client):
    # Load all groups from JSON file
    with open(groups_file, "r", encoding="utf-8") as f:
        groups = json.load(f)

    message_to_post = random.choice(message_list)

    for group in groups["groups"]:
        try:
            await client.send_message(group["id"], message_to_post)
            print(f"✅ Sent to {group['name']}")
        except Exception as e:
            print(f"⚠️ Failed to send to {group['name']}: {e}")
            await asyncio.sleep(5)  # short delay to avoid rate limits
