from telethon.sync import TelegramClient
from telemongo import MongoSession
import mongoengine
import os
host = os.environ['MONGODB_HOST']
mongoengine.connect(os.environ['MONGODB_DATABASE'], host=host)
session = MongoSession(os.environ['MONGODB_DATABASE'], host=host)
api_id = os.environ['TELEGRAM_API_ID']
api_hash = os.environ['TELEGRAM_API_HASH']
client = TelegramClient(session, api_id, api_hash)
client.connect()
lonami = client.get_entity('resaqulyubi')
client.send_message(lonami.id, 'KAMU LUCUUUUUUU [BOT]')
# print(lonami.id)