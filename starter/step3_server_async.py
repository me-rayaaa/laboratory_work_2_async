"""Шаг 3б. Асинхронный "сервер": все клиенты принимаются сразу.

Пока bob ждёт базу, event loop успевает ответить всем остальным.
"""

import asyncio

from timer import log, print_time

CLIENTS = [
    ("alice", 0.5),
    ("bob", 5.0),
    ("carol", 0.5),
    ("dave", 0.5),
    ("eve", 0.5),
]


async def handle_request(client: str, duration: float) -> None:
    log(client + ": запрос принят")
    await asyncio.sleep(duration)
    log(client + ": ответ отправлен")


async def main() -> None:
    incoming = [handle_request(name, db_time) for name, db_time in CLIENTS]
    await asyncio.gather(*incoming)


if __name__ == "__main__":
    with print_time():
        asyncio.run(main())
