import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from AnonX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 10:
        ba = "⚪─────────"
    elif 10 < anon < 20:
        ba = "━⚪────────"
    elif 20 <= anon < 30:
        ba = "━━⚪───────"
    elif 30 <= anon < 40:
        ba = "━━━⚪──────"
    elif 40 <= anon < 50:
        ba = "━━━━⚪─────"
    elif 50 <= anon < 60:
        ba = "━━━━━⚪────"
    elif 60 <= anon < 70:
        ba = "━━━━━━⚪───"
    elif 70 <= anon < 80:
        ba = "━━━━━━━⚪──"
    elif 80 <= anon < 95:
        ba = "━━━━━━━━⚪─"
    else:
        ba = "━━━━━━━━━⚪"

#bar of wynk---------------------------------------
    if 0 < anon <= 2:
        bar = "𝑾𝒚𝒏𝒌 𝑴𝒖𝒔𝒊𝒄"
    elif 2 < anon < 4:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 4 <= anon < 6:
        bar = "𝐒𝗂𝗑 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 6 <= anon < 8:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 8 <= anon < 10:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 10 <= anon < 12:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 12 <= anon < 14:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 14 <= anon < 16:
        bar = "𝐖𝗒𐓣𝗄 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 16 <= anon < 18:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐖𝗒𐓣𝗄 "
    elif 18 <= anon < 20:
        bar = "𝐖𝗒𐓣𝗄 𝐒𝗍υᑯ𝗂ⱺ"
    elif 20 <= anon < 22:
        bar = "𝐖𝗒𐓣𝗄 𝐀ρρ"
    elif 22 <= anon < 24:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐖𝗒𐓣𝗄 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 24 <= anon < 26:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐖𝗒𐓣𝗄 𝐌υ𝗌𝗂𝖼"
    elif 26 <= anon < 28:
        bar = "𝑾𝒚𝒏𝒌 𝑴𝒖𝒔𝒊𝒄"
    elif 28 <= anon < 30:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 30 <= anon < 32:
        bar = "𝐒𝗂𝗑 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 32 <= anon < 34:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 34 <= anon < 36:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 36 <= anon < 38:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 38 <= anon < 40:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 40 <= anon < 42:
        bar = "𝐖𝗒𐓣𝗄 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 42 <= anon < 44:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐖𝗒𐓣𝗄"
    elif 44 <= anon < 46:
        bar = "𝐖𝗒𐓣𝗄 𝐒𝗍υᑯ𝗂ⱺ"
    elif 46 <= anon < 48:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐖𝗒𐓣𝗄 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 48 <= anon < 50:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 50 <= anon < 52:
        bar = "𝐒𝗂𝗑 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 52 <= anon < 54:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 54 <= anon < 56:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 56 <= anon < 58:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 58 <= anon < 60:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 60 <= anon < 62:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐖𝗒𐓣𝗄"
    elif 62 <= anon < 64:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐖𝗒𐓣𝗄 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 64 <= anon < 66:
        bar = "𝐖𝗒𐓣𝗄 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 66 <= anon < 68:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 68 <= anon < 70:
        bar = "𝐖𝗒𐓣𝗄 𝐀ρρ"
    elif 70 <= anon < 72:
        bar = "𝐖𝗒𐓣𝗄 𝐒𝗍υᑯ𝗂ⱺ"
    elif 72 <= anon < 74:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 74 <= anon < 76:
        bar = "𝐒𝗂𝗑 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 76 <= anon < 78:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ "
    elif 78 <= anon < 80:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 80 <= anon < 82:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 82 <= anon < 84:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 84 <= anon < 86:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐖𝗒𐓣𝗄 "
    elif 86 <= anon < 88:
        bar = "𝐖𝗒𐓣𝗄 𝐀ρρ"
    elif 88 <= anon < 90:
        bar = "𝐖𝗒𐓣𝗄 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 90 <= anon < 92:
        bar = "𝐖𝗒𐓣𝗄 𝐌υ𝗌𝗂𝖼"
    elif 92 <= anon < 94:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 94 <= anon < 96:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐖𝗒𐓣𝗄 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 96 <= anon < 98:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 98 <= anon < 99:
        bar = "𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"
    else:
        bar = "𝐖𝐲𝐧𝐤 𝐒𝐭𝐮𝐢𝐝𝐨"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{bar}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {ba} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="►►", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝑾𝒚𝒏𝒌", url=f"https://wynk.in/music"
            ),       
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data="close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 10:
        bar = "⚪─────────"
    elif 10 < anon < 20:
        ba = "━⚪────────"
    elif 20 <= anon < 30:
        ba = "━━⚪───────"
    elif 30 <= anon < 40:
        ba = "━━━⚪──────"
    elif 40 <= anon < 50:
        ba = "━━━━⚪─────"
    elif 50 <= anon < 60:
        ba = "━━━━━⚪────"
    elif 60 <= anon < 70:
        ba = "━━━━━━⚪───"
    elif 70 <= anon < 80:
        ba = "━━━━━━━⚪──"
    elif 80 <= anon < 95:
        ba = "━━━━━━━━⚪─"
    else:
        ba = "━━━━━━━━━⚪"

# Wynk bar-----------------------------------------------------------
    if 0 < anon <= 2:
        bar = "𝑾𝒚𝒏𝒌 𝑴𝒖𝒔𝒊𝒄"
    elif 2 < anon < 4:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 4 <= anon < 6:
        bar = "𝐒𝗂𝗑 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 6 <= anon < 8:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 8 <= anon < 10:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 10 <= anon < 12:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 12 <= anon < 14:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 14 <= anon < 16:
        bar = "𝐖𝗒𐓣𝗄 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 16 <= anon < 18:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐖𝗒𐓣𝗄 "
    elif 18 <= anon < 20:
        bar = "𝐖𝗒𐓣𝗄 𝐒𝗍υᑯ𝗂ⱺ"
    elif 20 <= anon < 22:
        bar = "𝐖𝗒𐓣𝗄 𝐀ρρ"
    elif 22 <= anon < 24:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐖𝗒𐓣𝗄 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 24 <= anon < 26:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐖𝗒𐓣𝗄 𝐌υ𝗌𝗂𝖼"
    elif 26 <= anon < 28:
        bar = "𝑾𝒚𝒏𝒌 𝑴𝒖𝒔𝒊𝒄"
    elif 28 <= anon < 30:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 30 <= anon < 32:
        bar = "𝐒𝗂𝗑 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 32 <= anon < 34:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 34 <= anon < 36:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 36 <= anon < 38:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 38 <= anon < 40:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 40 <= anon < 42:
        bar = "𝐖𝗒𐓣𝗄 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 42 <= anon < 44:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐖𝗒𐓣𝗄"
    elif 44 <= anon < 46:
        bar = "𝐖𝗒𐓣𝗄 𝐒𝗍υᑯ𝗂ⱺ"
    elif 46 <= anon < 48:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐖𝗒𐓣𝗄 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 48 <= anon < 50:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 50 <= anon < 52:
        bar = "𝐒𝗂𝗑 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 52 <= anon < 54:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 54 <= anon < 56:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 56 <= anon < 58:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 58 <= anon < 60:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 60 <= anon < 62:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐖𝗒𐓣𝗄"
    elif 62 <= anon < 64:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐖𝗒𐓣𝗄 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 64 <= anon < 66:
        bar = "𝐖𝗒𐓣𝗄 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 66 <= anon < 68:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 68 <= anon < 70:
        bar = "𝐖𝗒𐓣𝗄 𝐀ρρ"
    elif 70 <= anon < 72:
        bar = "𝐖𝗒𐓣𝗄 𝐒𝗍υᑯ𝗂ⱺ"
    elif 72 <= anon < 74:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 74 <= anon < 76:
        bar = "𝐒𝗂𝗑 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 76 <= anon < 78:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ "
    elif 78 <= anon < 80:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 80 <= anon < 82:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 82 <= anon < 84:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 84 <= anon < 86:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐖𝗒𐓣𝗄 "
    elif 86 <= anon < 88:
        bar = "𝐖𝗒𐓣𝗄 𝐀ρρ"
    elif 88 <= anon < 90:
        bar = "𝐖𝗒𐓣𝗄 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 90 <= anon < 92:
        bar = "𝐖𝗒𐓣𝗄 𝐌υ𝗌𝗂𝖼"
    elif 92 <= anon < 94:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 94 <= anon < 96:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐖𝗒𐓣𝗄 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 96 <= anon < 98:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 98 <= anon < 99:
        bar = "𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"
    else:
        bar = "𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{bar}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {ba} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="►►", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▧", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="𝑾𝒚𝒏𝒌", url=f"https://wynk.in/music")
        ],
        [
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data=f"close"
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="►►", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▧", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝑾𝒚𝒏𝒌", url=f"https://wynk.in/music")
        ],
        [
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="►►", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▧", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="𝑾𝒚𝒏𝒌", url=f"https://wynk.in/music")
        ],
        [
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="𝑪𝒍𝒐𝒔𝒆", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▧", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            
            InlineKeyboardButton(
                text="𝑾𝒚𝒏𝒌", url=f"https://wynk.in/music"
            ),       
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data=f"close"
            )
        ],
    ]
    return buttons
