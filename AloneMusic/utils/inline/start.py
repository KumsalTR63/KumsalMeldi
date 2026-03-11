from pyrogram import enums
from pyrogram.types import InlineKeyboardButton

import config
from AloneMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=enums.ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,
                style=enums.ButtonStyle.SUCCESS,
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=enums.ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                callback_data="settings_back_helper",
                style=enums.ButtonStyle.SECONDARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                user_id=config.OWNER_ID,
                style=enums.ButtonStyle.SUCCESS,
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,
                style=enums.ButtonStyle.SUCCESS,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_6"],
                url=config.SUPPORT_CHANNEL,
                style=enums.ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["S_B_7"],
                url=config.UPSTREAM_REPO,
                style=enums.ButtonStyle.DANGER,
            ),
        ],
    ]
    return buttons
