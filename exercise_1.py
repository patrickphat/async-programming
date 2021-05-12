import asyncio

async def print_number():
    for i in range(1,11):
        print(i)
        await asyncio.sleep(1)
async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(2)
    
    data = {"student_id":1, "student_name": "Patrick"}
    print("Done fetching")
    return data

async def main():
    task_print_number = asyncio.create_task(print_number())
    task_fetch_data = asyncio.create_task(fetch_data())
    data = await task_fetch_data
    await task_print_number
    print("hello")

    print(data)
asyncio.run(main())



