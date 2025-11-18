
import time

def timer(duration):
    start_time = time.time()

    while True:
        now_time = int(time.time() - start_time)

        if now_time > duration:
            break

        mins , sec = divmod(now_time,60)
        print(f"{mins:02d} : {sec:02d}",end="\r")
        time.sleep(1)


timer(10)