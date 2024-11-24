
from src import timeutil
from src import ioutil

from src import Grapher


CSV_PATH = "sleep.csv"

CMD_PROMPT = "?> "
QUIT_CMDS = {"q", "quit"}
INPUT_CMDS = {"i", "input"}
GRAPH_CMDS = {"g", "graph"}

DATETIME_FMT = timeutil.get_printable_datetime_format()

START_TIME_PROMPT = f"Bedtime? (24-hour time, {DATETIME_FMT}): "
STOP_TIME_PROMPT = f"Wake time? (24-hour time, {DATETIME_FMT}): "
INV_CMD_MSG = "Invalid command!\n[Q]uit, [I]nput, [G]raph"
INV_TIME_MSG = "Invalid time!"


running = True
grapher = Grapher(CSV_PATH)


def main():
    global grapher
    grapher = Grapher(CSV_PATH)
    while running:
        response = input(CMD_PROMPT).lower().strip()
        dispatch(response)


def dispatch(cmd):
    if cmd in QUIT_CMDS:
        global running
        running = False
    elif cmd in INPUT_CMDS:
        get_new_times()
    elif cmd in GRAPH_CMDS:
        show_graph()
    else:
        print(INV_CMD_MSG)


def get_new_times():
    start = timeutil.str_to_datetime(input(START_TIME_PROMPT).strip())
    while start is None:
        print(INV_TIME_MSG)
        start = timeutil.str_to_datetime(input(START_TIME_PROMPT).strip())

    stop = timeutil.str_to_datetime(input(STOP_TIME_PROMPT).strip())
    while start is None:
        print(INV_TIME_MSG)
        stop = timeutil.str_to_datetime(input(STOP_TIME_PROMPT).strip())

    start_timestamp = timeutil.datetime_to_timestamp(start)
    stop_timestamp = timeutil.datetime_to_timestamp(stop)
    ioutil.write_csv(CSV_PATH, start_timestamp, stop_timestamp)


def show_graph():
    grapher()


if __name__ == "__main__":
    main()

