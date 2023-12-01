from aiogram import Router, F, enums
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards import main_menu_markup, sender_markup
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from keyboards import cancel_markup, profile_markup, location_markup, work_mode_markup, back_markup
from aiogram import Dispatcher, Bot
from config import TOKEN
from DB.db_main import add_candidats
from DB.DB import conn
bot = Bot(token=TOKEN)
router = Router()



class Fsm_anket(StatesGroup):
    profile = State()
    name = State()
    location = State()
    salary = State()
    work_mode = State()
    stack = State()
    experience = State()
    resume = State()
    coment = State()
    hashtag = State()
    candidat = State()
    check = State()


@router.callback_query(F.data == 'cancel')
async def cancel(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer('Вы вернулись в главное меню', reply_markup=main_menu_markup)


@router.callback_query(F.data == 'create')
async def get_name(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите фамилию и инициалы кандидата", reply_markup=cancel_markup)
    await state.set_state(Fsm_anket.name)


@router.message(Fsm_anket.name)
async def get_profile(message: Message, state: FSMContext):
    try:
        await state.update_data(name=message.text)
        await message.answer("Выберете профиль кандидата, если нужного профиля нет, введите в ручную",
                             reply_markup=profile_markup)
        await state.set_state(Fsm_anket.profile)
    except Exception as e:
        await message.answer("Произошла ошибка, повторите действие")
        await state.set_state(Fsm_anket.name)

@router.message(Fsm_anket.profile)
async def get_location(mess: Message, state: FSMContext):
    await state.update_data(profile=mess.text)
    await mess.answer("Выберете город кандидата, если в списке нет,"
                              "введите город вручную", reply_markup=location_markup().as_markup())
    await state.set_state(Fsm_anket.salary)


@router.callback_query(Fsm_anket.profile)
async def get_location(call: CallbackQuery, state: FSMContext):
    if call.data == 'back':
        print(call.data)
        await state.update_data(name=None)
        await state.set_state(Fsm_anket.name)
        await call.message.answer("Введите фамилию и инициалы кандидата", reply_markup=cancel_markup)
    else:
        await state.update_data(profile=call.data)
        await call.message.answer("Выберете город кандидата, если в списке нет,"
                                  "введите город вручную", reply_markup=location_markup().as_markup())
        await state.set_state(Fsm_anket.salary)

@router.callback_query(Fsm_anket.salary)
async def get_salary(call: CallbackQuery, state: FSMContext):
    if call.data == 'back':
        await state.update_data(profile=None)
        await call.message.answer("Выберете профиль кандидата", reply_markup=profile_markup)
        await state.set_state(Fsm_anket.profile)
    else:
        await state.update_data(location=call.data)
        await call.message.answer("Укажите зарплатные ожидания", reply_markup=back_markup)
        await state.set_state(Fsm_anket.work_mode)

@router.message(Fsm_anket.salary)
async def get_salary(mess: CallbackQuery, state: FSMContext):
    await state.update_data(location=mess.text)
    await mess.answer("Укажите зарплатные ожидания", reply_markup=back_markup)
    await state.set_state(Fsm_anket.work_mode)

@router.message(Fsm_anket.work_mode)
async def get_work_mode(mess: Message, state: FSMContext):
    await state.update_data(salary=mess.text)
    await mess.answer("Какой формат работы рассматривает кандидат? Если в списке нет, напишите другой вариант",
                      reply_markup=work_mode_markup)
    await state.set_state(Fsm_anket.stack)

@router.callback_query(Fsm_anket.stack)
async def get_stack(call: CallbackQuery, state: FSMContext):
    await state.update_data(work_mode=call.data)
    await call.message.answer("Укажите стэк кандидата", reply_markup=cancel_markup)
    await state.set_state(Fsm_anket.experience)

@router.message(Fsm_anket.stack)
async def get_stack(mess: Message, state: FSMContext):
    await state.update_data(work_mode=mess.text)
    await mess.answer("Укажите стэк кандидата", reply_markup=cancel_markup)
    await state.set_state(Fsm_anket.experience)

@router.message(Fsm_anket.experience)
async def get_experience(mess: Message, state: FSMContext):
    await state.update_data(stack=mess.text)
    await mess.answer('Какой у кандидата профильный опыт работы?', reply_markup=cancel_markup)
    await state.set_state(Fsm_anket.coment)

@router.message(Fsm_anket.coment)
async def get_coment(mess: Message, state: FSMContext):
    await state.update_data(experience=mess.text)
    await mess.answer("Ваши комментарии", reply_markup=cancel_markup)
    await state.set_state(Fsm_anket.resume)

@router.message(Fsm_anket.resume)
async def get_resume(mess: Message, state: FSMContext):
    await state.update_data(coment=mess.text)
    await mess.answer("Укажите ссылку на резюме", reply_markup=cancel_markup)
    await state.set_state(Fsm_anket.hashtag)

@router.message(Fsm_anket.hashtag)
async def get_hastag(mess: Message, state: FSMContext):
    await state.update_data(resume=mess.text)
    await mess.answer("Укажите Хештеги", reply_markup=cancel_markup)
    await state.set_state(Fsm_anket.candidat)

@router.message(Fsm_anket.candidat)
async def get_candidats(mess: Message, state: FSMContext):
    await state.update_data(hashtag=mess.text)
    data = await state.get_data()
    text = (f'Профиль: {data["profile"]}\n'
            f'Фамилия и инициалы: {data["name"]}\n'
            f'Локация: {data["location"]}\n'
            f'Стаж работы профильный: {data["experience"]}\n'
            f'З/П ожидания: {data["salary"]}\n'
            f'Режим работы: {data["work_mode"]}\n'
            f'Стэк технологий: {data["stack"]}\n'
            f'Комментарий от рекрутера: {data["coment"]}\n'
            f'Резюме: {data["resume"]}\n'
            f'Хэштеги: {data["hashtag"]}\n\n'
            f'<i>Оставьте комментарий с вашим именем и фамилией, если берете в работу</i>')
    await mess.answer(text, parse_mode="HTML", reply_markup=sender_markup)
    await state.set_state(Fsm_anket.check)


@router.callback_query(Fsm_anket.check)
async def get_check(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    hashtag = data["hashtag"]
    count = 0
    for symbol in hashtag:
        if symbol == '#':
            count += 1
    if count == 3:
        text = (f'Профиль: {data["profile"]}\n'
                f'Фамилия и инициалы: {data["name"]}\n'
                f'Локация: {data["location"]}\n'
                f'Стаж работы профильный: {data["experience"]}\n'
                f'З/П ожидания: {data["salary"]}\n'
                f'Режим работы: {data["work_mode"]}\n'
                f'Стэк технологий: {data["stack"]}\n'
                f'Комментарий от рекрутера: {data["coment"]}\n'
                f'Резюме: {data["resume"]}\n'
                f'Хэштеги: {data["hashtag"]}\n\n'
                f'<i>Оставьте комментарий с вашим именем и фамилией, если берете в работу</i>')
        await call.message.answer("Кандидат на проверку направлен", parse_mode="HTML")
        await bot.send_message(509695580, text)
        add_candidats(data["profile"], data["name"], data["location"], data["salary"], data["work_mode"], data["stack"],
                      data["experience"], data["resume"], data["coment"], data["hashtag"])
        conn.commit()
        await state.clear()
    elif count == 4:
        text = (f'Профиль: {data["profile"]}\n'
                f'Фамилия и инициалы: {data["name"]}\n'
                f'Локация: {data["location"]}\n'
                f'Стаж работы профильный: {data["experience"]}\n'
                f'З/П ожидания: {data["salary"]}\n'
                f'Режим работы: {data["work_mode"]}\n'
                f'Стэк технологий: {data["stack"]}\n'
                f'Комментарий от рекрутера: {data["coment"]}\n'
                f'Резюме: {data["resume"]}\n'
                f'Хэштеги: {data["hashtag"]}\n\n'
                f'<i>Оставьте комментарий с вашим именем и фамилией, если берете в работу</i>')
        await bot.send_message(537554059, text)
        await call.message.answer("Кандидат на проверку направлен", parse_mode="HTML")
        add_candidats(data["profile"], data["name"], data["location"], data["salary"], data["work_mode"], data["stack"],
                      data["experience"], data["resume"], data["coment"], data["hashtag"])
        conn.commit()

        await state.clear()
    else:
        await call.message.answer("Нужно ввести 3 или 4 тега")
        await state.set_state(Fsm_anket.candidat)
