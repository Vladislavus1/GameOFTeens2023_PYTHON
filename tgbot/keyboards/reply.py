from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType

start_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Тарифи")
        ]
    ]
)

menu_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Усі тарифи")
        ],
        [
            KeyboardButton(text="Підібрати тариф під себе")
        ]
    ]
)

start_phone_kb = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Поділитися контактом", request_contact=True)
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

phone_var_kb = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Лімітний"),
            KeyboardButton(text="Безлімітний")
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)
phone_var_kb2 = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Лімітні"),
            KeyboardButton(text="Безлімітні")
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

phone_var_kb3 = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="375 грн"),
            KeyboardButton(text="250 грн"),
            KeyboardButton(text="180 грн"),
            KeyboardButton(text="150 грн"),
            KeyboardButton(text="120 грн"),
            KeyboardButton(text="90 грн"),
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

rate_kb = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Так :D"),
            KeyboardButton(text="Ні :(")
        ]
    ]
)

