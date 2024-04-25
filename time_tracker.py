from threading import Thread
import time
import datetime


def format_timer(timer):
    return str(datetime.timedelta(seconds=timer))[2:]


class TimeTracker:
    TIMER_DURATION = 1260

    def __init__(self):
        print('initializing time tracker')
        self.xd_one_timer = self.TIMER_DURATION
        self.x_one_timer = self.TIMER_DURATION
        self.xd_two_timer = self.TIMER_DURATION

        self.xd_one_timer_thread = None
        self.x_one_timer_thread = None
        self.xd_two_timer_thread = None

    def start_xd_one_timer(self, timer):
        timer.set(format_timer(self.TIMER_DURATION))
        self.xd_one_timer = self.TIMER_DURATION
        print('starting xd one timer')
        if not self.xd_one_timer_thread or not self.xd_one_timer_thread.is_alive():
            self.xd_one_timer_thread = Thread(target=self.run_xd_one_timer, args=(timer,), daemon=True)
            self.xd_one_timer_thread.start()

    def start_x_one_timer(self, timer):
        timer.set(format_timer(self.TIMER_DURATION))
        self.x_one_timer = self.TIMER_DURATION
        if not self.x_one_timer_thread or not self.x_one_timer_thread.is_alive():
            self.x_one_timer_thread = Thread(target=self.run_x_one_timer, args=(timer,), daemon=True)
            self.x_one_timer_thread.start()

    def start_xd_two_timer(self, timer):
        timer.set(format_timer(self.TIMER_DURATION))
        self.xd_two_timer = self.TIMER_DURATION
        if not self.xd_two_timer_thread or not self.xd_two_timer_thread.is_alive():
            self.xd_two_timer_thread = Thread(target=self.run_xd_two_timer, args=(timer,), daemon=True)
            self.xd_two_timer_thread.start()

    def run_xd_one_timer(self, timer):
        while self.xd_one_timer > 0:
            time.sleep(1)
            self.xd_one_timer = self.xd_one_timer - 1
            timer.set(format_timer(self.xd_one_timer))
            print(f'xd one timer: {self.xd_one_timer}')

    def run_x_one_timer(self, timer):
        while self.x_one_timer > 0:
            time.sleep(1)
            self.x_one_timer = self.x_one_timer - 1
            timer.set(format_timer(self.x_one_timer))

    def run_xd_two_timer(self, timer):
        while self.xd_two_timer > 0:
            time.sleep(1)
            self.xd_two_timer = self.xd_two_timer - 1
            timer.set(format_timer(self.xd_two_timer))
