from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup


class Fsm1(StatesGroup):
    name = State()
    family = State()




async def my_name(x, state: FSMContext):
    x = input("Введите ваше имя")


