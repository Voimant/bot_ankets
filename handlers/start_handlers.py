from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards import main_menu_markup

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    user_name = message.from_user.first_name
    print(message.chat.id)
    await message.answer(f'{user_name}, начнем работу?', reply_markup=main_menu_markup)
