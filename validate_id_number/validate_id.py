def day_month_year(number):
    day = number[4:6]
    if int(day) > 31:
        return False
    month = number[2:4]
    if int(month) > 12:
        return False
    if "02" in month and int(day) > 29:
        return False
    thirty_day_months = ["04", "06", "09", "11"]
    for i in thirty_day_months:
        if i == month and int(day) > 30:
            return False
    year = number[0:2]
    if int(year) < 0:
        return False
    else:
        return True


def citizenship(number):
    citizen = number[10:11]
    if int(citizen) > 1 or int(citizen) < 0:
        return False
    else:
        return True


def last_number_checksum(number):
    if number.isdigit():
        sum_of_multiplied_number = 0
        list_alternating_numbers = [int(number[i]) for i in range(0, len(number), 2)]
        list_multiplied_numbers = "".join(
            [str(int(number[j]) * 2) for j in range(1, len(number) - 1, 2)]
        )
        for n in list(list_multiplied_numbers):
            sum_of_multiplied_number += int(n)
        checksum = sum(list_alternating_numbers) + sum_of_multiplied_number
        if checksum % 10 != 0:
            return False
        else:
            return True


def length_and_characters(number):
    if number.isdigit() == False:
        return False
    if len(number) < 13:
        return False
    if len(number) > 13:
        return False
    else:
        return True


def validate_sa_id_number(number):
    if (
        length_and_characters(number) == True
        and last_number_checksum(number) == True
        and citizenship(number) == True
        and day_month_year(number) == True
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    print(validate_sa_id_number("2001014800086"))
