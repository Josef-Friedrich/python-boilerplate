import fire


class Calculator(object):
    """A simple calculator class."""

    def double(self, number: float):
        return 2 * number


def main():
    fire.Fire(Calculator)
