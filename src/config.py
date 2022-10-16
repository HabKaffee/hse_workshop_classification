# PATH
RAW_PATH = 'data/raw/'


# COLS
TARGET_COLS = ['Артериальная гипертензия', 'ОНМК', 'Стенокардия, ИБС, инфаркт миокарда', 'Сердечная недостаточность', 'Прочие заболевания сердца']
ID_COL = 'ID'
EDU_COL = 'Образование'
SEX_COL = 'Пол'
CAT_COLS = [
    'Семья', 'Этнос', 'Национальность', 'Религия', 'Образование', 
    'Профессия', 'Статус Курения', 'Частота пасс кур', 'Алкоголь',
    'Время засыпания', 'Время пробуждения'
]
OHE_COLS = [
    'Пол','Вы работаете?', 'Выход на пенсию', 'Прекращение работы по болезни', 'Сахарный диабет', 'Гепатит',
    'Онкология', 'Хроническое заболевание легких', 'Бронжиальная астма', 'Туберкулез легких ', 'ВИЧ/СПИД',
    'Регулярный прим лекарственных средств', 'Травмы за год', 'Переломы','Пассивное курение', 'Сон после обеда', 
    'Спорт, клубы', 'Религия, клубы', 'Жаворонок'
]
REAL_COLS = ['Возраст курения', 'Сигарет в день', 'Возраст алког']