import statistics

"""
python work
crated by:daniel tomanian
03.07.2022
"""


def print_all_dicts(data: dict, userNum=0):
    """
    func:
    print from dictionary all
    Prints all the values from dictionary whose age is above the number entered,
    if the user did not enter a number prints all the values
    """
    if userNum < 0:  # if parameter num is empty
        for key, value in data.items():
            print(key, value)
    else:
        for key, value in data.items():
            for k, age in value.items():
                if k.lower() == "age":
                    if age > userNum:
                        print(key, value)


def median_average(data):
    """
    func:
    Calculate Average age and Median age
    returns Average & median dictionary with keys Average&median
    import statistics for  median
    """
    avg = 0
    list = []
    for key, value in data.items():
        for k, v in value.items():
            if k.lower() == "age":
                avg = avg + v
                list.append(v)
    list.sort()
    avg = avg / len(data)
    median = statistics.median(list)  # after sorted find the median
    print("median : averge>>")

    return avg, median


def female_male_func(data):
    """
    func:
    split dictionary by  Male or Female.
    return male and female dictionaries
    """
    maleDict = {}
    femaleDict = {}
    for key, value in data.items():
        for k, v in value.items():
            if k == "sex":
                if v.lower().startswith("f"):
                    femaleDict[key] = value
            if k == "sex":
                if v.lower().startswith("m"):
                    maleDict[key] = value

    res = {"Female": femaleDict, "Male": maleDict}
    return res


def main():
    data_set = {134232342: {"name": "Tal", "sex": "female", "age": 11},
                121344321: {"name": "Habibi", "sex": "male", "age": 52},
                318266830: {"name": "Daniel", "sex": "female", "age": 96},
                557474227: {"name": "Alex", "sex": "male", "age": 67, "car": "b.m.w", "hieght": 190}, }
    # 1
    print("--------------------------------------")
    print("func 1 :")
    dictM_F = female_male_func(data_set)
    print(dictM_F)

    print("--------------------------------------")
    # 2 find med average()
    print("\nFunc 2 ")
    dict_median_avg = median_average(data_set)
    print(dict_median_avg)
    print("--------------------------------------")

    # 3  check print values
    print("\nFunc3 to print all dicts")
    print_all_dicts(data_set)
    print("--------------------------------------")
    # 4  check print values bigger the age=num=user input the Num
    print("\nFunc4 to print all dicts are age bigger then num")
    print_all_dicts(data_set, 23)
    print("--------------------------------------")


main()
