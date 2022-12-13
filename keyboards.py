from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types


def btn_proyti() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(KeyboardButton('/пройти_тест'))
    return kb


def btn_cancel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/завершить'))
    return kb


def btns_q_4_rodstvenniki():
    buttons = [
        types.InlineKeyboardButton(text="Нет пролапса", callback_data="Нет пролапса_q_4"),
        types.InlineKeyboardButton(text="У матери", callback_data="У матери_q_4"),
        types.InlineKeyboardButton(text="У родственников", callback_data="У родственников_q_4")
    ]
    # row_width=2, в первом ряду две кнопки, а третья на следующей строке
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_5():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_5"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_5")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_6():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_6"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_6")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_7():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_7"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_7")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_8():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_8"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_8")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_9():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_9"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_9")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_10():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_10"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_10")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_11():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_11"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_11")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_12():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_12"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_12")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_13():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_13"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_13")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_14():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_14"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_14")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_15():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_15"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_15")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_16():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_16"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_16")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_17():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_17"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_17")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_18():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_18"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_18")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_19():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_19"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_19")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_20():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_20"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_20")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_21():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_21"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_21")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_22():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_22"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_22")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_23():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_23"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_23")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_24():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_24"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_24")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_25():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_25"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_25")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_26():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_26"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_26")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_27():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_27"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_27")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_28():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_28"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_28")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_29():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_29"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_29")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_30():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_30"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_30")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_31():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_31"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_31")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btns_q_32_kolichestvo_rodov():
    buttons = [
        types.InlineKeyboardButton(text="Не рожала", callback_data="Не рожала_q_32"),
        types.InlineKeyboardButton(text="1", callback_data="1_q_32"),
        types.InlineKeyboardButton(text="2", callback_data="2_q_32"),
        types.InlineKeyboardButton(text="3 и более", callback_data="3 и более_q_32")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btns_q_36_alcogol():
    buttons = [
        types.InlineKeyboardButton(text="Не потребляю", callback_data="Не потребляю_q_36"),
        types.InlineKeyboardButton(text="Потребляла ранее", callback_data="Потребляла ранее_q_36"),
        types.InlineKeyboardButton(text="Употребляю", callback_data="Употребляю_q_36")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btns_q_37_tabak():
    buttons = [
        types.InlineKeyboardButton(text="Не курю", callback_data="Нет, не курю_q_37"),
        types.InlineKeyboardButton(text="Ранее курила, потом бросила", callback_data="Бросила_q_37"),
        types.InlineKeyboardButton(text="Курю", callback_data="Курю_q_37")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btns_q_38_obraz_zhizni():
    buttons = [
        types.InlineKeyboardButton(text="Нормальный", callback_data="Нормальный_q_38"),
        types.InlineKeyboardButton(text="Малоподвижный", callback_data="Малоподвижный_q_38"),
        types.InlineKeyboardButton(text="Тяжелый труд", callback_data="Тяжелый труд_q_38")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btns_q_40_travmy_promezhnosti():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_40"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_40"),
        types.InlineKeyboardButton(text="Разрыв промежности IV степени",
                                   callback_data="Разрыв промежности IV степени")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btns_q_41_akusherskie_operacii():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_41"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_41"),
        types.InlineKeyboardButton(text="Наложение щипцов", callback_data="Наложение щипцов_q_41")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_42():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_42"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_42")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_43():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_43"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_43")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_44():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_44"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_44")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_45():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_45"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_45")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_46():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_46"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_46")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_47():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_47"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_47")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_48():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_48"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_48")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_49():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_49"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_49")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_50():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_50"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_50")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_51():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_51"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_51")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_52():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_52"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_52")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_53():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_53"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_53")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_54():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_54"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_54")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_55():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_55"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_55")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_56():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_56"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_56")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_57():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_57"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_57")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_58():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_58"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_58")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btns_adentiya_q_59():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_59"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_59"),
        types.InlineKeyboardButton(text="Адентия", callback_data="Адентия_q_59")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_60():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_60"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_60")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_nepolostny_operacii_q_61():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_61"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_61")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_62():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_62"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_62")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_da_net_q_63():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="Да_q_63"),
        types.InlineKeyboardButton(text="Нет", callback_data="Нет_q_63")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def btn_podschet():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/Подсчитать'))
    return kb
