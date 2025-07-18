import os 
import random
from datetime import datetime 
from telegraph import upload_file
from PIL import Image , ImageDraw
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import *

#BOT FILE NAME
from BrandrdXMusic import app as app
from BrandrdXMusic.mongo.couples_db import _get_image, get_couple

POLICE = [
    [
        InlineKeyboardButton(
            text="ᴍʏ ᴄᴜᴛᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ  🥀",
            url=f"https://t.me/SEXYSHINU",
        ),
    ],
]


def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(" ")
    return dt_list
    

def dt_tom():
    a = (
        str(int(dt()[0].split("/")[0]) + 1)
        + "/"
        + dt()[0].split("/")[1]
        + "/"
        + dt()[0].split("/")[2]
    )
    return a

tomorrow = str(dt_tom())
today = str(dt()[0])

@app.on_message(filters.command("couples"))
async def ctest(_, message):
    cid = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply_text("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs.")
    try:
     #  is_selected = await get_couple(cid, today)
     #  if not is_selected:
         msg = await message.reply_text("𝐑𝐔𝐀𝐊 𝐉𝐀𝐎 𝐉𝐎𝐃𝐈 𝐁𝐀𝐍𝐀 𝐑𝐀𝐇𝐄 
(☞ ͡° ͜ʖ ͡°)☞( ˘ ³˘)(☞ ͡° ͜ʖ ͡°)☞( ˘ ³˘)
𝐀𝐀𝐏 𝐊𝙸 𝐊𝚈𝚊 𝐉𝙾𝙳𝙸 𝑩𝙰𝙽𝙴𝙶𝙸  𓆉︎

𝐀𝙿𝙿 𝙺𝙴 𝙻𝙰𝚈𝙰𝙺 𝙺𝙾𝙸 𝙿𝙰𝙸𝙳𝙰 𝙽𝙰 𝙷𝚄𝙰❤️❤️❤️❤️❤️

               𝐘𝐎𝐔 (tg://settings/))❣️ + 𝐋𝐎𝐕𝐄 (https://t.me/rarehosterbot?startgroup=true)❣️
                
      𝐒𝐎𝐎𝐍 𝐌𝐈𝐋𝐄𝐆𝐈  𝐀𝐀𝐂𝐇𝐈 𝐌𝐈𝐋𝐄𝐆𝐈 (https://t.me/rarehosterbot) 100%...")
         #GET LIST OF USERS
         list_of_users = []

         async for i in app.get_chat_members(message.chat.id, limit=50):
             if not i.user.is_bot:
               list_of_users.append(i.user.id)

         c1_id = random.choice(list_of_users)
         c2_id = random.choice(list_of_users)
         while c1_id == c2_id:
              c1_id = random.choice(list_of_users)


         photo1 = (await app.get_chat(c1_id)).photo
         photo2 = (await app.get_chat(c2_id)).photo
 
         N1 = (await app.get_users(c1_id)).mention 
         N2 = (await app.get_users(c2_id)).mention
         
         try:
            p1 = await app.download_media(photo1.big_file_id, file_name="pfp.png")
         except Exception:
            p1 = "BrandrdXMusic/assets/Upic.png"
         try:
            p2 = await app.download_media(photo2.big_file_id, file_name="pfp1.png")
         except Exception:
            p2 = "BrandrdXMusic/assets/upic.png"
            
         img1 = Image.open(f"{p1}")
         img2 = Image.open(f"{p2}")

         img = Image.open("BrandrdXMusic/assets/cppicbranded.jpg")

         img1 = img1.resize((437,437))
         img2 = img2.resize((437,437))

         mask = Image.new('L', img1.size, 0)
         draw = ImageDraw.Draw(mask) 
         draw.ellipse((0, 0) + img1.size, fill=255)

         mask1 = Image.new('L', img2.size, 0)
         draw = ImageDraw.Draw(mask1) 
         draw.ellipse((0, 0) + img2.size, fill=255)


         img1.putalpha(mask)
         img2.putalpha(mask1)

         draw = ImageDraw.Draw(img)

         img.paste(img1, (11, 16), img1)
         img.paste(img2, (78, 16), img2)

         img.save(f'test_{cid}.png')
    
         TXT = f"""
**ᴛᴏᴅᴀʏ's ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ :

{N1} + {N2} = 💚

ɴᴇxᴛ ᴄᴏᴜᴘʟᴇs ᴡɪʟʟ ʙᴇ sᴇʟᴇᴄᴛᴇᴅ ᴏɴ {tomorrow} !!**
"""
    
         await message.REPLY (f"test_{cid}.png", caption=TXT, reply_markup=InlineKeyboardMarkup(POLICE),
    )
         await msg.delete()
         a = upload_file(f"test_{cid}.png")
         for x in a:
           img = "https://files.catbox.moe/ms7xee.jpg" + x
           couple = {"c1_id": c1_id, "c2_id": c2_id}
          # await save_couple(cid, today, couple, img)
    
         
      # elif is_selected:
      #   msg = await message.reply_text("𝐑𝐔𝐀𝐊 𝐉𝐀𝐎 𝐉𝐎𝐃𝐈 𝐁𝐀𝐍𝐀 𝐑𝐀𝐇𝐄 
(☞ ͡° ͜ʖ ͡°)☞( ˘ ³˘)(☞ ͡° ͜ʖ ͡°)☞( ˘ ³˘)
𝐀𝐀𝐏 𝐊𝙸 𝐊𝚈𝚊 𝐉𝙾𝙳𝙸 𝑩𝙰𝙽𝙴𝙶𝙸  𓆉︎

𝐀𝙿𝙿 𝙺𝙴 𝙻𝙰𝚈𝙰𝙺 𝙺𝙾𝙸 𝙿𝙰𝙸𝙳𝙰 𝙽𝙰 𝙷𝚄𝙰❤️❤️❤️❤️❤️

               𝐘𝐎𝐔 (tg://settings/))❣️ + 𝐋𝐎𝐕𝐄 (https://t.me/rarehosterbot?startgroup=true)❣️
                
      𝐒𝐎𝐎𝐍 𝐌𝐈𝐋𝐄𝐆𝐈  𝐀𝐀𝐂𝐇𝐈 𝐌𝐈𝐋𝐄𝐆𝐈 (https://t.me/rarehosterbot) 100%...")
      #   b = await _get_image(cid)
       #  c1_id = int(is_selected["c1_id"])
       #  c2_id = int(is_selected["c2_id"])
       #  c1_name = (await app.get_users(c1_id)).first_name
        # c2_name = (await app.get_users(c2_id)).first_name
         
      #   TXT = f"""
#**ᴛᴏᴅᴀʏ's sᴇʟᴇᴄᴛᴇᴅ ᴄᴏᴜᴘʟᴇs 🎉 :
#➖➖➖➖➖➖➖➖➖➖➖➖
#[{c1_name}](tg://openmessage?user_id={c1_id}) + [{c2_name}](tg://openmessage?user_id={c2_id}) = ❣️
#➖➖➖➖➖➖➖➖➖➖➖➖
#ɴᴇxᴛ ᴄᴏᴜᴘʟᴇꜱ ᴡɪʟʟ ʙᴇ ꜱᴇʟᴇᴄᴛᴇᴅ ᴏɴ {tomorrow} !!**
#"""
 #        await message.(b, caption=TXT)
        # await msg.delete()
    except Exception as e:
        print(str(e))
    try:
      os.remove(f"./downloads/pfp.png")
      os.remove(f"./downloads/pfp.png")
      os.remove(f"test_{cid}.png")
    except Exception:
       pass
         

__mod__ = "COUPLES"
__help__ = """
**» /couples** - Get Todays Couples Of The Group In Interactive View
"""





    




    
