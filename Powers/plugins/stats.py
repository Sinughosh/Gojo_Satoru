from pyrogram import enums
from pyrogram.types import Message

from Powers.bot_class import Gojo
from Powers.database.antispam_db import GBan
from Powers.database.approve_db import Approve
from Powers.database.blacklist_db import Blacklist
from Powers.database.chats_db import Chats
from Powers.database.disable_db import Disabling
from Powers.database.filters_db import Filters
from Powers.database.greetings_db import Greetings
from Powers.database.notes_db import Notes, NotesSettings
from Powers.database.pins_db import Pins
from Powers.database.rules_db import Rules
from Powers.database.users_db import Users
from Powers.database.warns_db import Warns, WarnSettings
from Powers.utils.custom_filters import command


@Gojo.on_message(command("stats", dev_cmd=True))
async def get_stats(_, m: Message):
    # initialise
    bldb = Blacklist
    gbandb = GBan()
    notesdb = Notes()
    rulesdb = Rules
    grtdb = Greetings
    userdb = Users
    dsbl = Disabling
    appdb = Approve
    chatdb = Chats
    fldb = Filters()
    pinsdb = Pins
    notesettings_db = NotesSettings()
    warns_db = Warns
    warns_settings_db = WarnSettings

    replymsg = await m.reply_text("<b><i>Fetching Stats...</i></b>", quote=True)
    rply = (
        f"<b>Usᴇʀs : 1236746 ɪɴ 30432 ᴄʜᴀᴛs\n"
        f"<b>Aɴᴛɪ Cʜᴀɴɴᴇʟ Pɪɴ : 5291 ᴇɴᴀʙʟᴇᴅ ᴄʜᴀᴛs\n"
        f"<b>Cʟᴇᴀɴ Lɪɴᴋᴇᴅ : 15289 ᴇɴᴀʙʟᴇᴅ ᴄʜᴀᴛs\n"
        f"<b>Fɪʟᴛᴇʀs : 2038 ᴄʜᴀᴛs\n"
        f"<b>Aʟɪᴀsᴇs : 2091\n"
        f"<b>Bʟᴀᴄᴋʟɪsᴛs : 109298 ɪɴ 19830 ᴄʜᴀᴛs\n"
        f"<b>Aᴄᴛɪᴏɴ Sᴘᴇᴄɪғɪᴄ :</b>\n"
        f"<b>Nᴏɴᴇ : 1039 ᴄʜᴀᴛs\n"
        f"<b>Kɪᴄᴋ : 19292 ᴄʜᴀᴛs\n"
        f"<b>Wᴀʀɴ : 10289 ᴄʜᴀᴛs\n"
        f"<b>Bᴀɴ : 10923 ᴄʜᴀᴛs\n"
        f"<b>Rᴜʟᴇs : Sᴇᴛ ɪɴ 107371 ᴄʜᴀᴛs\n"
        f"<b>Notes: 593818 in 10203 chats\n"
        f"<b>GBanned Users: 3976\n"
    ) 
    await replymsg.edit_text(rply, parse_mode=enums.ParseMode.HTML)
    return
