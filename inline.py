from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="telefon nomer",request_contact=True)
        ],
        [
            KeyboardButton(text="menu")
        ]
    ],
    resize_keyboard=True
)

menumenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="MENU"),
            # KeyboardButton(text="SUVLAR"),
            KeyboardButton(text="➕🛒Korzinaga qo'shish")
        ],
        [
            KeyboardButton(text="⚙️🛠Sozlamalar"),
            KeyboardButton(text="lakatsa", request_location=True)
        ]
    ],
    resize_keyboard=True
)

menuProg=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Asosiy menu"),
            KeyboardButton(text="➕🛒Korzinaga qo'shish")
        ],
        [
            KeyboardButton(text="Lavash"),
            KeyboardButton(text="Lavash pishloqli")
        ],
        [
            KeyboardButton(text="Blast donar"),
            KeyboardButton(text="Blast donar Mini")
        ],
        [
            KeyboardButton(text="Xaggi"),
            KeyboardButton(text="Kolumbiya")
        ],
        [
            KeyboardButton(text="Donar"),
            KeyboardButton(text="Donar Mini")
        ],
        [
            KeyboardButton(text="Donar Bludo"),
            KeyboardButton(text="Gamburger")
        ],
        [
            KeyboardButton(text="Big Gamburger"),
            KeyboardButton(text="CHizburger")
        ],
        [
            KeyboardButton(text="Big CHizburger"),
            KeyboardButton(text="Klab-Sendvich")
        ],
        [
            KeyboardButton(text="Xot dog korolevsliy"),
            KeyboardButton(text="Fri")
        ],
        [
            KeyboardButton(text="Xot Dog"),
            KeyboardButton(text="orqaga")
        ]
    ],
    resize_keyboard=True
)

menuLavash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Asosiy menu"),
            KeyboardButton(text="➕🛒Korzinaga qo'shish")
        ],
        [
            KeyboardButton(text="orqaga")
        ]
    ],
    resize_keyboard=True
)
reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3"),
            KeyboardButton(text="4"),
            KeyboardButton(text="5"),
        ],
        [
            KeyboardButton(text="6"),
            KeyboardButton(text="7"),
            KeyboardButton(text="8"),
            KeyboardButton(text="9"),
            KeyboardButton(text="10"),
        ],
        [
            KeyboardButton(text="orqaga")
        ]
    ],
    resize_keyboard=True
)