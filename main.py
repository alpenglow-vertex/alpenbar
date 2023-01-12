import time

from alpenbar import Alpenbar, track_progress

if __name__ == "__main__":
    this_bar = Alpenbar(total_count=2000, bar_name="This Bar", bar_size=50, enable_time=True)
    for x in range(0, 2000):
        time.sleep(0.004)
        this_bar.tick(x)

    for x in track_progress([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
        time.sleep(.5)
    print("next computation...")
