def get_num():
    number = input("Enter a number ")
    return int(number)


def get_digit_sum():
    number = get_num()
    # number = 2937645
    digit_sum = 0
    while number > 0:
        modulo_res = number % 10
        digit_sum += modulo_res
        number -= modulo_res
        number /= 10
    print(f"Digit summary - {int(digit_sum)}")
    return int(digit_sum)


get_digit_sum()
