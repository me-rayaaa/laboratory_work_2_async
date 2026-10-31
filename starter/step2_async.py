"""Шаг 2. То же самое на asyncio.

run_one_by_one - вариант 2а (await в цикле, ~10 с)
main           - вариант 2б (gather, ~1 с), он и запускается
run_with_tasks - доп. вариант через create_task (~1 с)
"""

import asyncio

from timer import print_time

TASKS_COUNT = 10
PAUSE = 1


async def work(n: int) -> None:
    print("start", n)
    await asyncio.sleep(PAUSE)  # здесь корутина отдаёт управление event loop
    print("done", n)


async def run_one_by_one() -> None:
    for i in range(1, TASKS_COUNT + 1):
        await work(i)


async def run_with_tasks() -> None:
    started = []
    for i in range(1, TASKS_COUNT + 1):
        started.append(asyncio.create_task(work(i)))
    for task in started:
        await task


async def main() -> None:
    jobs = [work(i) for i in range(1, TASKS_COUNT + 1)]
    await asyncio.gather(*jobs)


if __name__ == "__main__":
    with print_time():
        asyncio.run(main())