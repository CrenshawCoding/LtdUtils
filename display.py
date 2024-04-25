import tkinter
import time_tracker


class Display:
    def __init__(self):

        self.time_tracker = time_tracker.TimeTracker()

        self.root = tkinter.Tk()
        self.root.title("LtdUtils")

        self.cooldown_frame = tkinter.Frame(self.root, padx=30)
        self.xd_one_frame = tkinter.Frame(self.cooldown_frame)
        self.x_one_frame = tkinter.Frame(self.cooldown_frame)
        self.xd_two_frame = tkinter.Frame(self.cooldown_frame)

        self.xd_one_button = tkinter.Button(self.xd_one_frame, text='@xd', command=self.xd_one_button_callback)
        self.x_one_button = tkinter.Button(self.x_one_frame, text='@x', command=self.x_one_button_callback)
        self.xd_two_button = tkinter.Button(self.xd_two_frame, text='@xd', command=self.xd_two_button_callback)

        self.xd_one_timer = tkinter.StringVar()
        self.x_one_timer = tkinter.StringVar()
        self.xd_two_timer = tkinter.StringVar()

        self.xd_one_text = tkinter.Label(self.xd_one_frame, textvariable=self.xd_one_timer)
        self.x_one_text = tkinter.Label(self.x_one_frame, textvariable=self.x_one_timer)
        self.xd_two_text = tkinter.Label(self.xd_two_frame, textvariable=self.xd_two_timer)

        self.setup_cooldown_frame()

    def setup_cooldown_frame(self):
        self.cooldown_frame.grid(column=0, row=0)
        self.xd_one_frame.grid(column=0, row=0, padx=10)
        self.x_one_frame.grid(column=1, row=0, padx=10)
        self.xd_two_frame.grid(column=2, row=0, padx=10)

        self.xd_one_button.grid(column=0, row=0)
        self.x_one_button.grid(column=1, row=0)
        self.xd_two_button.grid(column=2, row=0)

        self.xd_one_text.grid(column=0, row=1)
        self.x_one_text.grid(column=1, row=1)
        self.xd_two_text.grid(column=2, row=1)

    def xd_one_button_callback(self):
        self.time_tracker.start_xd_one_timer(self.xd_one_timer)

    def x_one_button_callback(self):
        self.time_tracker.start_x_one_timer(self.x_one_timer)

    def xd_two_button_callback(self):
        self.time_tracker.start_xd_two_timer(self.xd_two_timer)

    @staticmethod
    def run():
        tkinter.mainloop()
