from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from AloneMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_3"],
                    url=f"https://t.me/{app.username}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="help_callback hb2",
                ),
            ],
            [
                InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
                InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            ],
            [
                InlineKeyboardButton(
                    text="✚ ᴋᴀʏɴᴀᴋ ᴋᴏᴅᴜ ✚",
                    url="https://github.com/KumsalTR63/KumsalMeldi/blob/master/AloneMusic",
                ),
            ],
            [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
        ],
        [
            InlineKeyboardButton(
                text="✚ ᴋᴀʏɴᴀᴋ ᴋᴏᴅᴜ ✚",
                url="https://github.com/KumsalTR63/KumsalMeldi/blob/master/AloneMusic",
            ),
        ],
    ]
    return buttons
