"""Шаг 3а. Синхронный "сервер": клиенты обслуживаются строго по очереди.

Пока база отвечает bob-у 5 секунд, остальные клиенты даже не приняты.
"""

import time

from timer import log, print_time

CLIENTS = [
    ("alice", 0.5),
    ("bob", 5.0),
    ("carol", 0.5),
    ("dave", 0.5),
    ("eve", 0.5),
]


def handle_request(client: str, duration: float) -> None:
    log(client + ": запрос принят")
    time.sleep(duration)
    log(client + ": ответ отправлен")


def main() -> None:
    for name, db_time in CLIENTS:
        handle_request(name, db_time)


if __name__ == "__main__":
    with print_time():
        main()
