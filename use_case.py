import time


def test_time():
    start = time.time()
    while True:
        print("we are on a test")

        current_time = time.time()
        period = current_time-start

        print(period)

        if (period > 5.0):
            break


rps = test_time()
    


