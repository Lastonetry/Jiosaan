import logging
import random

from jiosaavn.bot import Bot

from pyrogram import filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

logger = logging.getLogger(__name__)

# Replace these with your actual image URLs
PICS = "https://telegra.ph/file/adef46f8e7942c6b9f324.jpg"

@Bot.on_callback_query(filters.regex('^home$'))
@Bot.on_message(filters.command('start') & filters.private & filters.incoming)
async def start_handler(cient: Bot, message: Message|CallbackQuery):
    # Choose a random image URL from the PICS list
    random_pic = random.choice(PICS.split())

    text = (
        f"**ʜᴇʟʟᴏ {message.from_user.mention},\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n"
        "ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛɢ sᴘᴏᴛɪғʏ ʙᴏᴛ! "
        "ᴛʜɪs ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇᴀʀᴄʜ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢs, ᴘʟᴀʏʟɪsᴛs, ᴀʟʙᴜᴍs ᴀɴᴅ ᴀʀᴛɪsᴛs ᴅɪʀᴇᴄᴛʟʏ ғʀᴏᴍ sᴘᴏᴛɪғʏ.\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n"
        "ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ:\n"
        "- sᴇᴀʀᴄʜ ғᴏʀ sᴏɴɢs, ᴀʟʙᴜᴍs,  ᴘʟᴀʏʟɪsᴛs ᴀɴᴅ ᴀʀᴛɪsᴛs\n"
        "- ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜʀ ғᴀᴠᴏᴜʀɪᴛᴇ ᴛʀᴀᴄᴋ ᴅɪʀᴇᴄᴛʟʏ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ\n"
        "- ᴇxᴘʟᴏʀᴇ ᴠᴀʀɪᴏᴜs ғᴇᴀᴛᴜʀᴇs ᴛᴀɪʟᴏʀᴇᴅ ᴛᴏ ᴇɴʜᴀɴᴄᴇ ʏᴏᴜʀ ᴍᴜsɪᴄ ᴇxᴘᴇʀɪᴇɴᴄᴇ**\n\n"
        "**© ᴅᴇᴠ : __[ᴍᴏɢɢᴇʀ ᴋɪɴɢ](https://t.me/MoggerKing)__**"
    )

    buttons = [[
        InlineKeyboardButton('🧑‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/MoggerKing'),
        InlineKeyboardButton('♻️ ᴀʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton('💥 ʜᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('sᴇᴛᴛɪɴɢs ⚙', callback_data='settings')
        ],[
        InlineKeyboardButton('sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🌐', url='https://t.me/MoggerKing')
    ]]
    if isinstance(message, Message):
        await message.reply_photo(
            photo=random_pic,
            caption=text,
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
    else:
        await message.message.edit_media(
            media=random_pic,
            caption=text,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

@Bot.on_callback_query(filters.regex('^help$'))
@Bot.on_message(filters.command('help') & filters.private & filters.incoming)
async def help_handler(client: Bot, message: Message | CallbackQuery):
    text = (
        "**ɪᴛ's ᴠᴇʀʏ sɪᴍᴘʟᴇ ᴛᴏ ᴜsᴇ ᴍᴇ! 😉**\n\n"
        "**1. sᴛᴀʀᴛ ʙʏ ᴄᴏɴғɪɢᴜʀɪɴɢ ʏᴏᴜʀ ᴘʀᴇғᴇʀᴇɴᴄᴇs ᴜsɪɴɢ ᴛʜᴇ `/settings` ᴄᴏᴍᴍᴀɴᴅ.\n"
        "2. sᴇɴᴅ ᴍᴇ ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴀ sᴏɴɢ, ᴘʟᴀʏʟɪsᴛ, ᴀʟʙᴜᴍ ᴏʀ ᴀʀᴛɪsᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴀʀᴄʜ ғᴏʀ.\n"
        "3. ɪ'ʟʟ ʜᴀɴᴅʟᴇ ᴛʜᴇ ʀᴇsᴛ ᴀɴᴅ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴡɪᴛʜ ᴛʜᴇ ʀᴇsᴜʟᴛs!\n\n"
        "ғᴇᴇʟ ғʀᴇᴇ ᴛᴏ ᴇxᴘʟᴏʀᴇ ᴀɴᴅ ᴇɴᴊᴏʏ ᴛʜᴇ ᴍᴜsɪᴄ! <3 ❣️**"
    )

    buttons = [[
        InlineKeyboardButton('♻️ ᴀʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('sᴇᴛᴛɪɴɢs ⚙', callback_data='settings')
        ],[
        InlineKeyboardButton('ʜᴏᴍᴇ 🏠', callback_data='home'),
        InlineKeyboardButton('ᴄʟᴏsᴇ ❌', callback_data='close')
    ]]

    if isinstance(message, Message):
        await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await message.message.edit(text, reply_markup=InlineKeyboardMarkup(buttons))

@Bot.on_callback_query(filters.regex('^about$'))
@Bot.on_message(filters.command('about') & filters.private & filters.incoming)
async def about(client: Bot, message: Message|CallbackQuery):
    me = await client.get_me()

    text = (
        f"**🤖 ᴍʏ ɴᴀᴍᴇ:** {me.mention()}\n\n"
        "**📝 ʟᴀɴɢᴜᴀɢᴇ:** [Python 3](https://www.python.org/)\n\n"
        "**🧰 ғʀᴀᴍᴇᴡᴏʀᴋ:** [Pyrogram](https://github.com/pyrogram/pyrogram)\n\n"
        "**👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ:** [ᴍᴏɢɢᴇʀ ᴋɪɴɢ](https://t.me/MoggerKing)\n\n"
        "**🔗 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ: ᴘʀɪᴠᴀᴛᴇ ᴘʀᴏᴊᴇᴄᴛ! ʙᴜᴛ ɪғ ʏᴏᴜ ᴡᴀɴɴᴀ ʙᴜʏ, ᴘɪɴɢ ᴍᴇ ʜᴇʀᴇ** @MoggerKing\n\n"
    )

    buttons = [[
        InlineKeyboardButton('💥 ʜᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('sᴇᴛᴛɪɴɢs ⚙', callback_data='settings')
        ],[
        InlineKeyboardButton('ʜᴏᴍᴇ 🏠', callback_data='home'),
        InlineKeyboardButton('ᴄʟᴏsᴇ ❌', callback_data='close')
    ]]
    if isinstance(message, Message):
        await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True, quote=True)
    else:
        await message.message.edit(text, reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

@Bot.on_callback_query(filters.regex('^close$'))
async def close_cb(client: Bot, callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    await callback.message.reply_to_message.delete()
