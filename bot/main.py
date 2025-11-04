import asyncio
from telethon import TelegramClient
from bot.config import api_id, api_hash, session_name, delay_minutes
from bot.utils import send_to_all_groups

async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()
    print("🤖 Bot is running...")

    while True:
        await send_to_all_groups(client)
        print(f"⏰ Waiting {delay_minutes} minutes before next post...\n")
        await asyncio.sleep(delay_minutes * 60)  # ✅ async sleep

if __name__ == "__main__":
    asyncio.run(main())

