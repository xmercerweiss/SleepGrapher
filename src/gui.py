import tkinter as tk


class RootWindow:

    _TITLE = "Sleep Grapher"
    _GEO = "500x500"

    def __init__(self):
        self._root = self._init_root()
        self._start, self._stop = self._init_time_inputs()

    def _init_root(self):
        root = tk.Tk()
        root.title(self._TITLE)
        root.geometry(self._GEO)
        return root

    def _init_time_inputs(self):
        start = TimeInput(self._root)
        start.panel.grid(row=0, column=0, sticky="NSEW")
        stop = TimeInput(self._root)
        stop.panel.grid(row=1, column=0, sticky="NSEW")
        return start, stop

    def launch(self):
        self._root.mainloop()
        return False


class TimeInput:

    # Format: HH:mm MM/dd/YYYY
    _GRID_WIDTH = 9

    _LABELS = (
        (1, ":"),
        (3, " "),
        (5, "/"),
        (7, "/")
    )

    def __init__(self, parent):
        self._parent = parent
        self._panel = self._init_panel()
        self._init_labels()
        self._hour, self._minute, self._month, self._day, self._year \
            = self._init_entries()

    def _init_panel(self):
        panel = tk.Frame(self._parent)
        #panel.grid_propagate(0)
        for i in range(self._GRID_WIDTH):
            panel.columnconfigure(i, weight=1)
        return panel

    def _init_labels(self):
        for index, text in self._LABELS:
            label = tk.Label(self._panel, text=text)
            label.grid(row=0, column=index)

    def _init_entries(self):
        hour = tk.Entry(self._panel, width=2)
        hour.grid(row=0, column=0)

        minute = tk.Entry(self._panel, width=2)
        minute.grid(row=0, column=2)

        month = tk.Entry(self._panel, width=2)
        month.grid(row=0, column=4)

        day = tk.Entry(self._panel, width=2)
        day.grid(row=0, column=6)

        year = tk.Entry(self._panel, width=4)
        year.grid(row=0, column=8)
        
        return hour, minute, month, day, year

    def get_time(self):
        return 0

    @property
    def panel(self):
        return self._panel

