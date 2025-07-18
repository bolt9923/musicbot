from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("𝕮ʜᴀᴛ𝕲𝕻𝕿", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("♓ɪ💲ᴛᴏʀʏ", callback_data="mplus HELP_History"),InlineKeyboardButton("R̶ᴇ̶ᴇ̶ʟ̶ ☜(`o´)", callback_data="mplus HELP_Reel")],
    [InlineKeyboardButton("𝖙𝖆𝖌 𝖆𝖑𝖑✍", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("𝕴ɴꜰᴏ✍", callback_data="mplus HELP_Info"),InlineKeyboardButton("𝕰𝖝ᴛʀᴀ😍", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("💞💘ᴄᴏᴜᴘʟᴇꜱ💔💏", callback_data="mplus HELP_Couples"),
    InlineKeyboardButton("♥A♥ᴄᴛɪᴏɴ", callback_data="mplus HELP_Action"),InlineKeyboardButton("𝕾ᴇᴀʀᴄʜ✍", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("◦•●◉✿ ғ̴ᴏ̴ɴ̴ᴛ̴ ✿◉●•◦", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("𓂀 𝔅ᴏᴛ𝔰 𓂀", callback_data="mplus HELP_Bots"),InlineKeyboardButton("••÷[ Ⓣ-ɢʀᴀᴘʜ ]÷••", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("꧁ད S̴ᴏ̴ᴜ̴ʀ̴ᴄ̴ᴇ̴ ཌ꧂", callback_data="mplus HELP_Source"),
    InlineKeyboardButton(".•♫•♬• Tʀᴜᴛʜ-ᗪᴀʀᴇ •♬•♫•.", callback_data="mplus HELP_TD"),InlineKeyboardButton("✌𝓠ᴜɪᴢ✌", callback_data="mplus HELP_Quiz")], 
    [InlineKeyboardButton("♪·¯·♫¸¸ ᴛᴛ𝓼¸¸♫·¯·♪", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("🥂🍸 𝓡ᴀᴅɪᴏ 🍻🍷", callback_data="mplus HELP_Radio"),InlineKeyboardButton("•´¯`•. ǫ♥ᴜ♥ᴏ♥ᴛ♥ʟ♥ʏ .•´¯`•", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("◁", callback_data=f"settings_back_helper"),
     InlineKeyboardButton("↻ ʙᴀᴄᴋ ↻", callback_data=f"mbot_cb"), 
    InlineKeyboardButton("▷", callback_data=f"managebot123 settings_back_helper"),
    ]]
