from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main_menu_button = [
    [InlineKeyboardButton(text='Создать профиль кандидата', callback_data='create')]
]
main_menu_markup = InlineKeyboardMarkup(inline_keyboard=main_menu_button)

cancel_button = [[InlineKeyboardButton(text="Отмена", callback_data='cancel')]]
cancel_markup = InlineKeyboardMarkup(inline_keyboard=cancel_button)

profile_button = [
    [InlineKeyboardButton(text='Devops', callback_data='Devops')],
    [InlineKeyboardButton(text='Системный Аналитик', callback_data='Системный Аналитик')],
    [InlineKeyboardButton(text='Java', callback_data='Java'), InlineKeyboardButton(text='Python', callback_data='Python')],
    [InlineKeyboardButton(text='qa', callback_data='qa')],
    [InlineKeyboardButton(text='назад', callback_data='back')]
]
profile_markup = InlineKeyboardMarkup(inline_keyboard=profile_button)



def location_markup():
    cites = ["Москва", "Санкт-Петербург", "Рязань", "Брянск", "Вологда", "Ростов-на-Дону", "Нижний Новгород", "Сочи",
             "Екатеринбург",
             "Новосибирск", "Омск", "Барнаул", "Самара", "Казань", "Иннополис", "Балаково", "Хабаровск", "Владивосток",
             ]
    builder = InlineKeyboardBuilder()
    for city in cites:
        builder.row(InlineKeyboardButton(text=str(city), callback_data=str(city)))
    builder.row(InlineKeyboardButton(text=str('Назад'), callback_data='back'))
    builder.adjust(2)
    return builder

work_mode_button = [[
    InlineKeyboardButton(text='Офис', callback_data='офис'),
    InlineKeyboardButton(text='Удалёнка', callback_data='удаленка'),
    InlineKeyboardButton(text='Гибрид', callback_data='гибрид')
]]
work_mode_markup = InlineKeyboardMarkup(inline_keyboard=work_mode_button)

back_button = [[InlineKeyboardButton(text="Назад", callback_data='back')]]
back_markup = InlineKeyboardMarkup(inline_keyboard=back_button)

sender_button = [[InlineKeyboardButton(text="Отправить", callback_data='sender'), InlineKeyboardButton(text="Отмена", callback_data="cancel")]]
sender_markup = InlineKeyboardMarkup(inline_keyboard=sender_button)