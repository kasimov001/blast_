from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup
import logging

menustart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Raqamni yuborish", request_contact=True)
        ],
    ],
    resize_keyboard=True
)


menustart1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Lokatsiya yuborish", request_location=True)
        ],
    ],
    resize_keyboard=True
)



# menushaxar = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Toshkent"),
#             KeyboardButton(text="Surxondaryo"),
#             KeyboardButton(text="Sirdaryo")
#         ],
#         [
#             KeyboardButton(text="Samarqand"),
#             KeyboardButton(text="Qashqadaryo"),
#             KeyboardButton(text="Navoiy")
#         ],
#         [
#             KeyboardButton(text="Namangan"),
#             KeyboardButton(text="Xorazim"),
#             KeyboardButton(text="Jizzax")
#         ],
#         [
#             KeyboardButton(text="Fargona"),
#             KeyboardButton(text="Buxoro"),
#             KeyboardButton(text="Andijon")
#         ]
#     ],
#     resize_keyboard=True
# )
menumenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌯Lavash",callback_data="Lavash"),
            InlineKeyboardButton(text="🍟FRI MENU", callback_data="Fri")
        ],
        [
            InlineKeyboardButton(text="🌮Shaurma Mol gosht", callback_data="SHaurma Mol gosht")
        ],
        [
            InlineKeyboardButton(text="🌮Shourma Tovuq gosht", callback_data="SHourma Tovuq gosht")
        ],
        [
            InlineKeyboardButton(text="🍔 Cheeseburger", callback_data="CHeeseburger"),
            InlineKeyboardButton(text="🍔Gamburger", callback_data="gam")
        ],
        [
            InlineKeyboardButton(text="🍔🥤Combo Plus", callback_data="Combo Plus"),
            InlineKeyboardButton(text="🌭🧃🍟Kids Combo", callback_data="Kids Combo")
        ],
        [
            InlineKeyboardButton(text="🌭Hot-Dog MENU", callback_data="Hot-Dog MENU"),
            InlineKeyboardButton(text="🥤🧋🧃 Ichimliklar", callback_data="Ichimliklar")
        ]
    ]
)
menulavash = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Original Lavash", callback_data="Mol gosht"),
            InlineKeyboardButton(text="Orginal Kichik Lavash", callback_data="Tovuq gosht")
        ],
        [
            InlineKeyboardButton(text="Pishloqli Lavash", callback_data="CHeese Mol gosht"),
            InlineKeyboardButton(text="Pishloqli Kichik Lavash", callback_data="CHeese Tovuq gosht")
        ],
        [
            InlineKeyboardButton(text="Tandir Lavash", callback_data="Tandir"),
            InlineKeyboardButton(text="Pishloqli Tandir Lavash", callback_data="pishlav")
        ],
        [
            InlineKeyboardButton(text="Xalapenyoli Lavash", callback_data="xala")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menufri = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍟FRI", callback_data="🍟FRI MENU"),
            InlineKeyboardButton(text="Salat", callback_data="Salat")
        ],
        [
            InlineKeyboardButton(text='Guruch', callback_data="Guruch")
        ],
        [
            InlineKeyboardButton(text="Tovuq Strips", callback_data="Tovuq Strips")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]

)
menushaurmagosht = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Big", callback_data="Big"),
            InlineKeyboardButton(text="Standard", callback_data="Standard")
        ],
        [
            InlineKeyboardButton(text="Big Qalampir", callback_data="Big Qalampir")
        ],
        [
            InlineKeyboardButton(text="Standard Qalampir", callback_data="Standard Qalampir")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menushaurmatovuq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Big", callback_data="big"),
            InlineKeyboardButton(text="Standard", callback_data="standard")
        ],
        [
            InlineKeyboardButton(text="Big Qalampir", callback_data="big qalampir")
        ],
        [
            InlineKeyboardButton(text="Standard Qalampir", callback_data="standard qalampir")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menucheeseburger = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Cheeseburger", callback_data="Cheeseburger"),
            InlineKeyboardButton(text="Double Cheese", callback_data="Doule Cheese")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menugamburger = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍔Gamburger", callback_data="cheeseburger"),
            InlineKeyboardButton(text="🍔Gamburger big", callback_data="doule cheese")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menucombo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="1️⃣"),
            InlineKeyboardButton(text="2️⃣", callback_data="2️⃣"),
            InlineKeyboardButton(text="3️⃣", callback_data="3️⃣")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menucombokids = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="1kids"),
            InlineKeyboardButton(text="2️⃣", callback_data="2kids"),
            InlineKeyboardButton(text="3️⃣", callback_data="3kids")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menuhoddog = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Hot-Dog Kids", callback_data="Hot-Dog Kids")
        ],
        [
            InlineKeyboardButton(text="Hot-Dog Classic", callback_data="Hot-Dog Classic")
        ],
        [
            InlineKeyboardButton(text="Hot-Dog Baguette", callback_data="Hot-Dog Baguette")
        ],
        [
            InlineKeyboardButton(text="Hot-Dog Baguette Duoble", callback_data="Hot-Dog Baguette Duoble")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menuichimliklar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Coca Cola", callback_data="Coca Cola")
        ],
        [
            InlineKeyboardButton(text="Pepsi", callback_data="Pepsi")
        ],
        [
            InlineKeyboardButton(text="Fanta", callback_data="Fanta")
        ],
        [
            InlineKeyboardButton(text="Sprite", callback_data="Sprite")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
#menning ichi
menumol = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="t"),
            InlineKeyboardButton(text="2️⃣", callback_data="t"),
            InlineKeyboardButton(text="3️⃣", callback_data="t")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menutovuq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="q"),
            InlineKeyboardButton(text="2️⃣", callback_data="q"),
            InlineKeyboardButton(text="3️⃣", callback_data="q")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menucheesemol = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="10e"),
            InlineKeyboardButton(text="2️⃣", callback_data="10e"),
            InlineKeyboardButton(text="3️⃣", callback_data="10e")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menucheesetovuq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="w"),
            InlineKeyboardButton(text="2️⃣", callback_data="w"),
            InlineKeyboardButton(text="3️⃣", callback_data="w")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menutandir = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="y"),
            InlineKeyboardButton(text="2️⃣", callback_data="y"),
            InlineKeyboardButton(text="3️⃣", callback_data="y")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menupish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="u"),
            InlineKeyboardButton(text="2️⃣", callback_data="u"),
            InlineKeyboardButton(text="3️⃣", callback_data="u")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menuxala = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="i"),
            InlineKeyboardButton(text="2️⃣", callback_data="i"),
            InlineKeyboardButton(text="3️⃣", callback_data="i")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
        ]
)
menufri1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="o"),
            InlineKeyboardButton(text="2️⃣", callback_data="o"),
            InlineKeyboardButton(text="3️⃣", callback_data="o")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menusalat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="p"),
            InlineKeyboardButton(text="2️⃣", callback_data="p"),
            InlineKeyboardButton(text="3️⃣", callback_data="p")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menuguruch = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="a"),
            InlineKeyboardButton(text="2️⃣", callback_data="a"),
            InlineKeyboardButton(text="3️⃣", callback_data="a")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menuStrips = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="s"),
            InlineKeyboardButton(text="2️⃣", callback_data="s"),
            InlineKeyboardButton(text="3️⃣", callback_data="s")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menubig = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="d"),
            InlineKeyboardButton(text="2️⃣", callback_data="d"),
            InlineKeyboardButton(text="3️⃣", callback_data="d")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menustandard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="f"),
            InlineKeyboardButton(text="2️⃣", callback_data="f"),
            InlineKeyboardButton(text="3️⃣", callback_data="f")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menubigqalampir = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="g"),
            InlineKeyboardButton(text="2️⃣", callback_data="g"),
            InlineKeyboardButton(text="3️⃣", callback_data="g")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menustndardqalampir = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="h"),
            InlineKeyboardButton(text="2️⃣", callback_data="h"),
            InlineKeyboardButton(text="3️⃣", callback_data="h")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menugib = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="k"),
            InlineKeyboardButton(text="2️⃣", callback_data="k"),
            InlineKeyboardButton(text="3️⃣", callback_data="k")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menudard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="l"),
            InlineKeyboardButton(text="2️⃣", callback_data="l"),
            InlineKeyboardButton(text="3️⃣", callback_data="l")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menugibqalampir = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="z"),
            InlineKeyboardButton(text="2️⃣", callback_data="z"),
            InlineKeyboardButton(text="3️⃣", callback_data="z")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menudardqalampir = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="x"),
            InlineKeyboardButton(text="2️⃣", callback_data="x"),
            InlineKeyboardButton(text="3️⃣", callback_data="x")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menucheese = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="c"),
            InlineKeyboardButton(text="2️⃣", callback_data="c"),
            InlineKeyboardButton(text="3️⃣", callback_data="c")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menudoule = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="v"),
            InlineKeyboardButton(text="2️⃣", callback_data="v"),
            InlineKeyboardButton(text="3️⃣", callback_data="v")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
###
menuburger = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="b"),
            InlineKeyboardButton(text="2️⃣", callback_data="b"),
            InlineKeyboardButton(text="3️⃣", callback_data="b")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menuchesse = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="km"),
            InlineKeyboardButton(text="2️⃣", callback_data="km"),
            InlineKeyboardButton(text="3️⃣", callback_data="km")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menukids = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="m"),
            InlineKeyboardButton(text="2️⃣", callback_data="m"),
            InlineKeyboardButton(text="3️⃣", callback_data="m")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menuclassic = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="1q"),
            InlineKeyboardButton(text="2️⃣", callback_data="1q"),
            InlineKeyboardButton(text="3️⃣", callback_data="1q")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menubaguette = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="opa"),
            InlineKeyboardButton(text="2️⃣", callback_data="opa"),
            InlineKeyboardButton(text="3️⃣", callback_data="opa")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menubaguetteduoble = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="3e"),
            InlineKeyboardButton(text="2️⃣", callback_data="3e"),
            InlineKeyboardButton(text="3️⃣", callback_data="3e")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menucola = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="4r"),
            InlineKeyboardButton(text="2️⃣", callback_data="4r"),
            InlineKeyboardButton(text="3️⃣", callback_data="4r")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menupepsi = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="2w"),
            InlineKeyboardButton(text="2️⃣", callback_data="2w"),
            InlineKeyboardButton(text="3️⃣", callback_data="2w")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menufanta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="fanta"),
            InlineKeyboardButton(text="2️⃣", callback_data="fanta"),
            InlineKeyboardButton(text="3️⃣", callback_data="fanta")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)
menusprayt = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="ni"),
            InlineKeyboardButton(text="2️⃣", callback_data="ni"),
            InlineKeyboardButton(text="3️⃣", callback_data="ni")
        ],
        [
            InlineKeyboardButton(text="⬅️Ortga", callback_data="a16")
        ]
    ]
)











