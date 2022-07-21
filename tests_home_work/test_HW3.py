import logging
import statistics

from dict_tupels import female_male_func, median_average, print_all_dicts

data_set = {1: {"name": "Tal", "sex": "male", "age": 22},
            2: {"height": 1.77, "sex": "male", "age": 65, "name": "Oren"},
            3: {"height": 0.77, "sex": "female", "age": 2, "name": "Igor"},
            4: {"height": 2.77, "sex": "female", "age": 3, "name": "tali"}}


def test_split_male_female():
    data_set_m = female_male_func(data_set)["Male"]
    data_set_f = female_male_func(data_set)["Female"]
    if len(data_set_m) + len(data_set_f) != len(data_set):
        assert logging.info("this is info")


def test_median_avg():
    if median_average(data_set) != None:
        assert median_average(data_set)
    else:
        assert logging.warning('failed!!')

def test_print():
    try:
        print_all_dicts(data_set, 23)
    except:
        assert logging.warning("warning")


def test_median_avg():
    avg = 92 / 4
    median = statistics.median([13, 12, 65,12])
    a, m = median_average(data_set)
    print(a, avg, m, median)
    if a == avg and m == median:
        assert median_average(data_set)
    else:
       assert logging.error('Error in calculating avg and median ')
