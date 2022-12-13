import sqlite3 as sq


def sql_start():  # создание таблицы menu
    global base, cur

    base = sq.connect('anketa_pto.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')  # user_id INTEGER PRIMARY KEY, full_name TEXT
    base.execute("CREATE TABLE IF NOT EXISTS menu (user_id INTEGER PRIMARY KEY, full_name TEXT, Q_1 TEXT, Q_2 TEXT, "
                 "Q_3 TEXT, Q_4 TEXT, Q_5 TEXT, Q_6 TEXT, Q_7 TEXT, Q_8 TEXT, Q_9 TEXT, Q_10 TEXT, Q_11 TEXT, "
                 "Q_12 TEXT, Q_13 TEXT, Q_14 TEXT, Q_15 TEXT, Q_16 TEXT, Q_17 TEXT, Q_18 TEXT, Q_19 TEXT, Q_20 TEXT, "
                 "Q_21 TEXT, Q_22 TEXT, Q_23 TEXT, Q_24 TEXT, Q_25 TEXT, Q_26 TEXT, Q_27 TEXT, Q_28 TEXT, Q_29 TEXT, "
                 "Q_30 TEXT, Q_31 TEXT, Q_32 TEXT, Q_33 TEXT, Q_34 TEXT, Q_35 TEXT, Q_36 TEXT, Q_37 TEXT, Q_38 TEXT, "
                 "Q_39 TEXT, Q_40 TEXT, Q_41 TEXT, Q_42 TEXT, Q_43 TEXT, Q_44 TEXT, Q_45 TEXT, Q_46 TEXT, Q_47 TEXT, "
                 "Q_48 TEXT, Q_49 TEXT, Q_50 TEXT, Q_51 TEXT, Q_52 TEXT, Q_53 TEXT, Q_54 TEXT, Q_55 TEXT, Q_56 TEXT, "
                 "Q_57 TEXT, Q_58 TEXT, Q_59 TEXT, Q_60 TEXT, Q_61 TEXT, Q_62 TEXT, Q_63 TEXT, Q_64 TEXT, Q_65 TEXT)")
    base.commit()


async def sql_add_command(state):  # внесение данных опроса
    # base = sq.connect('anketa_pto.db')
    # cur = base.cursor()
    async with state.proxy() as data:
        cur.execute("INSERT OR IGNORE INTO menu (full_name, Q_1, Q_2, Q_3, Q_4, Q_5, Q_6, Q_7, Q_8, Q_9, Q_10,"
                    " Q_11, Q_12, Q_13, Q_14, Q_15, Q_16, Q_17, Q_18, Q_19, Q_20, Q_21, Q_22, Q_23, Q_24, Q_25, Q_26, "
                    "Q_27, Q_28, Q_29, Q_30, Q_31, Q_32, Q_33, Q_34, Q_35, Q_36, Q_37, Q_38, Q_39, Q_40, Q_41, Q_42, "
                    "Q_43, Q_44, Q_45, Q_46, Q_47, Q_48, Q_49, Q_50, Q_51, Q_52, Q_53, Q_54, Q_55, Q_56, Q_57, Q_58, "
                    "Q_59, Q_60, Q_61, Q_62, Q_63, Q_64, Q_65) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                    "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                    "?, ?, ?, ?, ?)", tuple(data.values()))
    base.commit()
