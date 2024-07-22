import time
import threading

def main():
    pass
    
def calculate_sqaures(n):
    sum_sqaures = 0
    for i in range(n):
        sum_sqaures = i ** 2
    print(sum_sqaures)

def sleep_little(seconds):
    time.sleep(seconds)


if __name__ == "__main__":
    current_threads = []
    calc_time = time.time()
    for i in range(5):
        maximum_value = (i+1) * 1000000
        t = threading.Thread(target=calculate_sqaures, args=(maximum_value,))
        t.start()
        current_threads.append(t)
    for i in range(len(current_threads)):
        current_threads[i].join()

    print("calculate sum of sqaures took:", round(time.time() - calc_time,1))
    t = threading.Thread(target=calculate_sqaures, args=(maximum_value,))
    t.start()

    current_threads = []
    for i in range(len(current_threads)):
        current_threads[i].join()
    sleep_start_time =  time.time() 

    for i in range(1,5):
        sleep_little(i)
    print("sleep took: ", time.time() - calc_time )
    main()
