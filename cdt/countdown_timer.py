import time

class Timer:
    def __init__(self, init_time):
        self.init_time = init_time
        self.curr_time = init_time
        self.status = False
    def start(self):
        self.status = True
        while self.curr_time>0:
            print(f"{self.curr_time} is left!")
            time.sleep(1)
            self.curr_time -= 1
        print('HAPPY NEW YEAR!')
        self.status = False
    def pause(self):
        self.status = False
    def resume(self):
        if self.status is False:
            self.start()
    def stop(self):
        self.status = False
        self.curr_time = 0
        print('Timer stopped!')

t = Timer(10)
t.start()
