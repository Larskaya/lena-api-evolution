
# для двух задач: поиск соседей при добавление в сектор + уменьшение еды в секторах


import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Ждём завершения обеих задач (это должно занять
    # около 2 секунд.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

# ------------------------------------------------------------------------------

# get data
# update data 
# set data 

async def update_after(time, request):
    await asyncio.sleep(time)
    print('before update')

async def main():
    get_data = 0