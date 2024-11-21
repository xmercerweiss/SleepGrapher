from src import RootWindow

from utils import Grapher


CSV_PATH = "data/sleep.csv"


def main():
    app = RootWindow()
    running = True
    while running:
        running = app.launch()


if __name__ == "__main__":
    main()

