from loader import dp, bot
from aiogram import executor
from handlers import *
from aiogram.types import BotCommand


async def setup_bot_commands(dp):
    bot_commands = [
        BotCommand(command="/help", description="Помощь"),
        BotCommand(command="/start", description="Начать")
    ]
    await bot.set_my_commands(bot_commands)

if __name__ == '__main__':
    print("Starting Questern bot")
    executor.start_polling(dp, skip_updates=True, on_startup=setup_bot_commands)
    
