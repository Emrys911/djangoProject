import random
import json
from aiogram import Bot, Dispatcher, types
from aiogram.executor import Executor
from get_memes_for_api import get_memes
from get_neiro_memes import get_neiro_memes
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

token = '6701996903:AAG86hAkmORtKPQ-HYpZLquM9hiBNGoEKkg'
bot = Bot(token=token)
disp = Dispatcher(storage=storage)


class RegistrationForm(StatesGroup):
    username = State()
    password = State()
    confirm_password = State()


@disp.message(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Welcome to the registration process! Please, enter your desired username.")
    await RegistrationForm.username.set()


@disp.message(State=RegistrationForm.username)
async def process_username(message: types.Message.StateFSMContext):
    user_username = message.text
    await State.update_data(username=user_username)
    await message.reply("Please, enter your password")
    await RegistrationForm.password.set()


@disp.message(State=RegistrationForm.password)
async def process_password():
    user_password = message.text
    await State.update_data(password=user_password)
    await message.reply("Please, confirm your password")
    await RegistrationForm.confirm_password.set()


@disp.message(State=RegistrationForm.confirm_password)
async def process_confirm_password():
    awaitState.get_data()


username = data.get('username')
password = data.get('password')


@disp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Мем")
    button_2 = types.KeyboardButton(text="Нейросеть")
    keyboard.add(button_1)
    keyboard.add(button_2)
    await message.answer(
        "Для того чтобы получить мем нажмите на кнопку!\n",
        reply_markup=keyboard)


@disp.message_handler(lambda message: message.text == "Мем")
async def parser_memes(message: types.Message):
    with open('memes.json', 'r') as file:
        mem = random.choice(json.load(file)['img'])
    await bot.send_photo(message.chat.id, mem)


@disp.message_handler(lambda message: message.text == "Нейросеть")
async def parser_memes(message: types.Message):
    with open('neiro.json', 'r') as file:
        mem = random.choice(json.load(file)['img'])
    await bot.send_photo(message.chat.id, mem)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Hello,I am gpt_bot')


@bot.message_handler(content_types=['text'])
def talk(message):
    response = openai.Completion.create(
        model="text-davinchi-003",
        prompt=message.text,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_pelaty=0.5
    )
    gpt_text = response['choises'][0]['text']
    bot.send_message(message.chat.id, gpt_text)


if __name__ == '__main__':
    get_memes("https://api.memegen.link/images")
    get_neiro_memes()
    executor.start_polling(disp, skip_updates=True)
    bot.polling(none_stop=True)
