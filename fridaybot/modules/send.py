import asyncio
from datetime import datetime

from fridaybot.utils import friday_on_cmd
from fridaybot.utils import sudo_cmd

fridaythumb = "./resources/IMG_20201108_160133_369-1.jpg"


@friday.on(friday_on_cmd(pattern="send ?(.*)"))
@friday.on(sudo_cmd(pattern="send ?(.*)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    the_plugin_file = "./fridaybot/modules/{}.py".format(input_str)
    end = datetime.now()
    (end - start).seconds
    men = f"Plugin Name - {input_str}.py \nUploaded By Friday"
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        thumb=fridaythumb,
        caption=men,
        force_document=True,
        allow_cache=False,
        reply_to=message_id,
    )
    await asyncio.sleep(5)
    await event.delete()
