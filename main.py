import time

from alpenbar import Alpenbar

if __name__ == "__main__":
    this_bar = Alpenbar(bar_name="This Bar", bar_size=50, total_count=2000, enable_time=True)

    for x in range(0, 2000):
        time.sleep(0.04)
        this_bar.tick(x)