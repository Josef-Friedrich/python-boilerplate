import fire


class Calculator:
    """A simple calculator class."""

    def double(self, number: float):
        return 2 * number


def main():
    fire.Fire(Calculator)
