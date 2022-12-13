from aiogram import executor, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from data_calculation import calculation
from keyboards import *
from config import TOKEN
from data_base import sqlite_db


storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)


async def on_startup(_):
    sqlite_db.sql_start()
    print("Запущен бот и база данных из файла ", "\033[4m\033[37m\033[44m{}\033[0m"
          .format('221211_PTO!'))


class AnketaSG(StatesGroup):
    Q_1 = State()
    Q_2 = State()
    Q_3 = State()
    Q_4 = State()
    Q_5 = State()
    Q_6 = State()
    Q_7 = State()
    Q_8 = State()
    Q_9 = State()
    Q_10 = State()
    Q_11 = State()
    Q_12 = State()
    Q_13 = State()
    Q_14 = State()
    Q_15 = State()
    Q_16 = State()
    Q_17 = State()
    Q_18 = State()
    Q_19 = State()
    Q_20 = State()
    Q_21 = State()
    Q_22 = State()
    Q_23 = State()
    Q_24 = State()
    Q_25 = State()
    Q_26 = State()
    Q_27 = State()
    Q_28 = State()
    Q_29 = State()
    Q_30 = State()
    Q_31 = State()
    Q_32 = State()
    Q_33 = State()
    Q_34 = State()
    Q_35 = State()
    Q_36 = State()
    Q_37 = State()
    Q_38 = State()
    Q_39 = State()
    Q_40 = State()
    Q_41 = State()
    Q_42 = State()
    Q_43 = State()
    Q_44 = State()
    Q_45 = State()
    Q_46 = State()
    Q_47 = State()
    Q_48 = State()
    Q_49 = State()
    Q_50 = State()
    Q_51 = State()
    Q_52 = State()
    Q_53 = State()
    Q_54 = State()
    Q_55 = State()
    Q_56 = State()
    Q_57 = State()
    Q_58 = State()
    Q_59 = State()
    Q_60 = State()
    Q_61 = State()
    Q_62 = State()
    Q_63 = State()
    Q_64 = State()
    Q_65 = State()


# обрабатывает команду '/завершить' для прерывания процесса
@dp.message_handler(commands=['завершить'], state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    if state is None:
        return

    await state.finish()
    await message.reply('Вы прервали прохождение анкеты!',
                        reply_markup=btn_proyti())


@dp.message_handler(commands=['старт', 'start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!\nЭто анкета для "
                         f"прогнозирования степени риска пролапса тазовых органов у женщин.\n"
                         f"Чтобы начать нажмите кнопку /пройти_тест",
                         reply_markup=btn_proyti())  # выводит клавишу '/пройти_тест'


@dp.message_handler(lambda message: not message.text.
                    isdigit() or float(message.text) > 100 or float(message.text) < 10,
                    state=AnketaSG.Q_1)
async def check_age(message: types.Message):
    await message.reply('Введите корректный возраст!')


@dp.message_handler(commands=['пройти_тест'])
@dp.message_handler(Text(equals='пройти_тест',
                         ignore_case=True))
async def cmd_create(message: types.Message) -> None:
    await message.reply("Вопрос № 1\n"
                        "Укажите, пожалуйста, сколько Вам полных лет:",
                        reply_markup=btn_cancel())
    await AnketaSG.Q_1.set()  # установили состояние


@dp.message_handler(lambda message: not message.text.
                    isdigit() or float(message.text) > 20 or float(message.text) < 1,
                    state=AnketaSG.Q_2)
async def check_age(message: types.Message):
    await message.reply('Введите корректный возраст!')


@dp.message_handler(state=AnketaSG.Q_1)
async def ques_1(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['full_name'] = message.from_user.full_name
        data['Q_1'] = message.text

    await AnketaSG.next()
    await message.reply("Вопрос № 2\n"
                        "Укажите, в каком возрасте (полных лет) у Вас начались менструации: ")


@dp.message_handler(lambda message: not message.text.
                    isdigit() or float(message.text) > 100 or float(message.text) < 10,
                    state=AnketaSG.Q_3)
async def check_age(message: types.Message):
    await message.reply('Введите корректный возраст!')


@dp.message_handler(state=AnketaSG.Q_2)
async def ques_2(message: types.Message,
                 state: FSMContext) -> None:
    async with state.proxy() as data:
        data['Q_2'] = message.text

    await message.reply("Вопрос № 3\n"
                        "Укажите, в каком возрасте (полных лет) у Вас прекратились менструации:")
    await AnketaSG.next()


@dp.message_handler(state=AnketaSG.Q_3)
async def ques_3(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['Q_3'] = message.text

    await message.reply("Вопрос № 4\n"
                        "Укажите у кого из родственников было опущение и/или"
                        " выпадение половых органов и грыжи:",
                        reply_markup=btns_q_4_rodstvenniki())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_4)
async def ques_4(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Нет пролапса_q_4':
        async with state.proxy() as data:
            data['Q_4'] = 'Нет пролапса'
    elif callback.data == 'У матери_q_4':
        async with state.proxy() as data:
            data['Q_4'] = 'У матери'
    else:
        async with state.proxy() as data:
            data['Q_4'] = 'У родственников'

    await callback.message.answer("Вопрос № 5\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Астенический тип телосложения или недостаточная масса тела: ",
                                  reply_markup=btn_da_net_q_5())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_5)
async def ques_5(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_5':
        async with state.proxy() as data:
            data['Q_5'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_5'] = 'Нет'

    await callback.message.answer("Вопрос № 6\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Отсутствие стрий на коже передней брюшной стенки "
                                  "(у женщин, имевших в анамнезе роды): ",
                                  reply_markup=btn_da_net_q_6())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_6)
async def ques_6(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_6':
        async with state.proxy() as data:
            data['Q_6'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_6'] = 'Нет'

    await callback.message.answer("Вопрос № 7\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Нарушение рефракции в возрасте до 40 лет: ",
                                  reply_markup=btn_da_net_q_7())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_7)
async def ques_7(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_7':
        async with state.proxy() as data:
            data['Q_7'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_7'] = 'Нет'

    await callback.message.answer("Вопрос № 8\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Мышечная гипотония и низкие показатели манометрии: ",
                                  reply_markup=btn_da_net_q_8())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_8)
async def ques_8(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_8':
        async with state.proxy() as data:
            data['Q_8'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_8'] = 'Нет'

    await callback.message.answer("Вопрос № 9\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Уплощение свода стопы: ",
                                  reply_markup=btn_da_net_q_9())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_9)
async def ques_9(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_9':
        async with state.proxy() as data:
            data['Q_9'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_9'] = 'Нет'

    await callback.message.answer("Вопрос № 10\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Склонность к легкому образованию синяков, повышенная "
                                  "кровоточивость тканей: ",
                                  reply_markup=btn_da_net_q_10())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_10)
async def ques_10(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_10':
        async with state.proxy() as data:
            data['Q_10'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_10'] = 'Нет'

    await callback.message.answer("Вопрос № 11\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Кровотечение в послеродовом периоде: ",
                                  reply_markup=btn_da_net_q_11())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_11)
async def ques_11(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_11':
        async with state.proxy() as data:
            data['Q_11'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_11'] = 'Нет'

    await callback.message.answer("Вопрос № 12\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Вегето-сосудистые дисфункции: ",
                                  reply_markup=btn_da_net_q_12())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_12)
async def ques_12(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_12':
        async with state.proxy() as data:
            data['Q_12'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_12'] = 'Нет'

    await callback.message.answer("Вопрос № 13\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Нарушение сердечного ритма и проводимости (ЭКГ): ",
                                  reply_markup=btn_da_net_q_13())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_13)
async def ques_13(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_13':
        async with state.proxy() as data:
            data['Q_13'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_13'] = 'Нет'

    await callback.message.answer("Вопрос № 14\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Сколиоз, кифоз, кифосколиоз: ",
                                  reply_markup=btn_da_net_q_14())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_14)
async def ques_14(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_14':
        async with state.proxy() as data:
            data['Q_14'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_14'] = 'Нет'

    await callback.message.answer("Вопрос № 15\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Плоскостопие 2-3 степени: ",
                                  reply_markup=btn_da_net_q_15())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_15)
async def ques_15(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_15':
        async with state.proxy() as data:
            data['Q_15'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_15'] = 'Нет'

    await callback.message.answer("Вопрос № 16\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Эластоз кожи: ",
                                  reply_markup=btn_da_net_q_16())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_16)
async def ques_16(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_16':
        async with state.proxy() as data:
            data['Q_16'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_16'] = 'Нет'

    await callback.message.answer("Вопрос № 17\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Гиперподвижность суставов, склонность к вывихам, "
                                  "растяжениям связочного аппарата суставов: ",
                                  reply_markup=btn_da_net_q_17())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_17)
async def ques_17(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_17':
        async with state.proxy() as data:
            data['Q_17'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_17'] = 'Нет'

    await callback.message.answer("Вопрос № 18\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Склонность к аллергическим реакциям и "
                                  "простудным заболеваниям; тонзилэктомия: ",
                                  reply_markup=btn_da_net_q_18())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_18)
async def ques_18(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_18':
        async with state.proxy() as data:
            data['Q_18'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_18'] = 'Нет'

    await callback.message.answer("Вопрос № 19\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Варикозная болезнь, геморрой: ",
                                  reply_markup=btn_da_net_q_19())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_19)
async def ques_19(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_19':
        async with state.proxy() as data:
            data['Q_19'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_19'] = 'Нет'

    await callback.message.answer("Вопрос № 20\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Дискинезия желчевыводящих путей: ",
                                  reply_markup=btn_da_net_q_20())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_20)
async def ques_20(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_20':
        async with state.proxy() as data:
            data['Q_20'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_20'] = 'Нет'

    await callback.message.answer("Вопрос № 21\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Нарушение эвакуационной функции ЖКТ: ",
                                  reply_markup=btn_da_net_q_21())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_21)
async def ques_21(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_21':
        async with state.proxy() as data:
            data['Q_21'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_21'] = 'Нет'

    await callback.message.answer("Вопрос № 22\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Угроза преждевременных родов на сроке 32 - 35 недель беременности "
                                  "и/или преждевременные роды: ",
                                  reply_markup=btn_da_net_q_22())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_22)
async def ques_22(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_22':
        async with state.proxy() as data:
            data['Q_22'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_22'] = 'Нет'

    await callback.message.answer("Вопрос № 23\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Быстрые и стремительные роды в анамнезе с или без "
                                  "гипотонического кровотечения в 3-ем периоде родов: ",
                                  reply_markup=btn_da_net_q_23())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_23)
async def ques_23(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_23':
        async with state.proxy() as data:
            data['Q_23'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_23'] = 'Нет'

    await callback.message.answer("Вопрос № 24\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Пролапс гениталий или грыжи у родственников первой линии: ",
                                  reply_markup=btn_da_net_q_24())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_24)
async def ques_24(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_24':
        async with state.proxy() as data:
            data['Q_24'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_24'] = 'Нет'

    await callback.message.answer("Вопрос № 25\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Грыжи: ",
                                  reply_markup=btn_da_net_q_25())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_25)
async def ques_25(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_25':
        async with state.proxy() as data:
            data['Q_25'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_25'] = 'Нет'

    await callback.message.answer("Вопрос № 26\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Спланхноптоз: ",
                                  reply_markup=btn_da_net_q_26())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_26)
async def ques_26(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_26':
        async with state.proxy() as data:
            data['Q_26'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_26'] = 'Нет'

    await callback.message.answer("Вопрос № 27\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Варикозная болезнь и геморрой (оперативное лечение), "
                                  "хроническая венозная недостаточность с трофическими нарушениями : ",
                                  reply_markup=btn_da_net_q_27())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_27)
async def ques_27(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_27':
        async with state.proxy() as data:
            data['Q_27'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_27'] = 'Нет'

    await callback.message.answer("Вопрос № 28\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Привычные вывихи суставов или вывихи более 2-ух суставов: ",
                                  reply_markup=btn_da_net_q_28())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_28)
async def ques_28(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_28':
        async with state.proxy() as data:
            data['Q_28'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_28'] = 'Нет'

    await callback.message.answer("Вопрос № 29\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Нарушения моторной функции ЖКТ, подтвержденные инструментальными "
                                  "методами исследования (рентгенологическими, эндоскопическими): ",
                                  reply_markup=btn_da_net_q_29())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_29)
async def ques_29(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_29':
        async with state.proxy() as data:
            data['Q_29'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_29'] = 'Нет'

    await callback.message.answer("Вопрос № 30\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Дивертикулы, долихосигма: ",
                                  reply_markup=btn_da_net_q_30())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_30)
async def ques_30(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_30':
        async with state.proxy() as data:
            data['Q_30'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_30'] = 'Нет'

    await callback.message.answer("Вопрос № 31\n"
                                  "Ваши особенности. Наблюдается ли у Вас данный фактор? "
                                  "Поливалентная аллергия, тяжелые анафилактические реакции: ",
                                  reply_markup=btn_da_net_q_31())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_31)
async def ques_31(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_31':
        async with state.proxy() as data:
            data['Q_31'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_31'] = 'Нет'

    await callback.message.answer("Вопрос № 32\n"
                                  "Количество родов. "
                                  "Укажите, сколько у Вас было родов всего: ",
                                  reply_markup=btns_q_32_kolichestvo_rodov())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_32)
async def ques_32(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Не рожала_q_32':
        async with state.proxy() as data:
            data['Q_32'] = 'Не рожала'
    elif callback.data == '1_q_32':
        async with state.proxy() as data:
            data['Q_32'] = '1'
    elif callback.data == '2_q_32':
        async with state.proxy() as data:
            data['Q_32'] = '2'
    else:
        async with state.proxy() as data:
            data['Q_32'] = '3 и более'

    await callback.message.answer("Вопрос № 33\n"
                                  "Возраст первых родов. "
                                  "Укажите, в каком возрасте (полных лет) у Вас были первые роды: ")
    await AnketaSG.next()


@dp.message_handler(lambda message: not message.text.
                    isdigit() or float(message.text) > 50 or float(message.text) < 10,
                    state=AnketaSG.Q_33)
async def check_age(message: types.Message):
    await message.reply('Введите корректный возраст!')


@dp.message_handler(state=AnketaSG.Q_33)
async def ques_33(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['Q_33'] = message.text

    await message.reply("Вопрос № 34\n"
                        "Масса тела. Укажите, сколько Вы весите (в КГ): ")
    await AnketaSG.next()


@dp.message_handler(lambda message: not message.text.
                    isdigit() or float(message.text) > 200 or float(message.text) < 30,
                    state=AnketaSG.Q_34)
async def check_age(message: types.Message):
    await message.reply('Введите корректный вес!')


@dp.message_handler(state=AnketaSG.Q_34)
async def ques_34(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['Q_34'] = message.text

    await message.reply("Вопрос № 35\n"
                        "Рост. Укажите Ваш рост (в САНТИМЕТРАХ!):")
    await AnketaSG.next()


@dp.message_handler(lambda message: not message.text.
                    isdigit() or float(message.text) > 300 or float(message.text) < 120,
                    state=AnketaSG.Q_35)
async def check_age(message: types.Message):
    await message.reply('Введите корректный рост!')


@dp.message_handler(state=AnketaSG.Q_35)
async def ques_35(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['Q_35'] = message.text

    await message.reply("Вопрос № 36\n"
                        "Потребление алкоголя. "
                        "Укажите, употребляете ли Вы алкоголь "
                        "(или, быть может, потребляли ранее):",
                        reply_markup=btns_q_36_alcogol())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_36)
async def ques_36(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Не потребляю_q_36':
        async with state.proxy() as data:
            data['Q_36'] = 'Не потребляю'
    elif callback.data == 'Потребляла ранее_q_36':
        async with state.proxy() as data:
            data['Q_36'] = 'Потребляла ранее'
    else:
        async with state.proxy() as data:
            data['Q_36'] = 'Употребляю'

    await callback.message.answer("Вопрос № 37\n"
                                  "Табакокурение. "
                                  "Укажите, курите ли Вы?: ",
                                  reply_markup=btns_q_37_tabak())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_37)
async def ques_37(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Нет, не курю_q_37':
        async with state.proxy() as data:
            data['Q_37'] = 'Нет, не курю'
    elif callback.data == 'Бросила_q_37':
        async with state.proxy() as data:
            data['Q_37'] = 'Ранее курила, потом бросила'
    else:
        async with state.proxy() as data:
            data['Q_37'] = 'Курю'

    await callback.message.answer("Вопрос № 38\n"
                                  "Образ жизни. "
                                  "Укажите, каков Ваш образ жизни: ",
                                  reply_markup=btns_q_38_obraz_zhizni())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_38)
async def ques_38(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Нормальный_q_38':
        async with state.proxy() as data:
            data['Q_38'] = 'Нормальный'
    elif callback.data == 'Малоподвижный_q_38':
        async with state.proxy() as data:
            data['Q_38'] = 'Малоподвижный'
    else:
        async with state.proxy() as data:
            data['Q_38'] = 'Тяжелый труд'

    await callback.message.answer("Вопрос № 39\n"
                                  "Масса плода (гр.). "
                                  "Укажите массу плода "
                                  "(если родов было несколько, то укажите наибольшую массу):")
    await AnketaSG.next()


@dp.message_handler(lambda message: not message.text.
                    isdigit() or float(message.text) > 7000 or float(message.text) < 500, state=AnketaSG.Q_39)
async def check_age(message: types.Message):
    await message.reply('Введите корректный рост!')


@dp.message_handler(state=AnketaSG.Q_39)
async def ques_39(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['Q_39'] = message.text

    await message.reply("Вопрос № 40\n"
                        "Травмы промежности. "
                        "Укажите, были ли у вас травмы промежности и органов малого таза в родах "
                        "(разрывы шейки матки, стенок влагалища, промежности, "
                        "наружных половых расхождение швов)?:",
                        reply_markup=btns_q_40_travmy_promezhnosti())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_40)
async def ques_40(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_40':
        async with state.proxy() as data:
            data['Q_40'] = 'Да'
    elif callback.data == 'Нет_q_40':
        async with state.proxy() as data:
            data['Q_40'] = 'Нет'
    else:
        async with state.proxy() as data:
            data['Q_40'] = 'Разрыв промежности IV степени'

    await callback.message.answer("Вопрос № 41\n"
                                  "Акушерские операции. "
                                  "Укажите, были ли у вас операции на промежности в родах "
                                  "(эпизиотомия, перинеотомия, ручное отделение плаценты и "
                                  "выделение последа, наложение щипцов)?",
                                  reply_markup=btns_q_41_akusherskie_operacii())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_41)
async def ques_41(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_41':
        async with state.proxy() as data:
            data['Q_41'] = 'Да'
    elif callback.data == 'Нет_q_41':
        async with state.proxy() as data:
            data['Q_41'] = 'Нет'
    else:
        async with state.proxy() as data:
            data['Q_41'] = 'Наложение щипцов'

    await callback.message.answer("Вопрос № 42\n"
                                  "Расстройства функции тазовых органов. "
                                  "Укажите, были ли у вас расстройства функции тазовых органов "
                                  "(острая задержка мочи, геморрой после родов, анальная трещина, "
                                  "недержание мочи, газов, запоры)?",
                                  reply_markup=btn_da_net_q_42())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_42)
async def ques_42(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_42':
        async with state.proxy() as data:
            data['Q_42'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_42'] = 'Нет'

    await callback.message.answer("Вопрос № 43\n"
                                  "Экстрагенитальные заболевания во время беременности. "
                                  "Укажите, какие были у вас заболевания и осложнения в период беременности, "
                                  "родов и послеродовом периоде (преэклампсия, эклампсия, анемия, "
                                  "недостаточный рост плода, гестационный сахарный диабет)?",
                                  reply_markup=btn_da_net_q_43())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_43)
async def ques_43(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_43':
        async with state.proxy() as data:
            data['Q_43'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_43'] = 'Нет'

    await callback.message.answer("Вопрос № 44\n"
                                  "Преждевременные роды. "
                                  "Укажите, были ли у Вас когда-либо преждевременные роды?",
                                  reply_markup=btn_da_net_q_44())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_44)
async def ques_44(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_44':
        async with state.proxy() as data:
            data['Q_44'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_44'] = 'Нет'

    await callback.message.answer("Вопрос № 45\n"
                                  "Воспалительные заболевания половых органов. "
                                  "Укажите, были ли у Вас воспаления придатков матки, "
                                  "матки, шейки матки (цервицит), влагалища (кольпит), "
                                  "прямой кишки (анальный зуд), мочевого пузыря (цистит)?",
                                  reply_markup=btn_da_net_q_45())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_45)
async def ques_45(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_45':
        async with state.proxy() as data:
            data['Q_45'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_45'] = 'Нет'

    await callback.message.answer("Вопрос № 46\n"
                                  "Доброкачественные заболевания половых органов. "
                                  "Укажите, наблюдались ли у Вас такие заболевания, "
                                  "как гиперплазия эндометрия, опухоль яичников в анамнезе, "
                                  "эндометриоз, миома матки, эрозия шейки матки, лейкоплакия, "
                                  "гипертрофическое удлинение и элонгация шейки матки, "
                                  "декубитальная язва?",
                                  reply_markup=btn_da_net_q_46())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_46)
async def ques_46(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_46':
        async with state.proxy() as data:
            data['Q_46'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_46'] = 'Нет'

    await callback.message.answer("Вопрос № 47\n"
                                  "Оперативные вмешательства по поводу гинекологических заболеваний. "
                                  "Укажите, были ли у вас операции на придатках, матке, шейке матки?",
                                  reply_markup=btn_da_net_q_47())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_47)
async def ques_47(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_47':
        async with state.proxy() as data:
            data['Q_47'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_47'] = 'Нет'

    await callback.message.answer("Вопрос № 48\n"
                                  "Травмы органов малого таза. "
                                  "Укажите, были ли у вас травмы наружных половых органов, "
                                  "прямой кишки, мочевого пузыря?",
                                  reply_markup=btn_da_net_q_48())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_48)
async def ques_48(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_48':
        async with state.proxy() as data:
            data['Q_48'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_48'] = 'Нет'

    await callback.message.answer("Вопрос № 49\n"
                                  "Операции на наружных половых и тазовых органов. "
                                  "Укажите, были ли у вас операции по поводу бартолинита, "
                                  "геморроя, недержания мочи или газов?",
                                  reply_markup=btn_da_net_q_49())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_49)
async def ques_49(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_49':
        async with state.proxy() as data:
            data['Q_49'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_49'] = 'Нет'

    await callback.message.answer("Вопрос № 50\n"
                                  "Заболевания эндокринной системы. "
                                  "Укажите, имеются ли у Вас гипофункция щитовидной железы, "
                                  "сахарный диабет, ожирение:",
                                  reply_markup=btn_da_net_q_50())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_50)
async def ques_50(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_50':
        async with state.proxy() as data:
            data['Q_50'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_50'] = 'Нет'

    await callback.message.answer("Вопрос № 51\n"
                                  "Заболевания органов дыхания. "
                                  "Укажите, имеются ли у Вас бронхит, пневмония, "
                                  "бронхиальная астма, бронхоэктатическая болезнь?",
                                  reply_markup=btn_da_net_q_51())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_51)
async def ques_51(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_51':
        async with state.proxy() as data:
            data['Q_51'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_51'] = 'Нет'

    await callback.message.answer("Вопрос № 52\n"
                                  "Заболевания мочевыделительной системы. "
                                  "Укажите, имеются ли у Вас Заболевания мочевыделительной системы"
                                  " пиелонефрит, цистит, мочекаменная болезнь, недержание мочи?",
                                  reply_markup=btn_da_net_q_52())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_52)
async def ques_52(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_52':
        async with state.proxy() as data:
            data['Q_52'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_52'] = 'Нет'

    await callback.message.answer("Вопрос № 53\n"
                                  "Заболевания сердечно сосудистой системы. "
                                  "Укажите, имеются ли у Вас гипертоническая болезнь, атеросклероз сосудов, "
                                  "врожденный порок сердца, ишемическая болезнь сердца, инфаркт миокарда?",
                                  reply_markup=btn_da_net_q_53())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_53)
async def ques_53(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_53':
        async with state.proxy() as data:
            data['Q_53'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_53'] = 'Нет'

    await callback.message.answer("Вопрос № 54\n"
                                  "Заболевания желудочно- кишечного тракта. "
                                  "Укажите, имеются ли у Вас гастрит, желчнокаменная болезнь, "
                                  "запоры, анальная трещина, геморрой?",
                                  reply_markup=btn_da_net_q_54())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_54)
async def ques_54(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_54':
        async with state.proxy() as data:
            data['Q_54'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_54'] = 'Нет'

    await callback.message.answer("Вопрос № 55\n"
                                  "Заболевания органов зрения. "
                                  "Укажите, имеются ли у Вас катаракта, глаукома, "
                                  "дальнозоркость, астигматизм, близорукость?",
                                  reply_markup=btn_da_net_q_55())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_55)
async def ques_55(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_55':
        async with state.proxy() as data:
            data['Q_55'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_55'] = 'Нет'

    await callback.message.answer("Вопрос № 56\n"
                                  "Заболевания нервной системы. "
                                  "Укажите, имеются ли у Вас опухоль головного мозга, "
                                  "эпилепсия, остеохондроз, межпозвоночные грыжи, инсульт?",
                                  reply_markup=btn_da_net_q_56())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_56)
async def ques_56(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_56':
        async with state.proxy() as data:
            data['Q_56'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_56'] = 'Нет'

    await callback.message.answer("Вопрос № 57\n"
                                  "Заболевания системы крови. "
                                  "Укажите, страдаете ли Вы хронической анемией?",
                                  reply_markup=btn_da_net_q_57())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_57)
async def ques_57(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_57':
        async with state.proxy() as data:
            data['Q_57'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_57'] = 'Нет'

    await callback.message.answer("Вопрос № 58\n"
                                  "Костно-мышечные заболевания. "
                                  "Укажите, имеются ли у Вас артрит, артроз, коксартроз, "
                                  "вальгусная деформация первого пальца стопы, "
                                  "эндопротезирование тазобедренного сустава, сколиоз, кифоз, кифосколио?",
                                  reply_markup=btn_da_net_q_58())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_58)
async def ques_58(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_58':
        async with state.proxy() as data:
            data['Q_58'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_58'] = 'Нет'

    await callback.message.answer("Вопрос № 59\n"
                                  "Патология зубочелюстной системы. "
                                  "Укажите, имеются ли у Вас кариес, нарушения прикуса, "
                                  "частичное или полное отсутствие зубов?",
                                  reply_markup=btns_adentiya_q_59())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_59)
async def ques_59(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_59':
        async with state.proxy() as data:
            data['Q_59'] = 'Да'
    elif callback.data == 'Нет_q_59':
        async with state.proxy() as data:
            data['Q_59'] = 'Нет'
    else:
        async with state.proxy() as data:
            data['Q_59'] = 'Адентия'

    await callback.message.answer("Вопрос № 60\n"
                                  "Перенесенные полостные операции. "
                                  "Укажите, перенесли ли Вы аппендэктомию, "
                                  "холецистэктомию; имеется ли у Вас спаечная болезнь, "
                                  "грыжа передней брюшной стенки?",
                                  reply_markup=btn_da_net_q_60())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_60)
async def ques_60(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_60':
        async with state.proxy() as data:
            data['Q_60'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_60'] = 'Нет'

    await callback.message.answer("Вопрос № 61\n"
                                  "Другие не полостные операции. "
                                  "Укажите, перенесли ли Вы операции по удалению "
                                  "геморроя, варикоза вен, тонзиллэктомию?",
                                  reply_markup=btn_nepolostny_operacii_q_61())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_61)
async def ques_61(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_61':
        async with state.proxy() as data:
            data['Q_61'] = 'Да_q_61'
    else:
        async with state.proxy() as data:
            data['Q_61'] = 'Нет_q_61'

    await callback.message.answer("Вопрос № 62\n"
                                  "Расстройства мочеиспускания. "
                                  "Укажите, имеются ли у Вас чувство неполного опорожнения мочевого пузыря, "
                                  "непроизвольное/затрудненное/учащенное выделение мочи, "
                                  "недержание мочи при напряжении, слабая прерывистая или "
                                  "разбрызгивающаяся струя мочи при мочеиспускании, "
                                  "необходимость вправления выпячивания для завершения мочеиспускания?",
                                  reply_markup=btn_da_net_q_62())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_62)
async def ques_62(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_62':
        async with state.proxy() as data:
            data['Q_62'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_62'] = 'Нет'

    await callback.message.answer("Вопрос № 63\n"
                                  "Нарушения дефекации. "
                                  "Укажите, наблюдаются ли у Вас чувство неполного опорожнения, "
                                  "длительная/затрудненная дефекация, многокомпонентное затрудненное опорожнение, "
                                  "отсутствие самостоятельного стула "
                                  "(с необходимостью применения ручного пособия для облегчения дефекации), "
                                  "эпизоды временного/постоянного недержания кала, газов, запоры?",
                                  reply_markup=btn_da_net_q_63())
    await AnketaSG.next()


@dp.callback_query_handler(state=AnketaSG.Q_63)
async def ques_63(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == 'Да_q_63':
        async with state.proxy() as data:
            data['Q_62'] = 'Да'
    else:
        async with state.proxy() as data:
            data['Q_62'] = 'Нет'

    await callback.message.answer("Вопрос № 64\n"
                                  "Нарушения половой функции. "
                                  "Укажите, наблюдаются ли у Вас хлюпающие звуки и "
                                  "попадание воздуха при половом акте, невозможность полового акта, "
                                  "связанная с болью при введении полового члена "
                                  "связанное с сужением влагалища, жалобы на дискомфорт при половом акте, "
                                  "ощущение инородного тела во влагалище, боли при половом акте "
                                  "связанные с сухостью и зудом. Оцените от 1 (минимум) до 10 баллов (максимум)"
                                  "(чем выше балл, тем сильнее проявления)?")
    await AnketaSG.next()


@dp.message_handler(lambda message: not message.text.
                    isdigit() or float(message.text) >= 10 or float(message.text) <= 1, state=AnketaSG.Q_64)
async def check_age(message: types.Message):
    await message.reply('Введите корректные баллы!')


@dp.message_handler(state=AnketaSG.Q_64)
async def ques_64(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['Q_64'] = message.text

    await message.reply("Вопрос № 65\n"
                        "Продолжительность расстройств функции тазовых органов. "
                        "Если у Вас наблюдается расстройство тазовых органов, "
                        "укажите, сколько лет это длится?")
    await AnketaSG.next()


@dp.message_handler(lambda message: not message.text.
                    isdigit() or float(message.text) > 50 or float(message.text) <= 0,
                    state=AnketaSG.Q_65)
async def check_age(message: types.Message):
    await message.reply('Введите корректные данные!')


@dp.message_handler(state=AnketaSG.Q_65)
async def ques_65(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['Q_65'] = message.text

    print(data)
    await sqlite_db.sql_add_command(state)
    await message.answer(f"Вы прошли опрос! Нажмите /Подсчитать",
                         reply_markup=btn_podschet())
    await state.finish()


@dp.message_handler(commands='Подсчитать')
async def delete_item(message: types.Message):
    risk = calculation.find_bal_risk()[0]
    bal = calculation.find_bal_risk()[1]
    await message.reply(f"Количество баллов {bal}.\n"
                        f"Степень риска пролапса тазовых органов {risk}",
                        reply_markup=btn_proyti())


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)
