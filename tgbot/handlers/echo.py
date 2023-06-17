from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from tgbot.services.repository import Repo
import time
from tgbot.keyboards.reply import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import markdown





phone_plans = {'Вільний Лайф🤟': {'Ціна': 'від 180 грн / 4 тижні', 'інтернет': 'Безліміт', 'Дзвінки': '1600 хв', 'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/'},
                'Смарт Лайф✌️': {'Ціна': 'від 120 грн / 4 тижні', 'інтернет': '25 ГБ', 'Дзвінки': '800 хв', 'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/'},
                'Просто Лайф👍': {'Ціна': 'від 90 грн / 4 тижні', 'інтернет': '8 ГБ', 'Дзвінки': '300 хв', 'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/'},
                'Platinum Лайф🛎': {'Ціна': 'від 250 грн / 4 тижні', 'інтернет': 'Безліміт', 'Дзвінки': '3000 хв', 'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/'},
                'Шкільний Лайф📚': {'Ціна': 'від 150 грн / 4 тижні', 'інтернет': '7 ГБ', 'Дзвінки': 'Безліміт', 'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/'},
                'Ґаджет⚙': {'Ціна': 'від 90 грн / 12 тижнів', 'інтернет': 'від 150 МБ до безліміту', 'Дзвінки': 'від 15 хв до 50 хв', 'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/gadget-series/'},
                "Смарт Сім'я👨‍👩‍👧‍👦": {'Ціна': 'від 375 грн / 4 тижні', 'інтернет': 'від 20 ГБ до 50 ГБ', 'Дзвінки': 'від 500 хв до 1500 хв', 'url': 'https://www.lifecell.ua/uk/mobilnij-zvyazok/smart-simya-series/'},
               }

# async def after_reg(message: types.Message, state: FSMContext, repo: Repo):
#     answer = await repo.already_registered(username=message.from_user.username)
#     if answer == True:
#         await message.answer("Вітаю!")
#     elif answer == False:
#         await message.answer("Схоже, що вас немає у нашій базі данних, пропоную вам зареєструватися у ній.")
#         time.sleep(1)
#         await message.answer("Для того, щоб зареєструватися надішліть нам свій контакт, для подальшої взаємодії :)", reply_markup=start_phone_kb)

async def add_user(message: types.Message, state:FSMContext, repo: Repo):
    if message.from_user.id == message.contact.user_id:
        await repo.add_user(username=message.from_user.first_name, phonenumber=message.contact.phone_number, id=message.from_user.id)
        print(f"Користувач - {message.from_user.first_name};\nНомер телефону - {message.contact.phone_number}\n")
        await message.answer('Вітаємо у Lifecell!\nЧим я можу вам допомогти?', reply_markup=start_keyboard)
    elif message.from_user.id != message.contact.user_id:
        await message.answer(f"Це не ваш номер!\nБудь ласка дайте нам свій\nсправжній контакт.🫵")
    else:
        await message.answer("Error!")

async def menu_func(message: types.Message, state: FSMContext, repo: Repo):
    await message.answer(text='Оберіть послугу:', reply_markup=menu_keyboard)

async def allphoneplans(message: types.Message, state: FSMContext):
    for plan, details in phone_plans.items():
        link_keyb = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Придбати тариф", url=details['url'])
                ]
            ]
        )
        await message.answer(f"{plan}\n\n{details['Ціна']}\n•Інтернет: {details['інтернет']}\n•Дзвінки: {details['Дзвінки']}", reply_markup=link_keyb)
        time.sleep(0.5)

async def help_command(message: types.Message, state: FSMContext):
    await message.answer("Цей бот був створений для того, щоб люди змогли оформити тариф через телеграм.")
    await message.answer("Як оформити тариф за допомогою нашого бота:\n\n" +
                         "1. У головному меню після реєстрації оберіть пункт \"Тарифи\".\n" +
                         "2. Після цього оберіть свій варіант (подивитися усі тарифи або підібрати тариф під себе).\n" +
                         "3. Після того, як ви обрали потрібний тариф, натисніть на кнопку під обраним тарифом " +
                         "та перейдіть на офіційний сайт Lifecell, де вам вже зможуть більш детально показати, " +
                         "як підключити тариф.")
    await message.answer("Як змінити тарифний план на Lifecell (Лайф):\n\n" +
                         "1. Зателефонуйте за безкоштовним номером 5433.\n" +
                         "2. У голосовому меню виберіть пункт 4 - «Доступні для підключення тарифні плани і ваш баланс».\n" +
                         "3. Після цього вам запропонують список доступних тарифів. Натиснувши відповідну кнопку, " +
                         "ви зможете змінити свій тариф і перейти на інший.")

result_list = []

async def phoneplaneforme1(message: types.Message, state: FSMContext):
    await message.answer('Для того, щоб підібрати найкращий для вас тариф, вам слід пройти опитування..')
    time.sleep(0.75)
    await message.answer('Крок 1 з 5:')
    await message.answer('•Яка ціна тарифу для вас є оптимальною?', reply_markup=phone_var_kb3)



async def phoneplaneforme2(message: types.Message, state: FSMContext):
    time.sleep(0.75)
    await message.answer('Крок 2 з 5:')
    await message.answer('•Бажаєте лімітний чи безлімітний інтернет?', reply_markup=phone_var_kb)
    result_list.append(message.text)

async def phoneplaneforme3(message: types.Message, state: FSMContext):
    time.sleep(0.75)
    await message.answer('Крок 3 з 5:')
    await message.answer('•Бажаєте лімітні чи безлімітні дзвінки?', reply_markup=phone_var_kb2)
    result_list.append(message.text)

async def phoneplaneforme4(message: types.Message, state: FSMContext):
    result_list.append(message.text)
    time.sleep(0.75)
    print(result_list)
    def keyboard(link):
        link_keyb = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Придбати тариф", url=link)
                ]
            ]
        )
        return link_keyb
    await message.answer('Крок 4 з 5:')
    if result_list[0] == '90 грн' and result_list[1] == "Лімітний":
        print(1)
        await message.answer('Просто Лайф👍\n\nвід 90 грн / 4 тижні\n•Інтернет: 8 ГБ\n•Дзвінки: 300 хв',
                             reply_markup=keyboard(
                                 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/'))
    elif result_list[0] == '120 грн':
        print(2)
        await message.answer('Смарт Лайф✌️\n\nвід 120 грн / 4 тижні\n•Інтернет: 25 ГБ\n•Дзвінки: 800 хв',
                             reply_markup=keyboard(
                                 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/'))
    elif result_list[0] == '150 грн':
        print(3)
        await message.answer('Шкільний Лайф📚️\n\nвід 150 грн / 4 тижні\n•Інтернет: 7 ГБ\n•Дзвінки: Безліміт',
                             reply_markup=keyboard(
                                 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/'))
    elif result_list[0] == '180 грн':
        print(4)
        await message.answer('Вільний Лайф🤟\n\nвід 180 грн / 4 тижні\n•Інтернет: Безліміт\n•Дзвінки: 1600 хв',
                             reply_markup=keyboard('https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/'))

    elif result_list[0] == '250 грн':
        print(5)
        await message.answer('Platinum Лайф🛎\n\nвід 250 грн / 4 тижні\n•Інтернет: Безліміт\n•Дзвінки: 3000 хв',
                             reply_markup=keyboard(
                                 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/'))
    elif result_list[0] == '375 грн':
        print(6)
        await message.answer('Platinum Лайф🛎\n\nвід 250 грн / 4 тижні\n•Інтернет: Безліміт\n•Дзвінки: 3000 хв',
                             reply_markup=keyboard(
                                 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/'))
    elif result_list[0] == '90 грн' and result_list[1] == "Безлімітний":
        print(7)
        await message.answer('Ґаджет⚙️\n\nвід 90 грн / 4 тижні\n•Інтернет: від 150 МБ до безліміту\n•Дзвінки: від 15 хв до 50 хв',
                             reply_markup=keyboard(
                                 'https://www.lifecell.ua/uk/mobilnij-zvyazok/gadget-series/'))
    else:
        print('error')
    time.sleep(0.75)
    result_list.clear()
    await message.answer('Крок 5 з 5:')
    await message.answer('Чи підійшов вам тариф?', reply_markup=rate_kb)

async def phone_answer(message: types.Message, state: FSMContext):
    time.sleep(0.5)
    await message.answer('Дякую за відгук!')
    await message.answer('Чим я ще можу вам допомогти?', reply_markup=start_keyboard)

def register_echo(dp: Dispatcher):
    dp.register_message_handler(phone_answer, text="Ні :(")
    dp.register_message_handler(phone_answer, text="Так :D")
    dp.register_message_handler(phoneplaneforme4, text="Безлімітні")
    dp.register_message_handler(phoneplaneforme4, text="Лімітні")
    dp.register_message_handler(phoneplaneforme3, text="Безлімітний")
    dp.register_message_handler(phoneplaneforme3, text="Лімітний")
    dp.register_message_handler(phoneplaneforme2, text='375 грн')
    dp.register_message_handler(phoneplaneforme2, text='250 грн')
    dp.register_message_handler(phoneplaneforme2, text='180 грн')
    dp.register_message_handler(phoneplaneforme2, text='150 грн')
    dp.register_message_handler(phoneplaneforme2, text='120 грн')
    dp.register_message_handler(phoneplaneforme2, text='90 грн')
    dp.register_message_handler(phoneplaneforme1, text='Підібрати тариф під себе')
    dp.register_message_handler(help_command, commands=["help"])
    dp.register_message_handler(allphoneplans, text='Усі тарифи')
    dp.register_message_handler(menu_func, text='Тарифи')
    dp.register_message_handler(add_user, state="*", content_types=types.ContentTypes.CONTACT)

