import asyncio
import time

async def task(name):
    start = time.time()
    print(f"{name} started at", start)

    await asyncio.sleep(3)

    end = time.time()
    print(f"{name} ended at", end)
    print(f"{name} took {end - start:.2f} seconds\n")


async def main():
    overall_start = time.time()

    await asyncio.gather(
        task("Task 1"),
        task("Task 2")
    )

    overall_end = time.time()
    print("Total time:", overall_end - overall_start)



asyncio.run(main())
