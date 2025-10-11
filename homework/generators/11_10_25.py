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


def filter_logs(li: list):
    """
    Есть строки лога. Сделай генератор filter_logs(lines, level), который возвращает только те строки, где есть level (например "ERROR").
    """
    for log in li:
        if "ERROR" in log:
            yield log


logs = [
    "INFO: start process",
    "ERROR: invalid token",
    "INFO: finished",
    "ERROR: file not found",
]

list(filter_logs(logs, "ERROR"))
# ['ERROR: invalid token', 'ERROR: file not found']
