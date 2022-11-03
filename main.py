from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram import executor
from config import dp, bot
from inline import menuStart, menuProg, menuLavash, reply,menumenu
import logging


@dp.message_handler(Command('start'))
async def start(msg: Message):
    img = open("images/photo_2022-10-27_15-35-07.jpg", "rb")
    text = f"Assalomu_alaykum {msg.from_user.full_name},\nBLAST BURGER Botiga hush kelibsiz "
    await bot.send_photo(msg.chat.id, img, caption=text, reply_markup=menuStart)


@dp.message_handler(commands='help')
async def help(msg: Message):
    img = open("", "rb")
    text = f"Yordam uchun https://t.me/Instagiram_i ga ulaning"
    await bot.send_photo(msg.chat.id, img, caption=text)


@dp.message_handler(text="menu")
async def python_asos(msg:Message):
    await msg.answer(f"kerakli tugmani tanglang!", reply_markup=menumenu)


@dp.message_handler(text="MENU")
async def python_asos(msg:Message):
    await msg.answer(f"kerakli tugmani tanglang!", reply_markup=menuProg)


@dp.message_handler(text="Lavash")
async def lavash(msg: Message):
    await msg.answer("😍Lavash😋 \n 💸Narxi:  25000 so'm", reply_markup=menuLavash)


@dp.message_handler(text="Lavash pishloqli")
async def lavash(msg: Message):
    await msg.answer("😍Lavash pishloqli😋 \n 💸Narxi:  28000 so'm", reply_markup=menuLavash)


@dp.message_handler(text="Blast donar")
async def lavash(msg: Message):
    await msg.answer("😍Blast Donar😋 \n 💸Narxi:  26000 so'm", reply_markup=menuLavash)


@dp.message_handler(text="Blast donar Mini")
async def lavash(msg: Message):
    await msg.answer("😍Blast Donar Mini😋 \n 💸Narxi:  19000 so'm", reply_markup=menuLavash)


@dp.message_handler(text="Xaggi")
async def lavash(msg: Message):
    await msg.answer("😍Xaggi😋 \n 💸Narxi:  29000 so'm",reply_markup=menuLavash)

@dp.message_handler(text="Kolumbiya")
async def lavash(msg: Message):
    await msg.answer("😍Kolumbiya😋 \n 💸Narxi:  30000 so'm",reply_markup=menuLavash)

@dp.message_handler(text="Donar")
async def lavash(msg: Message):
    await msg.answer("😍Donar😋 \n 💸Narxi:  24000 so'm",reply_markup=menuLavash)

@dp.message_handler(text="Donar Mini")
async def lavash(msg: Message):
    await msg.answer("😍Blast Donar Mini😋 \n 💸Narxi:  19000 so'm",reply_markup=menuLavash)

@dp.message_handler(text="Donar Bludo")
async def lavash(msg: Message):
    await msg.answer("😍Donar Bludo😋 \n 💸Narxi:  40000 so'm",reply_markup=menuLavash)

@dp.message_handler(text="Gamburger")
async def lavash(msg: Message):
    await msg.answer("😍Gamburger😋 \n 💸Narxi:  20000 so'm",reply_markup=menuLavash)

@dp.message_handler(text="Big Gamburger")
async def lavash(msg: Message):
    await msg.answer("😍Big Gamburger😋 \n 💸Narxi:  28000 so'm",reply_markup=menuLavash)

@dp.message_handler(text="CHizburger")
async def lavash(msg: Message):
    await msg.answer("😍Chizburger😋 \n 💸Narxi:  23000 so'm",reply_markup=menuLavash)

@dp.message_handler(text="Big CHizburger")
async def lavash(msg: Message):
    await msg.answer("😍Big Chizburger😋 \n 💸Narxi:  34000 so'm", reply_markup=menuLavash)

@dp.message_handler(text="Klab-Sendvich")
async def lavash(msg: Message):
    await msg.answer("😍Klab-Sendvich😋 \n 💸Narxi:  30000 so'm", reply_markup=menuLavash)

@dp.message_handler(text="Xot dog korolevsliy")
async def lavash(msg: Message):
    await msg.answer("😍Xot dog korolevskiy😋 \n 💸Narxi:  18000 so'm", reply_markup=menuLavash)

@dp.message_handler(text="Fri")
async def lavash(msg: Message):
    await msg.answer("😍Fri😋 \n 💸Narxi:  14000 so'm", reply_markup=menuLavash)

@dp.message_handler(text="Xot Dog")
async def lavash(msg: Message):
    await msg.answer("😍XOT DOG😋 \n 💸Narxi:  12000 so'm", reply_markup=menuLavash)

@dp.message_handler(text="➕🛒Korzinaga qo'shish")
async def lavash(msg:Message):
    await msg.answer("kerakli tugmani tanglang",reply_markup=reply)


@dp.message_handler(text="1")
async def lavash(msg:Message):
    await msg.answer("buyurtma qabul qilindi ",reply_markup=menuProg)

@dp.message_handler(text="2")
async def lavash(msg:Message):
    await msg.answer("buyurtma qabul qilindi ",reply_markup=menuProg)

@dp.message_handler(text="3")
async def lavash(msg:Message):
    await msg.answer("buyurtma qabul qilindi ",reply_markup=menuProg)

@dp.message_handler(text="4")
async def lavash(msg:Message):
    await msg.answer("buyurtma qabul qilindi ",reply_markup=menuProg)

@dp.message_handler(text="5")
async def lavash(msg:Message):
    await msg.answer("buyurtma qabul qilindi ",reply_markup=menuProg)

@dp.message_handler(text="6")
async def lavash(msg:Message):
    await msg.answer("buyurtma qabul qilindi ",reply_markup=menuProg)

@dp.message_handler(text="7")
async def lavash(msg:Message):
    await msg.answer("buyurtma qabul qilindi ",reply_markup=menuProg)

@dp.message_handler(text="8")
async def lavash(msg:Message):
    await msg.answer("buyurtma qabul qilindi ",reply_markup=menuProg)

@dp.message_handler(text="9")
async def lavash(msg:Message):
    await msg.answer("buyurtma qabul qilindi ",reply_markup=menuProg)

@dp.message_handler(text="10")
async def lavash(msg:Message):
    await msg.answer("buyurtma qabul qilindi ",reply_markup=menuProg)

@dp.message_handler(text="orqaga")
async def python_asos(msg:Message):
    await msg.answer(f"kerakli tugmani tanglang!", reply_markup=menuProg)


@dp.message_handler(text="Asosiy menu")
async def start(msg: Message):
    text = f"Assalomu_alaykum {msg.from_user.full_name},\nBLAST BURGER Botiga hush kelibsiz "
    await bot.send_photo(msg.chat.id, reply_markup=menuStart)

if __name__ == '__main__':
    executor.start_polling(dp)