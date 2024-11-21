from threading import Thread
import time
import datetime
import winsound


def format_timer(timer):
    return str(datetime.timedelta(seconds=timer))[2:]


class TimeTracker:
    TIMER_DURATION_XD = 1260  # = 21 minutes = 30 sc2 minutes
    TIMER_DURATION_X = 630  # = 10.5 minutes = 15 sc2 minutes

    def __init__(self):
        self.xd_one_timer = self.TIMER_DURATION_XD
        self.x_one_timer = self.TIMER_DURATION_XD
        self.xd_two_timer = self.TIMER_DURATION_XD

        self.xd_one_timer_thread = None
        self.x_one_timer_thread = None
        self.xd_two_timer_thread = None

    def start_xd_one_timer(self, timer):
        timer.set(format_timer(self.TIMER_DURATION_XD))
        self.xd_one_timer = self.TIMER_DURATION_XD
        if not self.xd_one_timer_thread or not self.xd_one_timer_thread.is_alive():
            self.xd_one_timer_thread = Thread(target=self.run_xd_one_timer, args=(timer,), daemon=True)
            self.xd_one_timer_thread.start()

    def start_x_one_timer(self, timer):
        timer.set(format_timer(self.TIMER_DURATION_X))
        self.x_one_timer = self.TIMER_DURATION_X
        if not self.x_one_timer_thread or not self.x_one_timer_thread.is_alive():
            self.x_one_timer_thread = Thread(target=self.run_x_one_timer, args=(timer,), daemon=True)
            self.x_one_timer_thread.start()

    def start_xd_two_timer(self, timer):
        timer.set(format_timer(self.TIMER_DURATION_XD))
        self.xd_two_timer = self.TIMER_DURATION_XD
        if not self.xd_two_timer_thread or not self.xd_two_timer_thread.is_alive():
            self.xd_two_timer_thread = Thread(target=self.run_xd_two_timer, args=(timer,), daemon=True)
            self.xd_two_timer_thread.start()

    def run_xd_one_timer(self, timer):
        while self.xd_one_timer > 0:
            time.sleep(1)
            self.xd_one_timer = self.xd_one_timer - 1
            timer.set(format_timer(self.xd_one_timer))
        winsound.PlaySound('SystemHand', winsound.SND_ALIAS)

    def run_x_one_timer(self, timer):
        while self.x_one_timer > 0:
            time.sleep(1)
            self.x_one_timer = self.x_one_timer - 1
            timer.set(format_timer(self.x_one_timer))
        winsound.PlaySound('SystemHand', winsound.SND_ALIAS)

    def run_xd_two_timer(self, timer):
        while self.xd_two_timer > 0:
            time.sleep(1)
            self.xd_two_timer = self.xd_two_timer - 1
            timer.set(format_timer(self.xd_two_timer))
        winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
