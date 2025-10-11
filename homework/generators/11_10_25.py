def sliding_window(seq, num):
    """
    Напиши генератор sliding_window(seq, n), который будет возвращать последовательность "окон" длиной n по списку seq.
    # [(1,2,3), (2,3,4), (3,4,5)]
    """
    length = len(seq)
    seq_id = 0
    while seq_id + num <= length:
        yield seq[seq_id : seq_id + num]
        seq_id += 1


print(list(sliding_window([1, 2, 3, 4, 5], 3)))

print("\n" + "#" * 80 + "\n")


def cycle_words(words):
    """
    Напиши генератор cycle_words(words), который будет бесконечно выдавать элементы списка words по кругу.
    gen = cycle_words(["red", "green", "blue"])
    [next(gen) for _ in range(7)]
    # ['red', 'green', 'blue', 'red', 'green', 'blue', 'red']

    по итогу реализация подсмотрел у cycle
    """
    # cycle_words_gen = cycle(words)
    # while True:
    #     yield next(cycle_words_gen)
    saved = []
    for word in words:
        saved.append(word)

    while saved:
        for word in saved:
            yield word


gen = cycle_words(["red", "green", "blue"])
print(list(next(gen) for _ in range(5)))

print("\n" + "#" * 80 + "\n")


def accumulator():
    """
    Создай генератор accumulator(), который принимает через .send() число и возвращает текущую сумму.
    """
    acc = 0
    while True:
        received = yield acc
        acc += received


gen = accumulator()
next(gen)  # запускаем
print(gen.send(5))  # 5
print(gen.send(3))  # 8
print(gen.send(-2))  # 6

print("\n" + "#" * 80 + "\n")


def filter_logs(li: list, level: str):
    """
    Есть строки лога. Сделай генератор filter_logs(lines, level), который возвращает только те строки, где есть level (например "ERROR").
    # ['ERROR: invalid token', 'ERROR: file not found']
    """
    for log in li:
        if level in log:
            yield log


logs = [
    "INFO: start process",
    "ERROR: invalid token",
    "INFO: finished",
    "ERROR: file not found",
]

print(list(filter_logs(logs, "ERROR")))

print("\n" + "#" * 80 + "\n")


def batcher(seq, size: int):
    """
    Напиши генератор batcher(iterable, size), который будет собирать элементы в пакеты по size.
    # [(0,1,2), (3,4,5), (6,7,8), (9,)]

    Не придумал куда тут генератор вставить.
    """
    seq = list(seq)
    result = []
    while seq:
        temp_list = []
        try:
            for _ in range(size):
                temp_list.append(seq.pop(0))
            result.append(tuple(temp_list))
        except Exception:
            result.append(tuple(temp_list))
    return result


# def batcher_2(seq, size: int):
#     """
#     как я понял, нужно что б seq было не в памяти.
#     но я не могу придумать, как запоминать, где остановлся в предыдущий раз.
#     если доступ по индексу, то это загрузка в память.
#     если срезы - тоже в память.
#
#     """
# result = []
# cur_id = 0
#
# def format_list(seq):
#     temp = []
#     for _ in range(size):
#         nonlocal cur_id
#         temp.append(seq[cur_id + _])
#         cur_id +=size
#     yield tuple(temp)
#
# while seq:
#     print(cur_id, seq[cur_id])
#     result.append(format_list(seq))
# return result
###########
# cursor = 0
# result = []
# temp_list = []
# for i in range(size):
#     temp_list.append(seq[cursor : cursor + size])
#     cursor += size
#
# result.append(temp_list)
# return result
###########
# cursor = 0
# result = []
# def return_size_list(seq, cursor, size):
#     temp_list = []
#     for i in range(size):
#         temp_list.append(seq[cursor + i])
#
#     yield tuple(temp_list)
#
# while seq:
#     print(seq)
#     result.append(return_size_list(seq, cursor, size))
#     cursor += size
#
# return result

print(list(batcher(range(10), 3)))
# print(list(batcher_2(range(3), 3)))
