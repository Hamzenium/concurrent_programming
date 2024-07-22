import time
import threading
from workers import SquaredSumWorkers 
from workers import SleepWorkers

def main():
    current_workers = []
    calc_time = time.time()
    
    # Create and start SquaredSumWorkers
    for i in range(5):
        maximum_value = (i + 1) * 1000000
        square = SquaredSumWorkers.SquaredSumWorkers(n=maximum_value)
        current_workers.append(square)
    
    # Join SquaredSumWorkers threads
    for worker in current_workers:
        worker.join()
    
    print("Calculate sum of squares took:", round(time.time() - calc_time, 1))
    
    current_workers = []
    
    # Create and start SleepWorkers
    for sec in range(1, 6):
        sleep = SleepWorkers.SleepyWorkers(seconds=sec)
        current_workers.append(sleep)
    
    sleep_start_time = time.time()
    
    # Join SleepWorkers threads
    for worker in current_workers:
        worker.join()
    
    print("Sleep took:", round(time.time() - sleep_start_time, 1))

if __name__ == "__main__":
    main()
