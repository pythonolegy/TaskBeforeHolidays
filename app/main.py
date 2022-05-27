from fast_bitrix24 import Bitrix

from isdayoff import ProdCalendar, DayType
from datetime import datetime, timedelta, date
from time import sleep

###------------------------------------  ---  ---START HERE---  ---  ------------------------------------------------###
webhook = 'https://b24-xlxcp4.bitrix24.ru/rest/1/uqf2lp8dgfk85u15/'  # персональный вебхук Bitrix24
b = Bitrix(webhook)  # переменная-сокращение для вызова методов 'b.call()'
START_WORK_DAY = 6

calendar = ProdCalendar()  # переменная для вызова методов бибиотеки 'isdayoff'

day = date.today() + timedelta(days=3)  # переменная хранит дату по параметрам


def main():
    """ Функция создает задачу с со значениями из полей 'fields' """
    b.call('tasks.task.add',
           {
               'fields': {
                   'TITLE': 'title',
                   'DESCRIPTION': 'description',
                   'RESPONSIBLE_ID': 1
               }
           }
           )


def check_day_is_off():
    """ Функция проверяет будет ли через заданный в переменной 'day' день, если при этом он является будним"""
    if day.weekday() not in [5, 6] and calendar.check(day) == DayType.NOT_WORKING:
        return main()
    else:
        print('Через три дня нет праздничного выходного')


if __name__ == '__main__':
    """ 
        Функция активируется при запуске файла 'main.py'
            * Функция проверяет время дня, время равняется установленному 'now.hour'
            * Обращается к функции 'check_day_is_off()' 
    """
    while True:
        now = datetime.now()
        print('Проверка. Время >>> ', now.hour)
        if now.hour == START_WORK_DAY:
            check_day_is_off()
        sleep(3600)
