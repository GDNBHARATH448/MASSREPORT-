import os
import time

class Config(object):
    # Pyrogram Client
    API_ID    = int(os.environ.get("API_ID", "29896633"))  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "7a8a6dd1c08f6ffc33645885bb3ecf77") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8474871278:AAF4XBwAwIaIPrD3he4r_lWT5dCCD1jWUaQ") # ⚠️ Required
    
    # Other Configs
    BOT_START_TIME = time.time()
    OWNER    = int(os.environ.get("OWNER", "5867783630"))  # ⚠️ Required
    SUDO = list(map(int, os.environ.get("SUDO", "8067478942").split()))  # ⚠️ Required
    # Web Response Config
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))

class Txt(object):

    SEND_NUMBERS_MSG = "100"
❪ SEND THE TOTAL NUMBER YOU HAVE ❫

☛ How many Number do You have
"1"

    SEND_TARGET_CHANNEL = """
( SEND THE TARGET CHANNEL LINK or USERNAME)

☛ For e.g :- <code> @ </code> or <code> https:/t.me/itzdaxx </code>
"""

    SEND_SESSION_MSG = "BQHIL7kAtPFv2Wy5bmAoCA2_Ezc_C2ZAYz_EdkqijepTX-KgXqV5nLsFRJ_LXNr9zMOXN4vt0Rt7DNOawfCKx5Ruu1N9OB3pXF9xyR5LIy2MiGKryFbvh3D4mnGTggfBIUe8jmYK1okilHo05sR-4Mzlu1xdlWOA4n4iLrUMJv8OwUMSXxcDzjeGkmq_2L3AIY-G_kM7G4zJR4cQmocjmL5PSrynxOp_TpXbiZxp7LfXv8DCcdPY-VYO-BxjnUtsqj93OhhVg-phbE-VUQQNK4Zws1KccW4w1kqhxlVba0FT2H75fFkvHgz16MRW3XmO7Gj1tfv51KFe8yrfwaL82bq8KwAAAAHg2_WeAA"
❪ SEND SESSOIN STRING ❫

☛ Generate Session String form @


"""

    SEND_API_ID = """
❪ SEND API ID ❫

☛ Api_id Get from my.telegram.org
"""
    SEND_API_HASH = """
❪ SEND API HASH ❫

☛ Api_hash Get from my.telegram.org
"""

    MAKE_CONFIG_DONE_MSG = """
Your {} accounts has been added 👥

And Logined to the Target Channel/Group to Report it. ✅

➜ Click the button bellow to see the Number of Telegram account you added.
"""

    ADDED_ACCOUNT = "1"
Your have added {} accounts 👥

➜ Click the button bellow to see the More Info of the Telegram accounts which you haved added.
"""

    ACCOUNT_INFO = """
<b> Name :- </b> <code> {0} </code>
<b> User Id :- </b> <code> {1} </code>
"""

    REPORT_CHOICE = "1"
❪ SELECT REASON FOR REPORT 👤 ❫

1. Report for child abuse
2. Report for copyrighted content
3. Report for impersonation
4. Report an irrelevant geogroup
5. Report an illegal durg
6. Report for Violence
7. Report for offensive person detail
8. Reason for Pornography
9. Report for spam

Whats your  reason: select 1-9 👇 
"""

    SEND_NO_OF_REPORT_MSG = "100"
❪ SELECT NUMBER OF REPORTS 👤 ❫

**Send Number of reports which you want to report to this @{}**

The bot will keep reporting to target channel or group until it's reach the number of report. 🎯
"""

    START_MSG = """
Hɪ {},

Tʜɪs Bᴏᴛ ɪs ғᴏʀ ᴛᴏ ʀᴇᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ᴏʀ ɢʀᴏᴜᴘ ɪɴ ᴍᴀss ʟᴇᴠᴇʟ ᴛʜʀᴏᴜɢʜ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ sᴇssɪᴏɴ sᴛʀɪɴɢ ᴡʜɪᴄʜ ʏᴏᴜ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ʙʏ @

Tʜɪs ʙᴏᴛ ɪs sᴏʟᴇʟʏ ᴄʀᴇᴀᴛᴇ ᴏʀ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ :- @itzdaxx
"""

    HELP_MSG = """
🔆 HELP

📚 Available commands:
⏣ /start - check I'm alive 
⏣ /make_config - To Make Config 
⏣ /del_config - Delete the Config
⏣ /target - To see the target channel
⏣ /see_accounts - See all the accounts you added
⏣ /add_account - Add new accounts
⏣ /report - Report the target
⏣ /restart - Restart the bot

💢 Features:
► Report a single channel or group with multiple Id's
► Type of report option available
► Facilitie to change the Target Channel or Group
► Facilitie to add the multiples accounts after once you make config
► All the accounts you added will automatically joined the target channel or group
► No need to enter phone number, password or otp just send session string and that's it
► Check the server status and resources
"""

    ABOUT_MSG = """
- 𝖬𝗒 𝖭𝖺𝗆𝖾 : <a href=https://t.me/{}>{}</a>
- 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href=@itzdaxx</a>
- 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : Pyrogram
- 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : 𝖯𝗒𝗍𝗁𝗈𝗇 𝟥
- 𝖣𝖺𝗍𝖺𝖡𝖺𝗌𝖾 : 𝖬𝗈𝗇𝗀𝗈𝖣𝖡
- 𝖡𝖮𝖳 𝖲𝖾𝗋𝗏𝖾𝗋 : 𝖠𝗇𝗒𝖶𝗁𝖾𝗋𝖾
"""
