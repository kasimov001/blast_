from aiogram import executor
from aiogram.types import Message, CallbackQuery

from confic import dp, bot
from inline import *


@dp.message_handler(commands="location")
async def loc(msg: Message):
    await bot.send_location(msg.chat.id, latitude=41.344802, longitude=69.206470)


@dp.message_handler(content_types="contact")
async def loc(msg: Message):
    await msg.answer(text="locaticon yuboring", reply_markup=menustart1)


@dp.message_handler(content_types="location")
async def loc(msg: Message):
    await msg.answer(text="Quydagilardan birini tanglang", reply_markup=menumenu)


@dp.message_handler(commands="start")
async def start(msg: Message):
    img = open("image/photo_2022-05-12_10-36-04.jpg", "rb")
    text = f"Ro'yxatdan o'tish uchun telefon raqamingizni kiriting \n Raqamni +998********* shaklida yuboring."
    await msg.answer_photo(img, text, reply_markup=menustart)


# @dp.message_handler(text="Toshkent")
# async def uzb(msg: Message):
#     await msg.answer(f"Buyurtma bering", reply_markup=menumenu)
#
#
# @dp.message_handler(text="Surxondaryo")
# async def uzb(msg: Message):
#     await msg.answer(f"Buyurtma bering", reply_markup=menumenu)
#
#
# @dp.message_handler(text="Sirdaryo")
# async def uzb(msg: Message):
#     await msg.answer(f"Buyurtma bering", reply_markup=menushaxar)
#
#
# @dp.message_handler(text="Samarqand")
# async def uzb(msg: Message):
#     await msg.answer(f"Buyurtma bering", reply_markup=menushaxar)
#
#
# @dp.message_handler(text="Qashqadaryo")
# async def uzb(msg: Message):
#     await msg.answer(f"Buyurtma bering", reply_markup=menushaxar)
#
#
# @dp.message_handler(text="Navoiy")
# async def uzb(msg: Message):
#     await msg.answer(f"Buyurtma bering", reply_markup=menushaxar)
#
#
# @dp.message_handler(text="Namangan")
# async def uzb(msg: Message):
#     await msg.answer(f"Buyurtma bering", reply_markup=menushaxar)
#
#
# @dp.message_handler(text="Xorazim")
# async def uzb(msg: Message):
#     await msg.answer(f"Buyurtma bering", reply_markup=menushaxar)
#
#
# @dp.message_handler(text="Jizzax")
# async def uzb(msg: Message):
#     await msg.answer(f"Buyurtma bering", reply_markup=menushaxar)
#
#
# @dp.message_handler(text="Fargona")
# async def uzb(msg: Message):
#     await msg.answer(f"Buyurtma bering", reply_markup=menushaxar)
#
#
# @dp.message_handler(text="Buxoro")
# async def uzb(msg: Message):
#     await msg.answer(f"Buyurtma bering", reply_markup=menushaxar)
#
#
# @dp.message_handler(text="Andijon")
# async def uzb(msg: Message):
#     await msg.answer(f"Buyurtma bering", reply_markup=menushaxar)


@dp.callback_query_handler(text="Lavash")
async def sample(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"Quydagilarni birini Tanlang", photo=img, reply_markup=menulavash)
    await call.message.delete()


@dp.callback_query_handler(text="Fri")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-39-36.jpg", "rb")
    await call.message.answer_photo(caption=f"Quydagilarni birini Tanlang", photo=img, reply_markup=menufri)
    await call.message.delete()


@dp.callback_query_handler(text="SHaurma Mol gosht")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"Shaurma Mol go'sht", photo=img, reply_markup=menushaurmagosht)
    await call.message.delete()


@dp.callback_query_handler(text="SHourma Tovuq gosht")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"Shaurma Tovuq go'sht ", photo=img, reply_markup=menushaurmatovuq)
    await call.message.delete()


@dp.callback_query_handler(text="CHeeseburger")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-13.jpg", "rb")
    await call.message.answer_photo(caption=f"Cheeseburger \n Menu Tanlang", photo=img, reply_markup=menucheeseburger)
    await call.message.delete()


@dp.callback_query_handler(text="gam")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-22.jpg", "rb")
    await call.message.answer_photo(caption=f"Gamburger \n Menu Tanlang", photo=img, reply_markup=menugamburger)
    await call.message.delete()


@dp.callback_query_handler(text="Combo Plus")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-32.jpg", "rb")
    await call.message.answer_photo(caption=f"Combo Plus  Combo plus: Fri 🍟 PEPSI 🥤 \n Narxi: 13 000", photo=img,
                                    reply_markup=menucombo)
    await call.message.delete()


@dp.callback_query_handler(text="Kids Combo")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-41.jpg", "rb")
    await call.message.answer_photo(
        caption=f"Kids Plus  Kids plus: Fri 🍟 \n Bolalar Uchun Bliss Sharbat 🧃 \n Narxi: 15 000", photo=img,
        reply_markup=menucombokids)
    await call.message.delete()


@dp.callback_query_handler(text="Hot-Dog MENU")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-39-36.jpg", "rb")
    await call.message.answer_photo(caption=f"Hot-Doglar Menu Quydagilarni birini Tanlang", photo=img,
                                    reply_markup=menuhoddog)
    await call.message.delete()


@dp.callback_query_handler(text="Ichimliklar")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-57.jpg", "rb")
    await call.message.answer_photo(caption=f"ICHIMLIKLAR \n Quydagilarni birini Tanlang", photo=img,
                                    reply_markup=menuichimliklar)
    await call.message.delete()


@dp.callback_query_handler(text="a16")
async def Ortga(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"Quydagilardan birin tanlang!", photo=img, reply_markup=menumenu)


@dp.callback_query_handler(text="Mol gosht")
async def sample(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"Orginal Lavash 23 000 som", photo=img, reply_markup=menumol)
    await call.message.delete()


@dp.callback_query_handler(text="Tovuq gosht")
async def sample(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"Orginal Kichik Lavash 20 000 som", photo=img, reply_markup=menutovuq)
    await call.message.delete()


@dp.callback_query_handler(text="CHeese Mol gosht")
async def sample(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"Pishloqli Lavash 26 000 som", photo=img, reply_markup=menucheesemol)
    await call.message.delete()


@dp.callback_query_handler(text="CHeese Tovuq gosht")
async def sample(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"Pishloqli Kichik Lavash 23 000 som", photo=img,
                                    reply_markup=menucheesetovuq)
    await call.message.delete()


@dp.callback_query_handler(text="Tandir")
async def sample(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"Tandir Lavash 24 000 som", photo=img, reply_markup=menutandir)
    await call.message.delete()


@dp.callback_query_handler(text="pishlav")
async def sample(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"Pishloqli Tandir Lavash 27 000 som", photo=img, reply_markup=menupish)
    await call.message.delete()


@dp.callback_query_handler(text="xala")
async def sample(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"Xalapenyoli Lavash", photo=img, reply_markup=menuxala)
    await call.message.delete()


@dp.callback_query_handler(text="🍟FRI MENU")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-39-36.jpg", "rb")
    await call.message.answer_photo(caption=f"fri", photo=img,
                                    reply_markup=menufri1)
    await call.message.delete()


@dp.callback_query_handler(text="Salat")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-16-42.jpg", "rb")
    await call.message.answer_photo(caption=f"salat", photo=img,
                                    reply_markup=menusalat)
    await call.message.delete()


@dp.callback_query_handler(text="Guruch")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-18-11.jpg", "rb")
    await call.message.answer_photo(caption=f"guruch", photo=img,
                                    reply_markup=menuguruch)
    await call.message.delete()


@dp.callback_query_handler(text="Tovuq Strips")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-19-39.jpg", "rb")
    await call.message.answer_photo(caption=f"strips", photo=img,
                                    reply_markup=menuStrips)
    await call.message.delete()


@dp.callback_query_handler(text="Big")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"Zakaz sonin tanglang!", photo=img,
                                    reply_markup=menubig)
    await call.message.delete()


@dp.callback_query_handler(text="Standard")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"Zakaz sonin tanglang!", photo=img,
                                    reply_markup=menustandard)
    await call.message.delete()


@dp.callback_query_handler(text="Big Qalampir")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"Zakaz sonin tanglang!", photo=img,
                                    reply_markup=menubigqalampir)
    await call.message.delete()


@dp.callback_query_handler(text="Standard Qalampir")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"Zakaz sonin tanglang!", photo=img,
                                    reply_markup=menustndardqalampir)
    await call.message.delete()


@dp.callback_query_handler(text="big")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"Zakaz sonin tanglang!", photo=img,
                                    reply_markup=menugib)
    await call.message.delete()


@dp.callback_query_handler(text="standard")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"Zakaz sonin tanglang!", photo=img,
                                    reply_markup=menudard)
    await call.message.delete()


@dp.callback_query_handler(text="big qalampir")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"Zakaz sonin tanglang!", photo=img,
                                    reply_markup=menugibqalampir)
    await call.message.delete()


@dp.callback_query_handler(text="standard qalampir")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"Zakaz sonin tanglang!", photo=img,
                                    reply_markup=menudardqalampir)
    await call.message.delete()


@dp.callback_query_handler(text="Cheeseburger")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-13.jpg", "rb")
    await call.message.answer_photo(caption=f"Cheeseburger", photo=img, reply_markup=menucheese)
    await call.message.delete()


@dp.callback_query_handler(text="Doule Cheese")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-13.jpg", "rb")
    await call.message.answer_photo(caption=f"Doule chesse", photo=img, reply_markup=menudoule)
    await call.message.delete()


@dp.callback_query_handler(text="cheeseburger")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-13.jpg", "rb")
    await call.message.answer_photo(caption=f"Cheeseburger", photo=img, reply_markup=menuburger)
    await call.message.delete()


@dp.callback_query_handler(text="doule cheese")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-13.jpg", "rb")
    await call.message.answer_photo(caption=f"Big gamburger", photo=img, reply_markup=menuchesse)
    await call.message.delete()


@dp.callback_query_handler(text="1️⃣")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-32.jpg", "rb")
    await call.message.answer_photo(caption=f"Combo Plus  \n Combo plus: EVOS Fri 🍟 EVOS PEPSI 🥤 \n Narxi: 13 000",
                                    photo=img, reply_markup=menukids)
    await call.message.delete()


@dp.callback_query_handler(text="2️⃣")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-32.jpg", "rb")
    await call.message.answer_photo(caption=f"Combo Plus  \n Combo plus: EVOS Fri 🍟 EVOS PEPSI 🥤 \n Narxi: 13 000",
                                    photo=img, reply_markup=menukids)
    await call.message.delete()


@dp.callback_query_handler(text="3️⃣")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-32.jpg", "rb")
    await call.message.answer_photo(caption=f"Combo Plus  \n Combo plus: EVOS Fri 🍟 EVOS PEPSI 🥤 \n Narxi: 13 000",
                     photo=img, reply_markup=menukids)
    await call.message.delete()


@dp.callback_query_handler(text="1kids")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-41.jpg", "rb")
    await call.message.answer_photo(
        caption=f"Kids Plus   \n Kids plus: EVOS Fri 🍟 \n Bolalar Uchun Bliss Sharbat 🧃 \n Narxi: 15 000", photo=img,
        reply_markup=menucombokids)
    await call.message.delete()


@dp.callback_query_handler(text="2kids")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-41.jpg", "rb")
    await call.message.answer_photo(
        caption=f"Kids Plus   \n Kids plus: EVOS Fri 🍟 \n Bolalar Uchun Bliss Sharbat 🧃 \n Narxi: 15 000", photo=img,
        reply_markup=menucombokids)
    await call.message.delete()


@dp.callback_query_handler(text="3kids")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-41.jpg", "rb")
    await call.message.answer_photo(
        caption=f"Kids Plus   \n Kids plus: EVOS Fri 🍟 \n Bolalar Uchun Bliss Sharbat 🧃 \n Narxi: 15 000", photo=img,
        reply_markup=menucombokids)
    await call.message.delete()


@dp.callback_query_handler(text="Hot-Dog Kids")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-47-04.jpg", "rb")
    await call.message.answer_photo(caption=f"Hot-Dog Kids \n Buyurtmani Sonini Tanlang \n NARXI: 8 000", photo=img,
                                    reply_markup=menukids)
    await call.message.delete()


@dp.callback_query_handler(text="Hot-Dog Classic")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-47-04.jpg", "rb")
    await call.message.answer_photo(caption=f"Hot-Dog classic \n Buyurtmani Sonini Tanlang \n NARXI: 8 000", photo=img,
                                    reply_markup=menuclassic)
    await call.message.delete()


@dp.callback_query_handler(text="Hot-Dog Baguette")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-49-05.jpg", "rb")
    await call.message.answer_photo(caption=f"Hot-Dog Baguette \n NARXI: 11 000", photo=img, reply_markup=menubaguette)
    await call.message.delete()


@dp.callback_query_handler(text="Hot-Dog Baguette Duoble")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-51-06.jpg", "rb")
    await call.message.answer_photo(caption=f"Hot-Dog Baguette Double \n NARXI: 17 000", photo=img,
                                    reply_markup=menubaguetteduoble)
    await call.message.delete()


@dp.callback_query_handler(text="Coca Cola")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-52-33.jpg", "rb")
    await call.message.answer_photo(caption=f"Coca Cola \n NARXI: 9 000", photo=img, reply_markup=menucola)
    await call.message.delete()


@dp.callback_query_handler(text="Pepsi")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-53-26.jpg", "rb")
    await call.message.answer_photo(caption=f"Pepsi \n NARXI: 9 500", photo=img, reply_markup=menupepsi)
    await call.message.delete()


@dp.callback_query_handler(text="Fanta")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-54-50.jpg", "rb")
    await call.message.answer_photo(caption=f"Fanta \n NARXI: 10 500", photo=img, reply_markup=menufanta)
    await call.message.delete()


@dp.callback_query_handler(text="Sprite")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-55-40.jpg", "rb")
    await call.message.answer_photo(caption=f"Sprite \n NARXI: 11 500", photo=img, reply_markup=menusprayt)
    await call.message.delete()


# ------------------------------------

@dp.callback_query_handler(text="t")
async def sample(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi ", photo=img, reply_markup=menulavash)
    await call.message.delete()


@dp.callback_query_handler(text="q")
async def sample(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menulavash)
    await call.message.delete()


@dp.callback_query_handler(text="10e")
async def sample(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menulavash)
    await call.message.delete()



@dp.callback_query_handler(text="w")
async def sample(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menulavash)
    await call.message.delete()


@dp.callback_query_handler(text="y")
async def sample(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menulavash)
    await call.message.delete()



@dp.callback_query_handler(text="u")
async def sample(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menulavash)
    await call.message.delete()


@dp.callback_query_handler(text="i")
async def sample(call: CallbackQuery):
    img = open("image/oq tepalavash(1).jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menulavash)
    await call.message.delete()


@dp.callback_query_handler(text="o")
async def sample(call: CallbackQuery):
    img = open("image/fri.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menufri)
    await call.message.delete()


@dp.callback_query_handler(text="p")
async def sample(call: CallbackQuery):
    img = open("image/fri.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menufri)
    await call.message.delete()


@dp.callback_query_handler(text="a")
async def sample(call: CallbackQuery):
    img = open("image/fri.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menufri)
    await call.message.delete()


@dp.callback_query_handler(text="s")
async def sample(call: CallbackQuery):
    img = open("image/fri.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menufri)
    await call.message.delete()


@dp.callback_query_handler(text="d")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menushaurmagosht)
    await call.message.delete()


@dp.callback_query_handler(text="f")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menushaurmagosht)
    await call.message.delete()


@dp.callback_query_handler(text="g")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menushaurmagosht)
    await call.message.delete()


@dp.callback_query_handler(text="h")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menushaurmagosht)
    await call.message.delete()


@dp.callback_query_handler(text="j")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menushaurmatovuq)
    await call.message.delete()


@dp.callback_query_handler(text="l")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menushaurmatovuq)
    await call.message.delete()


@dp.callback_query_handler(text="x")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menushaurmatovuq)
    await call.message.delete()


@dp.callback_query_handler(text="z")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_05-53-34.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menushaurmatovuq)
    await call.message.delete()


@dp.callback_query_handler(text="x")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-22.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menucheeseburger)
    await call.message.delete()


@dp.callback_query_handler(text="v")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-22.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menucheeseburger)
    await call.message.delete()


@dp.callback_query_handler(text="b")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-13.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menugamburger)
    await call.message.delete()


@dp.callback_query_handler(text="km")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_13-40-13.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menugamburger)
    await call.message.delete()


@dp.callback_query_handler(text="m")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-47-04.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menuhoddog)
    await call.message.delete()


@dp.callback_query_handler(text="1q")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-47-04.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menuhoddog)
    await call.message.delete()


@dp.callback_query_handler(text="opa")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-49-05.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menuhoddog)
    await call.message.delete()


@dp.callback_query_handler(text="3e")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-51-06.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menuhoddog)
    await call.message.delete()


@dp.callback_query_handler(text="4r")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-52-33.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menuichimliklar)
    await call.message.delete()


@dp.callback_query_handler(text="2w")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-53-26.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menuichimliklar)
    await call.message.delete()


@dp.callback_query_handler(text="fanta")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-54-50.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menuichimliklar)
    await call.message.delete()


@dp.callback_query_handler(text="ni")
async def sample(call: CallbackQuery):
    img = open("image/photo_2022-11-14_14-55-40.jpg", "rb")
    await call.message.answer_photo(caption=f"buyurtma qabul qilindi", photo=img, reply_markup=menuichimliklar)
    await call.message.delete()


if __name__ == '__main__':
    executor.start_polling(dp)
