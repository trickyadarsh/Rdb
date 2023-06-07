from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝑨𝒅𝒅 𝙋𝙧𝙖𝙮 𝙭 𝙢𝙪𝙨𝙞𝙘 ",
                url=f"https://t.me/prayit_musicbot?startgroup=true",
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
                text="𝑨𝒅𝒅 𝙋𝙧𝙖𝙮 𝙭 𝙢𝙪𝙨𝙞𝙘 ",
                url=f"https://t.me/prayit_musicbot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑯𝒆𝒍𝒑", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="𝑷𝒓𝒂𝒚𝒊𝒕", url=f"https://t.me/plovestatus"
            )
        ],
     ]
    return buttons

