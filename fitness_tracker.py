import datetime
from typing import Tuple


class FitnessTracker:
    FULL_FORMAT = '%Y-%m-%d %H:%M:%S'
    FORMAT_WITHOUT_HOURS = '%Y-%m-%d'
    CALORIES_PER_KM = 200
    STEP_LENGTH = 0.65

    def __init__(self) -> None:
        self.storage_dict = {}

    def add_package(self, data: Tuple[str, int, int]) -> None:
        """ Добавление полученого пакетта """
        time, steps, pulse = data
        full_time = datetime.datetime.strptime(time, self.FULL_FORMAT)
        only_date = full_time.strftime(self.FORMAT_WITHOUT_HOURS)
        if full_time.time():
            if only_date in self.storage_dict.keys():
                self.storage_dict[only_date].append({'time': str(full_time.time()), 'steps': steps, 'pulse': pulse})
            else:
                self.storage_dict[only_date] = [{'time': str(full_time.time()), 'steps': steps, 'pulse': pulse}]

    def get_param_distance_for_last_day(self) -> None:
        """ Получить параметры пройденного пути """
        day = max(self.storage_dict)
        day_steps = sum([value['steps'] for value in self.storage_dict[day]])
        dist_km = (day_steps * self.STEP_LENGTH) / 1000
        spent_calories = dist_km * self.CALORIES_PER_KM
        print(f'''
            День: {day}
            За сегодня вы прошли {day_steps} шагов.
            Дистанция составила {dist_km} км.
            Вы сожгли {spent_calories} кал.
            ''')

    def get_steps_for_all_days(self) -> None:
        """ Получить шаги за все дни """
        steps_and_dist = ''
        for key in self.storage_dict.keys():
            day_steps = sum([value['steps'] for value in self.storage_dict[key]])
            dist_km = (day_steps * self.STEP_LENGTH) / 1000
            steps_and_dist += f'\t\t\t{key}: {day_steps} шагов, {dist_km} км. \n'
        print(steps_and_dist)


mylist = ('2012-11-14 14:32:30', 5000, 85)
mylist2 = ('2012-11-15 14:32:30', 7000, 110)
mylist3 = ('2012-11-16 14:32:30', 6000, 90)
mylist4 = ('2012-11-16 14:32:30', 3000, 80)
a = FitnessTracker()
a.add_package(mylist)
a.add_package(mylist2)
a.add_package(mylist3)
a.add_package(mylist4)
a.get_param_distance_for_last_day()
a.get_steps_for_all_days()
