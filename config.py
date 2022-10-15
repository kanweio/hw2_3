from aiogram import Bot, Dispatcher
from decouple import config
t0ken = config("TOKEN")
bot = Bot(t0ken)
dp = Dispatcher(bot=bot)
ADMINS = [982133561, ]