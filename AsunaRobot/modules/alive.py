from telethon import events, Button, custom
import re, os
from MashaRoBot.events import register
from MashaRoBot import telethn as tbot
from MashaRoBot import telethn as tgbot
PHOTO = "https://te.legra.ph/file/ee53c5046a47560e358ce.jpg"
@register(pattern=("/alive"))
async def awake(event):
  LOVELY = event.sender.first_name
  LOVELY = "**♡ I,m Lovely💕** \n\n"
  LOVELY += "**♡ I'm Working with awesome speed**\n\n"
  LOVELY += "**♡ Lovely : 2.0 LATEST**\n\n"
  LOVELY += "**♡ My Creator :** [𝗧𝗨𝗦𝗛𝗔𝗥😍](t.me/D3VILRAVANXOP)\n\n"
  LOVELY += "**♡ Telethon Version : 1.23.0**\n\n"
  BUTTON = [[Button.url("𝐒𝐔𝐏𝐏𝐎𝐑𝐓🙂", "https://t.me/STACY_SUPPORT"), Button.url("𝐔𝐏𝐃𝐀𝐓𝐄", "https://t.me/STACY_UPDATES")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LOVELY,  buttons=BUTTON)
