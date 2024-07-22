import threading

class SquaredSumWorkers(threading.Thread):
    def __init__(self,n, **kwargs):
        super(SquaredSumWorkers, self).__init__(**kwargs) 
        self._n = n
        self.start()

    def calculate_squares(self):
        sum_sqaures = 0
        for i in range(self._n):
            sum_sqaures = i ** 2
        print(sum_sqaures) 

    def run(self):
        self.calculate_squares()