from telethon.sync import TelegramClient
from telemongo import MongoSession
import mongoengine
import os
from decouple import config
import wget
host = os.getenv('MONGODB_HOST',config('MONGODB_HOST'))
mongoengine.connect(os.getenv('MONGODB_DATABASE',config('MONGODB_DATABASE')), host=host)
session = MongoSession(os.getenv('MONGODB_DATABASE',config('MONGODB_DATABASE')), host=host)
api_id = os.getenv('TELEGRAM_API_ID',config('TELEGRAM_API_ID'))
api_hash = os.getenv('TELEGRAM_API_HASH',config('TELEGRAM_API_HASH'))
client = TelegramClient(session, api_id, api_hash)
client.connect()
lonami = client.get_entity(os.getenv('SEND_TO',config('SEND_TO')))
wget.download("https://covid19.mathdro.id/api/og",out="panda.jpg")
client.send_file(lonami.id, 'panda.jpg', caption="PLEASE STAY HOMEEEEEEEEEEE")
os.remove("panda.jpg")

