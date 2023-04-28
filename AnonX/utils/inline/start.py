from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀ᑯᑯ 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝚰𐓣 𝐆𝗋ⱺυρ ",
                url=f"https://t.me/Jiosaavn_TetrisBot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑯𝒆𝒍𝒑",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝑺𝒆𝒕𝒕𝒊𝒏𝒈𝒔", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀ᑯᑯ 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝚰𐓣 𝐆𝗋ⱺυρ",
                url=f"https://t.me/Jiosaavn_TetrisBot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑯𝒆𝒍𝒑", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="𝐉𝗂ⱺ 𝐒αα𝗏𐓣", url=f"https://www.jiosaavn.com/"
            )
        ],
     ]
    return buttons

