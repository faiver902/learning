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
list(next(gen) for _ in range(5))

print("\n" + "#" * 80 + "\n")


def accumulator():
    summ = 0
    yield summ


gen = accumulator()
next(gen)  # запускаем
print(gen.send(5))  # 5
print(gen.send(3))  # 8
print(gen.send(-2))  # 6
