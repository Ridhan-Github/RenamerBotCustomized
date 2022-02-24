class Scripted(object):    

START_TEXT = """👋 ʜᴇʟʟᴏ, {} ♡

Tʜɪꜱ ɪꜱ ꜰɪʟᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ ᴡɪᴛʜ ꜰɪʟᴇ ᴄᴏɴᴠᴇʀᴛᴇʀ

Pʀᴇꜱꜱ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ...  

Pᴏᴡᴇʀᴇᴅ ʙʏ : [ᴅɪsɴᴇʏ ʙᴏᴛs](https://t.me/Disney_Bots)"""
   

    PROGRESS_DIS = """\n
╭───[**sᴛᴀᴛᴜs**]───⍟
│
├<b>🗂️ Sɪᴢᴇ : {1} | {2}</b>
│
├<b>📱 Pʀᴏɢʀᴇꜱꜱ : {0}%</b>
│
├<b>🚀 Sᴘᴇᴇᴅ : {3}/s</b>
│
├<b>⏱️ Eᴛᴀ : {4}</b>
╰─────────────────⍟"""

    HELP_TEXT = """
<b> Rᴇɴᴀᴍᴇ </b>

➠ sᴇɴᴅ ᴀ ғɪʟᴇ ᴏʀ ᴍᴇᴅɪᴀ ᴛᴏ ʀᴇᴘʟʏ /rename ғɪʟᴇ ɴᴀᴍᴇ.ᴇxᴛᴇɴsɪᴏɴ

➠ ᴍᴜsᴛ ʀᴇᴘʟʏ ғɪʟᴇ ɴᴀᴍᴇ ᴀɴᴅ ᴇxᴛᴇɴsɪᴏɴ.

<b> ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏ </b>

➠ sᴇɴᴅ ғɪʟᴇ ᴛᴏ ʀᴇᴘʟʏ /convert ɪᴛ ᴄᴏɴᴠᴇʀᴛ ᴀ ᴠɪᴅᴇᴏ ғᴏʀᴍᴀᴛ

<b> sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ </b>

➠ sᴇɴᴅ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴍᴀᴋᴇ ɪᴛ ᴀs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.

<b> ᴅᴇʟᴇᴛɪɴɢ ᴛʜᴜᴍʙɴᴀɪʟ </b>

➠ sᴇɴᴅ /delthumb ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴜᴍʙɴᴀɪʟ.

<b> sʜᴏᴡ ᴛʜᴜᴍʙɴᴀɪʟ </b>

➠ sᴇɴᴅ /showthumb ᴛᴏ ᴠɪᴇᴡ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ.
"""


    ABOUT_TEXT = """**Mʏ ɴᴀᴍᴇ :** [Rᴇɴᴀᴍᴇ ᴘʀᴏ ʙᴏᴛ](http://t.me/RenamerXProRobot)

**Cʜᴀɴɴᴇʟ :** [ᴅɪsɴᴇʏ ʙᴏᴛꜱ](https://t.me/Disney_Bots)

**Vᴇʀꜱɪᴏɴ :** [1.0 ʙᴇᴛᴀ](http://t.me/RenamerXProRobot)

**Sᴏᴜʀᴄᴇ :** [Cʟɪᴄᴋ Hᴇʀᴇ](https://t.me/tamilanbots)

**Dᴀᴛᴀʙᴀꜱᴇ :** [Mᴏɴɢᴏᴅʙ](https://www.mongodb.com/)

**Sᴇʀᴠᴇʀ :** [Hᴇʀᴏᴋᴜ](https://heroku.com/)

**Lᴀɴɢᴜᴀɢᴇ :** [Pʏᴛʜᴏɴ 3.9.5](https://www.python.org/)

**Fʀᴀᴍᴇᴡᴏʀᴋ :** [Pʏʀᴏɢʀᴀᴍ 1.4.7](https://docs.pyrogram.org/)

**Dᴇᴠᴇʟᴏᴘᴇʀ :** [𝙼𝚘𝚗𝚎𝚢𝙴𝚊𝚛𝚗𝚅𝙸𝙿](https://t.me/tamilanxbots)

**Pᴏᴡᴇʀᴇᴅ ʙʏ :** [@ᴅɪsɴᴇʏʜᴅʟɪɴᴋs](https://t.me/DisneyHDLinks)
"""

    CUSTOM_CAPTION = "<i>{}</i>"
    ACCESS_DENIED = "<i><b> sᴏʀʀʏ! ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ </b></i>"
    BANNED_USER_TEXT = "<i><b> sᴏʀʀʏ! ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ </b></i>"
    TRYING_TO_UPLOAD = "<b> ᴜᴘʟᴏᴀᴅɪɴɢ </b>"
    CURRENT_THUMBNAIL = "<i> Yᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ"
    THUMBNAIL_SAVED = "<i> Yᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ ✓ </i>"
    THUMBNAIL_DELETED = "<i> ᴛʜᴜᴍɴᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ </i>"
    NO_THUMBNAIL_FOUND = "<i> Nᴏ ᴛʜᴜᴍʙɴᴀɪʟ ꜰᴏᴜɴᴅ 😟 </i>"
    TRYING_TO_DOWNLOAD = " <b> DᴏᴡɴʟᴏᴀᴅɪɴG </b> "
    UPLOAD_SUCCESS = "<i> ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsᴇ ᴍᴇ /n/nᴊᴏɪɴ - https://t.me/DisneyBots"
    REPLY_TO_MEDIA = "<i> Rᴇᴘʟʏ ᴛᴏ ᴛʜᴀᴛ ꜰɪʟᴇ ᴡɪᴛʜ /convert ᴄᴏᴍᴍᴀɴᴅ </i>"
    UPLOAD_START = "<i> 📤 ᴜᴘʟᴏᴀᴅɪɴɢ ʏᴏᴜʀ ғɪʟᴇ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...</i>\n"
    DOWNLOAD_START = "<i> 📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ʏᴏᴜʀ ғɪʟᴇ ᴘʟᴇᴀᴄᴇ ᴡᴀɪᴛ...</i>\n"
    JOIN_NOW_TEXT = "<i> 👋 Hello, {} ♡︎ /n/nJoin my update channel to use me 🔐</i>"
    REPLY_TO_FILE = "<i> Rᴇᴘʟʏ ᴛᴏ ᴛʜᴀᴛ ꜰɪʟᴇ ᴡɪᴛʜ /rename ɴᴇᴡ ꜰɪʟᴇɴᴀᴍᴇ.ᴇxᴛᴇɴsɪᴏɴ </i>"
    CONTACT_MY_DEVELOPER = "<i></i>"
    UPGRADE_TEXT = "</i> <b>ᴛᴏ ᴜᴘɢʀᴀᴅᴇ ʏᴏᴜʀ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ᴄᴏɴᴛᴀᴄᴛ <a href='https://t.me/DisneyBots_Support'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></b></i>"
