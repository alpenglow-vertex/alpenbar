import time


def format_time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return f"{h:.0f}h{m:.0f}m{s:.0f}s"


class Alpenbar:
    space = " "
    block = u'\u2588'

    def __init__(self, total_count: int, bar_name: str = "Alpen progress", bar_size: int = 50, enable_time: bool = True, tk_mode: bool = False):
        self.total_count = total_count
        self.bar_size = bar_size
        self.bar_name = bar_name
        self.enable_time = enable_time
        self.tk_mode = tk_mode
        if self.enable_time:
            self.time_zero = time.perf_counter()

        self.current_count = 0
        self.tick()

    def tick(self, current_count=None):
        if current_count is None:
            current_count = self.current_count
            self.current_count += 1
        else:
            self.current_count = current_count

        n_blocks = int(current_count / self.total_count * self.bar_size)
        if self.enable_time and current_count != 0:
            time_elapsed = time.perf_counter() - self.time_zero
            average_iteration_time = time_elapsed / current_count
            time_remaining = average_iteration_time * (self.total_count - current_count)
            if self.tk_mode:
                print(f'\r{self.bar_name} |{Alpenbar.block * n_blocks}{Alpenbar.space * (self.bar_size - n_blocks)}| '
                      f'{current_count}/{self.total_count}    '
                      f'ETA: {format_time(time_remaining)}    ' 
                      f'Iteration Rate: {1 / average_iteration_time:.0f}    ',
                      f'Time Elapsed: {format_time(time_elapsed)}', end='')
            else:
                print(f'\r{self.bar_name} |{Alpenbar.block * n_blocks}{Alpenbar.space * (self.bar_size - n_blocks)}| '
                      f'{current_count}/{self.total_count}    '
                      f'ETR: {format_time(time_remaining)} ' 
                      f'It/s: {1 / average_iteration_time:.0f}', end='')
        else:
            print(f'\r{self.bar_name} |{Alpenbar.block * n_blocks}{Alpenbar.space * (self.bar_size - n_blocks)}| '
                  f'{current_count}/{self.total_count}', end='')


class AlpenbarIterator:
    def __init__(self, array, bar_name: str = "Alpen progress", bar_size: int = 50, enable_time: bool = True):
        self.array = list(array)
        self.progress_bar = Alpenbar(len(self.array), bar_name=bar_name, bar_size=bar_size, enable_time=enable_time)
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i < len(self.array):
            self.progress_bar.tick()
            return self.array[self.i]
        print()
        raise StopIteration()


def track_progress(array, bar_name: str = "Alpen progress", bar_size: int = 50, enable_time: bool = True):
    return AlpenbarIterator(array, bar_name=bar_name, bar_size=bar_size, enable_time=enable_time)
