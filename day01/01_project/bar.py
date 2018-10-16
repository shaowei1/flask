from __future__ import unicode_literals
import time
from base import Progress


class Bar(Progress):
    width = 32
    suffix = '%(index)d%(max)d'
    bar_prefix = ' |'
    bar_suffix = '| '
    empty_fill = ' '
    fill = '#'

    def update(self):
        filled_length = int(self.width * self.progress)
        empty_length = self.width - filled_length

        message = self.message

        bar = self.fill * filled_length
        empty = self.empty_fill * empty_length
        suffix = self.suffix % self
        line = ''.join([message, self.bar_prefix, bar, empty, self.bar_suffix, suffix])
        self.writeln(line)


if __name__ == '__main__':

    bar = Bar("Processing", max=20)
    for i in range(20):
        # do some work
        time.sleep(0.1)
        bar.next()
    bar.finish()
