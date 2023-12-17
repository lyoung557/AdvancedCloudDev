import asyncio

async def task(name, delay):
    print(f'Task {name} started')
    await asyncio.sleep(delay)
    print(f'Task {name} finished')

async def main():
    await asyncio.gather(
        task('A', 2),
        task('B', 3),
        task('C', 1)
    )

asyncio.run(main())
