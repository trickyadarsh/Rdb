from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝑷𝒆𝒓𝒔𝒐𝒏𝒂𝒍",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="𝑮𝒍𝒐𝒃𝒂𝒍", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝑻𝒐𝒑 𝟏𝟎 𝑾𝒚𝒏𝒌", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑷𝒆𝒓𝒔𝒐𝒏𝒂𝒍", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑮𝒍𝒐𝒃𝒂𝒍", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="𝑮𝒓𝒐𝒖𝒑'𝒔", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑩𝒂𝒄𝒌", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝑨𝒖𝒅𝒊𝒐", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="𝑽𝒊𝒅𝒆𝒐", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝑩𝒂𝒄𝒌", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝑻𝒐𝒑 𝟏𝟎 𝑾𝒚𝒏𝒌", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑷𝒆𝒓𝒔𝒐𝒏𝒂𝒍", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑮𝒍𝒐𝒃𝒂𝒍", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="𝑮𝒓𝒐𝒖𝒑'𝒔", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑩𝒂𝒄𝒌", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝑩𝒂𝒄𝒌",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝑫𝒆𝒍𝒆𝒕𝒆",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝑩𝒂𝒄𝒌",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="𝑪𝒍𝒐𝒔𝒆",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝑪𝒍𝒐𝒔𝒆",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
