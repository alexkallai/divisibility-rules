"""
With really big numbers checking for divisibility can be inefficient
with modulo.
So this package does the check using the divisibility rules:
https://en.wikipedia.org/wiki/Divisibility_rule
Current plan is to support divisors between 0 and 30
Other numbers are checked with modulo normally

Another planned function is to use recursion to determine divisibility
where it's required e.g. divide by 3 result can be checked recursively if needed
"""


def divisible(number_to_divide: int, divisor: int) -> bool:
    """
    This is the main function, the other functions are just helpers
    """

    # not possible to divide by 0
    def divisible_by_0() -> bool:
        raise ZeroDivisionError

    # all ints can be divided by 1
    def divisible_by_1():
        return True

    # if the number ends with 0, 2, 4, 6, 8
    def divisible_by_2():
        return str(number_to_divide)[-1] in ("0", "2", "4", "6", "8")

    # is the sum of the digit is divisible
    def divisible_by_3():
        return sum([int(digit) for digit in str(number_to_divide)]) % 3 == 0

    # If the tens digit is even, the ones digit must be 0, 4, or 8.
    # If the tens digit is odd, the ones digit must be 2 or 6. 
    def divisible_by_4():
        number_to_divide_str = str(number_to_divide)
        ones_digit = number_to_divide_str[-1]
        tens_digit = number_to_divide_str[-2]
        # if tens digit even
        if tens_digit in ("0", "2", "4", "6", "8"):
            if ones_digit in ("0", "4", "8"):
                return True
            else:
                return False
        if tens_digit in ("1", "3", "5", "7", "9"):
            if ones_digit in ("2", "6"):
                return True
            else:
                return False

    # if the number ends with 0 or 5
    def divisible_by_5():
        return str(number_to_divide)[-1] in ("0","5")

    def divisible_by_6():
        return divisible_by_3() and divisible_by_2()

    def divisible_by_7():
        raise NotImplementedError

    def divisible_by_8():
        raise NotImplementedError

    def divisible_by_9():
        raise NotImplementedError

    def divisible_by_10():
        raise NotImplementedError

    def divisible_by_11():
        raise NotImplementedError

    def divisible_by_12():
        raise NotImplementedError

    def divisible_by_13():
        raise NotImplementedError

    def divisible_by_14():
        raise NotImplementedError

    def divisible_by_15():
        raise NotImplementedError

    def divisible_by_16():
        raise NotImplementedError

    def divisible_by_17():
        raise NotImplementedError

    def divisible_by_18():
        raise NotImplementedError

    def divisible_by_19():
        raise NotImplementedError

    def divisible_by_20():
        raise NotImplementedError

    def divisible_by_21():
        raise NotImplementedError

    def divisible_by_22():
        raise NotImplementedError

    def divisible_by_23():
        raise NotImplementedError

    def divisible_by_24():
        raise NotImplementedError

    def divisible_by_25():
        raise NotImplementedError

    def divisible_by_26():
        raise NotImplementedError

    def divisible_by_27():
        raise NotImplementedError

    def divisible_by_28():
        raise NotImplementedError

    def divisible_by_29():
        raise NotImplementedError

    def divisible_by_30():
        raise NotImplementedError

    dict_of_args = {
        0:   divisible_by_0,
        1:   divisible_by_1,
        2:   divisible_by_2,
        3:   divisible_by_3,
        4:   divisible_by_4,
        5:   divisible_by_5,
        6:   divisible_by_6,
        7:   divisible_by_7,
        8:   divisible_by_8,
        9:   divisible_by_9,
        10:  divisible_by_10,
        11:  divisible_by_11,
        12:  divisible_by_12,
        13:  divisible_by_13,
        14:  divisible_by_14,
        15:  divisible_by_15,
        16:  divisible_by_16,
        17:  divisible_by_17,
        18:  divisible_by_18,
        19:  divisible_by_19,
        20:  divisible_by_20,
        21:  divisible_by_21,
        22:  divisible_by_22,
        23:  divisible_by_23,
        24:  divisible_by_24,
        25:  divisible_by_25,
        26:  divisible_by_26,
        27:  divisible_by_27,
        28:  divisible_by_28,
        29:  divisible_by_29,
        30:  divisible_by_30
        }

    # If divisibility rule implemented:
    if divisor in dict_of_args.keys():
        # the functions are stored in a dict
        return dict_of_args[divisor]()
    else:
        # if it's not implemented, use the normal method
        return number_to_divide % divisor == 0

if __name__ == "__main__":
    #print(divisible(99999999999999999999993, 5))
    import datetime
    import time

    BIG_NUMBER = 11111111111111111111111111111111111111111111111111111111111111111111111111111111111
    begin = datetime.datetime.now().timestamp()
    # measurement start
    print(BIG_NUMBER % 1 == 0)
    # measurement end
    end = datetime.datetime.now().timestamp()
    diff = end - begin
    print(f"{diff} seconds")

    begin = datetime.datetime.now().timestamp()
    # measurement start
    print(divisible(BIG_NUMBER, 1))
    # measurement end
    end = datetime.datetime.now().timestamp()
    diff = end - begin
    print(f"{diff} seconds")