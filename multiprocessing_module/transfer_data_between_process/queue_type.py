import os
import time
from multiprocessing import JoinableQueue, Process, current_process

SENTINEL = None  # маркер завершения


def consumer(task_q):
    proc = current_process().name
    pid = os.getpid()
    print(f"[{proc} | pid={pid}] Старт consumer.")
    while True:
        item = task_q.get()  # блокируется, пока нет данных
        if item is SENTINEL:
            print(f"[{proc} | pid={pid}] Получил SENTINEL. Завершаюсь.")
            task_q.task_done()  # отмечаем «задачу завершённой»
            break
        print(f"[{proc} | pid={pid}] Обрабатываю задачу: {item}")
        time.sleep(0.2)  # имитация работы
        print(f"[{proc} | pid={pid}] Готово: {item}")
        task_q.task_done()  # сигнал, что задача обработана


def producer(task_q, items):
    proc = current_process().name
    pid = os.getpid()
    print(f"[{proc} | pid={pid}] Старт producer. Кладём задачи.")
    for it in items:
        print(f"[{proc} | pid={pid}] put -> {it}")
        task_q.put(it)
    print(f"[{proc} | pid={pid}] Кладём SENTINEL для каждого consumer.")
    # допустим, у нас будет 2 потребителя:
    task_q.put(SENTINEL)
    task_q.put(SENTINEL)


if __name__ == "__main__":
    task_q = JoinableQueue()

    # два потребителя
    c1 = Process(target=consumer, args=(task_q,), name="Consumer-1")
    c2 = Process(target=consumer, args=(task_q,), name="Consumer-2")
    c1.start()
    c2.start()

    # один продюсер
    items = [f"task-{i}" for i in range(5)]
    p = Process(target=producer, args=(task_q, items), name="Producer")
    p.start()

    print("[Main] Жду, когда очередь будет полностью обработана (join)...")
    task_q.join()  # блок до тех пор, пока task_done() не будет вызван на ВСЕ put
    print("[Main] Все задачи обработаны.")

    p.join()
    c1.join()
    c2.join()
    print("[Main] Готово.")
