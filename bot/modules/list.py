from telegram.ext import CommandHandler, run_async
from bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from bot import LOGGER, dispatcher
from bot.helper.telegram_helper.message_utils import sendMessage, editMessage
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands

@run_async
def list_drive(update,context):
    try:
        search = update.message.text.split(' ',maxsplit=1)[1]
    except IndexError:
        sendMessage('<b>➼Sᴇɴᴅ ᴀ Fɪʟᴇ Nᴀᴍᴇ As Kᴇʏᴡᴏʀᴅ Tᴏ Sᴇᴀʀᴄʜ., Aʟᴏɴɢ Wɪᴛʜ</b> <b>/list</b> <b>Cᴏᴍᴍᴀɴᴅ</b>', context.bot, update)
        return
        
    reply = sendMessage('<b>🔍Sᴇᴀʀᴄʜɪɴɢ...Pʟᴇᴀsᴇ Wᴀɪᴛ!</b>', context.bot, update)

    LOGGER.info(f"Searching: {search}")
        
    gdrive = GoogleDriveHelper(None)
    msg, button = gdrive.drive_list(search)

    editMessage(msg,reply,button)


list_handler = CommandHandler(BotCommands.ListCommand, list_drive,filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
dispatcher.add_handler(list_handler)
