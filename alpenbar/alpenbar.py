import time


class Alpenbar:
    space = " "
    block = u'\u2588'

    def __init__(self, bar_name: str, bar_size: int, total_count: int, enable_time: bool):
        self.bar_name = bar_name
        self.bar_size = bar_size
        self.total_count = total_count
        self.enable_time = enable_time
        if self.enable_time:
            self.time_zero = time.perf_counter()

    def tick(self, current_count: int):
        n_blocks = int(current_count / self.total_count * self.bar_size)
        if self.enable_time and current_count != 0:
            time_remaining = (time.perf_counter() - self.time_zero) / current_count * (self.total_count - current_count)
            m, s = divmod(time_remaining, 60)
            h, m = divmod(m, 60)
            print(f'\r{self.bar_name} |{Alpenbar.block * n_blocks}{Alpenbar.space * (self.bar_size - n_blocks)}| '
                  f'{current_count}/{self.total_count}    '
                  f'Estimated Time Remaining: {h:.0f}h{m:.0f}m{s:.0f}s', end='')
        else:
            print(f'\r{self.bar_name} |{Alpenbar.block * n_blocks}{Alpenbar.space * (self.bar_size - n_blocks)}| '
                  f'{current_count}/{self.total_count}', end='')

