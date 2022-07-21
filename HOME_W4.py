class Date:

    def __init__(self, day: int, month: int, year: int):
        """
        constructor init day/month/year (integer type) put in objact
        """
        self.day = day
        self.month = month
        self.year = year
        if self.is_valid() is not True:
            print("invalid date")
            self.day = 0
            self.month = 0
            self.year = 0

    def __str__(self):
        """
        This Date ToString func
        :return: date in string type
        """
        res = f"date:{self.day}.{self.month}. {self.year} "
        return res

    def __lt__(self, other):
        """
            Check if this date before input date
            :param other: input date
            :return: True/False
            """
        if self.day < other.day and self.month <= other.month and self.year <= other.year:
            return True
        if self.month < other.month and self.year <= other.year:
            return True
        if self.year < other.year:
            return True
        else:
            return False

    def __le__(self, other):
        """
        Check if this date equal or before to input date
        :param other: Date
        :return: True/False
        """
        return self == other or self < other

    def __ge__(self, other):
        """
        Check if this date equal or after to input date
        :param other: Date
        :return: True/False
        """
        return self == other or self > other

    def __gt__(self, obj):
        """
         Check if this date after input date
            :param other: input date
            :return: True/False
            """
        if self.day > obj.day and self.month >= obj.month and self.year >= obj.year:
            return True
        if self.month > obj.month and self.year >= obj.year:
            return True
        if self.year > obj.year:
            return True
        else:
            return False

    def __eq__(self, obj):
        """
                Check if this date equal to other date
                :param other: Date
                :return: True/False
                """
        if self.day == obj.day and self.month == obj.month and self.year == obj.year:
            return True
        else:
            return False

    def __sub__(self, other):
        """
                Return date difference between two dates
                if this date before return a negative number
                :param other:input date, days count difference
                :return: days
                """
        days = 0
        if self.is_valid() == True and other.is_valid() == True:
            monthDays = [31, 28, 31, 30, 31, 30,
                         31, 31, 30, 31, 30, 31]  # monthDays - monthDays[4] =30 : april hes 30 dmonthDaysays in month
            if self.day - other.day > 0:
                days = days + self.day - other.day
            if self.day - other.day < 0:
                days = days + (self.day - other.day) * -1
            if self.month - other.month > 0:
                months = self.month - other.month
                days = days + months * monthDays[other.month]
            if self.month - other.month < 0:
                months = self.month - other.month
                days = days + (months * monthDays[other.month]) * -1
            if self.year - other.year > 0:
                days = days + (self.year - other.year) * 365
            if self.year - other.year < 0:
                days = days + ((self.year - other.year) * 365) * -1
        return "days:", days

    def is_valid(self):
        """
        check valid of date
        return true /false
        """

        if self.day > 0 and self.month > 0:
            if self.day <= 31 and self.month <= 12:
                if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:
                    if self.year > 0 and self.year < 2023:
                        return True

            if self.day <= 30:
                if self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
                    if self.year > 0 and self.year < 2023:
                        if self.year == 2022 and self.month < 8 and self.day < 12:
                            return True
                    return True
            if self.day <= 28:
                if self.month == 2:
                    return True

            if self.day == 29:
                if self.month == 2:
                    if self.year % 4 == 0 or self.year % 400 == 0:
                        return True

            if self.year >= 2022 and self.month > 7 and self.day > 12:
                return False
            else:
                return False

    def get_next_days(self, others=1):
        """
              Add 1 days to this date
              or user cohise(input others)
              :param others: int
              :return: date + others
              """
        import pandas as pd
        initial_date = str(self.month) + "/" +str(self.day) + "/" + str(self.year)
        final_date = pd.DateOffset(days=others)+pd.to_datetime(initial_date)

        return final_date
    def get_next_day(self):
        """
              Add 1 days to this date
              or user cohise(input others)
              :param others: int
              :return: date + others
              """
        import pandas as pd
        initial_date = str(self.month) + "/" +str(self.day) + "/" + str(self.year)
        final_date = pd.DateOffset(days=1)+pd.to_datetime(initial_date)

        return final_date



##main for check the funcs
def main():
    date1 = Date(28, 2, 2020)
    date2 = Date(14, 5, 2020)
    print("add 1 day: ", date1.get_next_days())
    print("add user days : ", date2.get_next_days(11))
    print("str :", date2)
    print("< __lt__ :", date2 < date1)
    print("<= __le__ :", date2 <= date1)
    print("> __gt__ :", date2 > date1)
    print(">= __ge__ :", date2 >= date1)
    print("== __eq__ :", date2 == date1)
    print("sub :", date1.__sub__(date2))
if __name__ == '__main__':
    main()
