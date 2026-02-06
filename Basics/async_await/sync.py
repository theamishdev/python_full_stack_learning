import time

def fake_api_call(name):
    start = time.time()
    print(f"{name} started at", start)

    time.sleep(3)

    end = time.time()
    print(f"{name} ended at", end)
    print(f"{name} took {end - start:.2f} seconds\n")


overall_start = time.time()

fake_api_call("task 1")
fake_api_call("task 2")

overall_end = time.time()
print("Total time:", overall_end - overall_start)
