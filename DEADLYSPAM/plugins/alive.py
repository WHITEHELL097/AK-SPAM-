import config
from DEADLYSPAM import BOT0, deadlyversion, SUDOERS
from telethon import events, version, Button
from telethon.tl.custom import button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_PIC = PIC
else:
    DEADLY_PIC = "https://graph.org/file/bf5ebe363845094c47512.jpg"

hl = config.CMD_HNDLR


DEADLY = "✯ Ak 𝗧𝗘𝗔𝗠 ✯\n\n"
DEADLY += f"═══════════════════\n"
DEADLY += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `4.0.0`\n"
DEADLY += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
DEADLY += f"• **ᴋɪɴɢ x ᴛᴀ ᴠᴇʀsɪᴏɴ**  : `{deadlyversion}`\n"
DEADLY += f"═══════════════════\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     Blaze = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/dil_ki_baatee"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/heart_talkz")], [Button.url("• ʀᴇᴘᴏ •", "https://te.legra.ph/file/344bd30504a44218daee7.mp4")]]
     await BOT0.send_file(event.chat_id, DEADLY_PIC, caption=DEADLY, buttons=Blaze) 
  else:
      await event.reply("**ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ᴋɪɴɢ x ᴛᴇᴀᴍ ʙʀᴀɴᴅᴇᴅ-ꜱᴘᴀᴍʙᴏᴛ!**") 
