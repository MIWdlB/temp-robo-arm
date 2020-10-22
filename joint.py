"""
Joint Class
"""

from typing import Tuple


class Joint:
    """
    Class representing a joint

    For a joint to freely rotate
    """

    def __init__(
        self,
        name: str,
        z_axis: Tuple[float, float, float],
        min_angle: float = 0.0,
        max_angle: float = 360.0,
    ):
        self.name = name
        self.min = min_angle
        self.max = max_angle
        self.angle = min_angle

    @property
    def free_rotation(self) -> bool:
        "Check whether the joint rotates freely"
        if self.max - self.min >= 360:
            return True
        return False

    def rotate(self, displacement: float) -> None:
        "Rotate around the z-axis"

        print(f"Moving {self.name}")
        self.angle += displacement

        if self.free_rotation:
            self.angle = self.angle % 360
        elif self.angle < self.min:
            self.angle = self.min
        elif self.angle > self.max:
            self.angle = self.max

        print(f"Angle now {self.angle}")
