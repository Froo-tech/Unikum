import asyncio as ao
import time

lst = []


async def goida(n):
    start_time = time.time()
    await ao.sleep(2)  # Задержка для подключения файла
    for i in range(n):
        await ao.sleep(0.1)
        lst.append(i)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time} секунд")


loop = ao.get_event_loop()
loop.run_until_complete(goida(32))

