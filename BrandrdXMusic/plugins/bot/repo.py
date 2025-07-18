from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from BrandrdXMusic import app

BOT_USERNAME = "heer_chatbot"

start_txt = """**
✪ 𝐊𝐇𝐔𝐃 𝐁𝐀𝐍𝐀 𝐁𝐇𝐎𝐒𝐃𝐈𝐊𝐄 ✪
 
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
     
            [ 
            InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙᴇs✪", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/thikhaisamjhgya"),
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/+7h61ibzWCWY5NTc1"),
             ],
     
             [
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/+7h61ibzWCWY5NTc1"),
             ],
     
              ]
 
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_video(
        video="https://envs.sh/ozv.mp4",
        caption=start_txt,
        reply_markup=reply_markup
    )
