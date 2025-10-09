import os
import time
from multiprocessing import Manager, Process, current_process


def accumulate(shared_dict, shared_list):
    proc = current_process().name
    pid = os.getpid()
    print(f"[{proc} | pid={pid}] Пишу в разделяемые структуры...")
    for i in range(3):
        key = f"k{i}"
        shared_dict[key] = (pid, i)
        shared_list.append((pid, i))
        print(f"[{proc} | pid={pid}] dict[{key}]={(pid, i)}, list+= {(pid, i)}")
        time.sleep(0.1)


if __name__ == "__main__":
    with Manager() as manager:
        shared_dict = manager.dict()
        shared_list = manager.list()

        p1 = Process(
            target=accumulate, args=(shared_dict, shared_list), name="Worker-1"
        )
        p2 = Process(
            target=accumulate, args=(shared_dict, shared_list), name="Worker-2"
        )
        p1.start()
        p2.start()
        p1.join()
        p2.join()

        print("[Main] Итоговый shared_dict:", dict(shared_dict))
        print("[Main] Итоговый shared_list:", list(shared_list))
        print("[Main] Готово.")
