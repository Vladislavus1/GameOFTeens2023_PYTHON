from aiogram import Dispatcher
from aiogram.types import Message
from tgbot.keyboards.reply import start_keyboard, start_phone_kb
import time
from tgbot.services.repository import Repo


async def admin_start(message: Message, repo: Repo):
    answer1 = await repo.already_registered(id=message.from_user.id)
    print(answer1)
    if answer1 == True:
        await message.answer(f"З поверненням {message.from_user.first_name}!")
        time.sleep(0.75)
        await message.answer('Чим я можу вам допомогти?', reply_markup=start_keyboard)
    elif answer1 == False:
        await message.answer_photo(
                "https://img2-frankfurt.cf-rabota.com.ua/1014/2021/07/img/071eaf79df734f4e28ee.png",
                caption=f"꧁🇺🇦🇺🇦Привіт, {message.from_user.first_name}🇺🇦🇺🇦꧂\n\n•Вас вітає телеграм-бот компанії Lifecell, провідний оператор мобільного зв'язку в Україні та партнер GoITeens.")
        time.sleep(1.15)
        answer2 = await repo.already_registered(id=message.from_user.id)
        print(answer2)
        if answer2 == True:
            await message.answer('Чим я можу вам допомогти?', reply_markup=start_keyboard)
        elif answer2 == False:
            await message.answer("Схоже, що вас немає у нашій базі данних, пропоную вам зареєструватися у ній.")
            time.sleep(1)
            await message.answer("Для того, щоб зареєструватися надішліть нам свій контакт, для подальшої взаємодії :)", reply_markup=start_phone_kb)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*")
