"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/85bc42603249760a19746.jpg"
pm_caption = "▀▄▀▄▀▄`devil IS:` **ONLINE**▄▀▄▀▄▀\n\n"
pm_caption += "**ιғ υ мεss ωιтн мε   ι ωιℓℓ ∂εғιηιтεℓү ∂εsтяσү үσυ**\n"
pm_caption += "**🆆🅷🅰🆃 🅳🅾🅴🆂🅽'🆃 🅺🅸🅻🅻 🆄 🅼🅰🅺🅴 🆄 🅼🅾🆁🅴 🆂🆃🆁🅾🅽🅶🅴🆁**\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **6.0.9**\n`Python:` **3.7.4**\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n"
pm_caption += "**Current Branch** : `master`\n"
pm_caption += "**Friday OS** : `3.14`\n"
pm_caption += "**Current Sat** : `StarkGangSat-2.25`\n"
pm_caption += f"**My OWNER** : {DEFAULTUSER} \n"
pm_caption += "**Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "**เ ɦαƭε รσ૨૨ყ / ℓเα૨ / ƒαҡε / & µ [ƭɦε ɦεℓℓ σωɳε૨]** \n \n\n"

pm_caption +=  "**License** : [MIT Licence](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n"
pm_caption += "Copyright : By [StarkGang@Github](GitHub.com/StarkGang)\n"
pm_caption += " [Deploy FridayUserbot](https://telegra.ph/FRIDAY-06-15)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
    
