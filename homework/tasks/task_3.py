import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    # Необходимо выполнить все полученные корутины, затем упорядочить их результаты
    # по полю number и вернуть строку, состоящую из склеенных полей key.
    #
    # Пример:
    # r1 = Ticket(number=2, key='мыла')
    # r2 = Ticket(number=1, key='мама')
    # r3 = Ticket(number=3, key='раму')
    #
    # Результат: 'мамамылараму'
    #
    tasks = [asyncio.create_task(coro) for coro in coros]
    list_ = [await task for task in tasks]
    return ''.join(el.key for el in sorted(list_, key=lambda x: x.number))


async def just_return_ticket(t: Ticket) -> Ticket:
    return t

tickets = [
        Ticket(number=2, key='мыла'),
        Ticket(number=1, key='мама'),
        Ticket(number=3, key='раму'),
    ]
coros = [just_return_ticket(t) for t in tickets]


if __name__ == '__main__':
    print(asyncio.run(coroutines_execution_order(coros)))


# import asyncio
# import random


# async def process_task(task: int) -> str:
#     print(f'\tprocess_task({task}) start')
#     await asyncio.sleep(random.random())
#     result = f'this is result: {task * 2}'
#     print(f'\tprocess_task({task}) end')
#     return result


# async def main():
#     print(f'main start')
#     t1 = asyncio.create_task(process_task(1))
#     t2 = asyncio.create_task(process_task(2))
#     t3 = asyncio.create_task(process_task(3))
#     #print(f'await t1')
#     await t1
#     #print(f'await t2')
#     await t2
#     print(f'await t3')
#     await t3
#     print(f'main end')


# if __name__ == '__main__':
#     asyncio.run(main())