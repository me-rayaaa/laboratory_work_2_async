"""Шаг 1. Синхронная версия: десять задач, каждая ждёт секунду, всё строго по очереди."""

import time

from timer import print_time

TASKS_COUNT = 10


def work(n: int) -> None:
    print("start", n)
    time.sleep(1)
    print("done", n)


def main() -> None:
    for number in range(1, TASKS_COUNT + 1):
        work(number)


if __name__ == "__main__":
    with print_time():
        main()