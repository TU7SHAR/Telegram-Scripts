from telethon import TelegramClient, sync
from telethon.tl.functions.channels import LeaveChannelRequest

# u can get api hash and api id from here https://my.telegram.org/apps
api_id = 'Your API ID'
api_hash = 'Your API Hash'
phone = '+919876543210' #ur number here with country code

client = TelegramClient('session_1', api_id, api_hash)

client.start(phone)

dialogs = client.get_dialogs()
found_groups_or_channels = False  

for dialog in dialogs:
    if dialog.is_channel:
        found_groups_or_channels = True  # Set the flag if a channel is found
        try:
            client(LeaveChannelRequest(dialog.entity))
            print(f"Successfully left: {dialog.name}")
        except:
            print(f"Failed to leave {dialog.name}")
if not found_groups_or_channels:
    print("You are not a member of any groups or channels.")

client.disconnect()
