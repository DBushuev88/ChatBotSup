from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token='ВАШ_ТОКЕН_ЗДЕСЬ')
dp = Dispatcher(bot)

@dp.message_handler()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    text = message.text

    with open('keywords.txt', 'r') as file:
        keywords = file.read().splitlines()
    
    if any(keyword in text for keyword in keywords):
        await bot.send_message(user_id, 'Вы использовали ключевое слово!')

    with open('user_ids.txt', 'a') as file:
        file.write(f'{user_id}\n')

if __name__ == '__main__':
    executor.start_polling(dp)
