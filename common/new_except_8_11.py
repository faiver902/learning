try:
    # допустим, мы собрали несколько ошибок
    g = True
    h = True
    if g:
        raise ExceptionGroup("oops", [ValueError("bad value"), TypeError("bad type")])
    if h:
        raise ExceptionGroup("oops", [ValueError("bad value"), TypeError("bad type")])
except* ValueError as eg:
    print("Обработка всех ValueError из группы:", eg)
except* TypeError as eg:
    print("Обработка всех TypeError из группы:", eg)
