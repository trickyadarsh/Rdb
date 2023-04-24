from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝑨𝒅𝒅 𝑾𝒚𝒏𝒌  𝑴𝒖𝒔𝒊𝒄 𝑰𝒏 𝑮𝒓𝒐𝒖𝒑 ",
                url=f"https://t.me/Wynk_Music_TetrisBot?startgroup=true",
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
                text="𝑨𝒅𝒅 𝑾𝒚𝒏𝒌  𝑴𝒖𝒔𝒊𝒄 𝑰𝒏 𝑮𝒓𝒐𝒖𝒑 ",
                url=f"https://t.me/Wynk_Music_TetrisBot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑯𝒆𝒍𝒑", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="𝑾𝒚𝒏𝒌", url=f"https://wynk.in/music"
            )
        ],
     ]
    return buttons

