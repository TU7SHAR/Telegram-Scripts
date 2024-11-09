from telethon import TelegramClient, sync
from telethon.tl.functions.messages import DeleteHistoryRequest

api_id = 'Your API ID'
api_hash = 'Your API Hash'
phone = '+919876543210' #ur number here with country code

client = TelegramClient('session_1', api_id, api_hash)

client.start(phone)

dialogs = client.get_dialogs()

for dialog in dialogs:
    if dialog.is_user:
        try:
            client(DeleteHistoryRequest(peer=dialog.entity, max_id=0))
            print(f"Deleted Chat: {dialog.name}")
        except:
            print(f"Trouble Deleting Chats")

client.disconnect()
