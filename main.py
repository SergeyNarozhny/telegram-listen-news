# default to python3.5+
import asyncio

# pip3 install telethon
from telethon import TelegramClient, events

config = {
    # Use Safari and get this info from my.telegram.org
    'api_id': 123,
    'api_hash': 'eee'
}
telegram_channels = {
    # You have to be subscribed for these channels!
    'from': [
        {
            'short_name': 'rbc_news',
            'channel_id': -1001099860397 # use @username_to_id_bot to fetch ids
        },
        {
            'short_name': 'markettwits',
            'channel_id': -1001203560567
        }
    ],
    'to': {
        'channel_id': -1002109687587 # @sdfsodifsdfsdf
    }
}
listen_channels = [ch['channel_id'] for ch in telegram_channels["from"]]

# TelegramClient has to sign in with this OR you need to remove .session file
with TelegramClient('telegram_listen_news_app_me', config['api_id'], config['api_hash']) as client:
    @client.on(events.NewMessage(chats=list(listen_channels)))
    async def get_message_handler(event):
        channel_username = event.message.chat.username
        msg = f'<b>Forwarded from <i>{channel_username}</i></b>: {event.raw_text}'
        await client.send_message(
            entity=telegram_channels['to']['channel_id'],
            parse_mode='html', link_preview=False, message=msg
        )
    client.run_until_disconnected()
