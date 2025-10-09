import os
import time
from multiprocessing import Pipe, Process, current_process


def worker(pipe_end):
    proc = current_process().name
    pid = os.getpid()
    print(f"[{proc} | pid={pid}] Старт worker. Жду сообщение от главного...")
    msg = pipe_end.recv()
    print(f"[{proc} | pid={pid}] Получил от главного: {msg!r}")

    reply = {"ok": True, "worker_pid": pid}
    print(f"[{proc} | pid={pid}] Отправляю ответ: {reply}")
    pipe_end.send(reply)

    print(f"[{proc} | pid={pid}] Закрываю свой конец канала.")
    pipe_end.close()


if __name__ == "__main__":
    print("[Main] Создаю Pipe()...")
    conn_main, conn_child = Pipe(duplex=True)  # двусторонний канал

    print("[Main] Стартую процесс worker...")
    p = Process(target=worker, args=(conn_child,), name="WorkerProcess")
    p.start()

    print("[Main] Отправляю привет рабочему...")
    conn_main.send({"cmd": "hello", "ts": time.time()})

    print("[Main] Жду ответ от worker...")
    reply: dict = conn_main.recv()
    print(f"[Main] Ответ от worker: {reply}")

    print("[Main] Закрываю свой конец канала.")
    conn_main.close()

    print("[Main] Жду завершения процесса...")
    p.join()
    print("[Main] Готово.")
