from telethon import TelegramClient, sync
from telethon.tl.functions.channels import LeaveChannelRequest

api_id = '26786589'
api_hash = '1cfda34fc9fb52eef23c5a448d1ec09a'
phone = '+919780400311'

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
