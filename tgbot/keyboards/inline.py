from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



link_keyb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Придбати тариф", callback_data="info")
        ]
    ]
)

