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
     if 0 < anon <= 1:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝑴𝒖𝒔𝒊𝒄"
    elif 1 < anon < 2:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 2 <= anon < 3:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 3 <= anon < 4:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 4 <= anon < 5:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 5 <= anon < 6:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 6 <= anon < 7:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 7 <= anon < 8:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 8 <= anon < 9:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 "
    elif 9 <= anon < 10:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 10 <= anon < 11:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 11 <= anon < 12:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 12 <= anon < 13:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐌υ𝗌𝗂𝖼"
    elif 13 <= anon < 14:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝑴𝒖𝒔𝒊𝒄"
    elif 14 <= anon < 15:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 15 <= anon < 16:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 16 <= anon < 17:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 17 <= anon < 18:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 18 <= anon < 19:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 19 <= anon < 20:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 20 <= anon < 21:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 21 <= anon < 22:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣"
    elif 22 <= anon < 23:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 23 <= anon < 24:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 24 <= anon < 25:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 25 <= anon < 26:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 26 <= anon < 27:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 27 <= anon < 28:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 28 <= anon < 29:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 29 <= anon < 30:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 30 <= anon < 31:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣"
    elif 31 <= anon < 32:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 32 <= anon < 33:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 33 <= anon < 34:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 34 <= anon < 35:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 35 <= anon < 36:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 36 <= anon < 37:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 37 <= anon < 38:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ "
    elif 38 <= anon < 39:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 39 <= anon < 40:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 40 <= anon < 41:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 41 <= anon < 42:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 "
    elif 42 <= anon < 43:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 43 <= anon < 44:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 44 <= anon < 45:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐌υ𝗌𝗂𝖼"
    elif 45 <= anon < 46:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 46 <= anon < 47:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 47 <= anon < 48:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 48 <= anon < 49:
        bar = "𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"
    elif 49 <= anon < 50:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 50 <= anon < 51:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 51 <= anon < 52:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 52 <= anon < 53:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 53 <= anon < 54:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 54 <= anon < 55:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 55 <= anon < 56:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 56<= anon < 57:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 "
    elif 57 <= anon < 58:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 58 <= anon < 59:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 59 <= anon < 60:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 60 <= anon < 61:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐌υ𝗌𝗂𝖼"
    elif 61 <= anon < 62:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝑴𝒖𝒔𝒊𝒄"
    elif 62 <= anon < 63:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 63 <= anon < 64:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 64 <= anon < 65:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 65 <= anon < 66:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 66 <= anon < 67:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 67 <= anon < 68:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 68 <= anon < 69:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 69 <= anon < 70:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣"
    elif 70 <= anon < 71:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 71 <= anon < 72:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 72 <= anon < 73:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 73 <= anon < 74:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 74 <= anon < 75:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 75 <= anon < 76:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 76 <= anon < 77:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 77 <= anon < 78:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 78 <= anon < 79:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣"
    elif 79 <= anon < 80:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 80 <= anon < 81:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 81 <= anon < 82:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 82 <= anon < 83:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 83 <= anon < 84:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 84 <= anon < 85:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 85 <= anon < 86:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 86 <= anon < 87:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ "
    elif 87 <= anon < 88:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 88 <= anon < 89:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 89 <= anon < 90:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 90 <= anon < 91:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 "
    elif 91 <= anon < 92:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 92 <= anon < 93:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 93 <= anon < 94:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐌υ𝗌𝗂𝖼"
    elif 94 <= anon < 95:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 95 <= anon < 96:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 96 <= anon < 97:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 97 <= anon < 98:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 98 <= anon < 99:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    else:
        bar = "𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"


    buttons = [
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
                text=f"{bar}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐉𝗂ⱺ 𝐒αα𝗏𐓣", url=f"https://wynk.in/music"
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
    if 0 < anon <= 1:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝑴𝒖𝒔𝒊𝒄"
    elif 1 < anon < 2:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 2 <= anon < 3:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 3 <= anon < 4:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 4 <= anon < 5:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 5 <= anon < 6:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 6 <= anon < 7:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 7 <= anon < 8:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 8 <= anon < 9:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 "
    elif 9 <= anon < 10:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 10 <= anon < 11:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 11 <= anon < 12:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 12 <= anon < 13:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐌υ𝗌𝗂𝖼"
    elif 13 <= anon < 14:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝑴𝒖𝒔𝒊𝒄"
    elif 14 <= anon < 15:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 15 <= anon < 16:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 16 <= anon < 17:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 17 <= anon < 18:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 18 <= anon < 19:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 19 <= anon < 20:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 20 <= anon < 21:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 21 <= anon < 22:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣"
    elif 22 <= anon < 23:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 23 <= anon < 24:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 24 <= anon < 25:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 25 <= anon < 26:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 26 <= anon < 27:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 27 <= anon < 28:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 28 <= anon < 29:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 29 <= anon < 30:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 30 <= anon < 31:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣"
    elif 31 <= anon < 32:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 32 <= anon < 33:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 33 <= anon < 34:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 34 <= anon < 35:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 35 <= anon < 36:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 36 <= anon < 37:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 37 <= anon < 38:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ "
    elif 38 <= anon < 39:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 39 <= anon < 40:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 40 <= anon < 41:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 41 <= anon < 42:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 "
    elif 42 <= anon < 43:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 43 <= anon < 44:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 44 <= anon < 45:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐌υ𝗌𝗂𝖼"
    elif 45 <= anon < 46:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 46 <= anon < 47:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 47 <= anon < 48:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 48 <= anon < 49:
        bar = "𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"
    elif 49 <= anon < 50:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 50 <= anon < 51:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 51 <= anon < 52:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 52 <= anon < 53:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 53 <= anon < 54:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 54 <= anon < 55:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 55 <= anon < 56:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 56<= anon < 57:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 "
    elif 57 <= anon < 58:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 58 <= anon < 59:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 59 <= anon < 60:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 60 <= anon < 61:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐌υ𝗌𝗂𝖼"
    elif 61 <= anon < 62:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝑴𝒖𝒔𝒊𝒄"
    elif 62 <= anon < 63:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 63 <= anon < 64:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 64 <= anon < 65:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 65 <= anon < 66:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 66 <= anon < 67:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 67 <= anon < 68:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 68 <= anon < 69:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 69 <= anon < 70:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣"
    elif 70 <= anon < 71:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 71 <= anon < 72:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 72 <= anon < 73:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 73 <= anon < 74:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 74 <= anon < 75:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 75 <= anon < 76:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 76 <= anon < 77:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 77 <= anon < 78:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 78 <= anon < 79:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣"
    elif 79 <= anon < 80:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 80 <= anon < 81:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 81 <= anon < 82:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 82 <= anon < 83:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 83 <= anon < 84:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 84 <= anon < 85:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 85 <= anon < 86:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 86 <= anon < 87:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ "
    elif 87 <= anon < 88:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 88 <= anon < 89:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 89 <= anon < 90:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 90 <= anon < 91:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 "
    elif 91 <= anon < 92:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 92 <= anon < 93:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 93 <= anon < 94:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐌υ𝗌𝗂𝖼"
    elif 94 <= anon < 95:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 95 <= anon < 96:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 96 <= anon < 97:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 97 <= anon < 98:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 98 <= anon < 99:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    else:
        bar = "𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"

    buttons = [
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
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{bar}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="𝐉𝗂ⱺ 𝐒αα𝗏𐓣", url=f"https://wynk.in/music")
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
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐉𝗂ⱺ 𝐒αα𝗏𐓣", url=f"https://wynk.in/music")
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
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="𝐉𝗂ⱺ 𝐒αα𝗏𐓣", url=f"https://wynk.in/music")
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
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            
            InlineKeyboardButton(
                text="𝐉𝗂ⱺ 𝐒αα𝗏𐓣", url=f"https://wynk.in/music"
            ),       
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data=f"close"
            )
        ],
    ]
    return buttons
