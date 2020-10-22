"""
Defines a pincer class to put on the end of an arm
"""


class Pincer:
    """
    Pincer class
    """

    def __init__(self, max_width: float, min_width: float):
        self.max_width = max_width
        self.min_width = min_width
        self.pinch = max_width

    def move(self, move_distance: float) -> None:
        "Move the pincer open or closed"
        self.pinch += move_distance

        if self.pinch > self.max_width:
            self.pinch = self.max_width
        elif self.pinch < self.min_width:
            self.pinch = self.min_width
