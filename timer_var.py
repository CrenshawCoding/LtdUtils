import tkinter
class TimerVar(tkinter.IntVar):
    def get(self) -> int:
        return self.get()