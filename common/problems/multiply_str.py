"""
Даны два неотрицательных целых числа num1 и num2, представленные в виде
строк, вернуть произведение num1 и num2, также представленное в виде строки.

Примечание. Вы не должны использовать какую-либо встроенную библиотеку
BigInteger или напрямую преобразовывать входные данные в целое число.
"""


def char_to_digit(char):
    mapping = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    return mapping[char]


def digit_to_char(n: int) -> str:
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return digits[n]


def sum_strings(num1: str, num2: str) -> str:
    max_len = max(len(num1), len(num2))
    num_1 = num1.zfill(max_len)
    num_2 = num2.zfill(max_len)

    carry = 0
    result = []

    for i in range(max_len - 1, -1, -1):
        d1 = char_to_digit(num_1[i])
        d2 = char_to_digit(num_2[i])
        total = d1 + d2 + carry
        result.append(digit_to_char(total % 10))
        carry = total // 10

    if carry:
        result.append(digit_to_char(carry))

    return "".join(reversed(result))


def multiply_strings(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    result = "0"
    num1_len = len(num1)
    num2_len = len(num2)

    for i in range(num2_len - 1, -1, -1):
        d2 = char_to_digit(num2[i])
        temp = []
        carry = 0

        for j in range(num1_len - 1, -1, -1):
            d1 = char_to_digit(num1[j])
            prod = d1 * d2 + carry
            temp.append(digit_to_char(prod % 10))
            carry = prod // 10

        if carry:
            temp.append(digit_to_char(carry))

        temp = "".join(reversed(temp))
        temp += "0" * (num2_len - 1 - i)
        result = sum_strings(result, temp)

    return result.lstrip("0")


nums = [9999, 99999]
print(multiply_strings(f"{nums[0]}", f"{nums[1]}"))
print(nums[0] * nums[1])
