'''
Joint Class
'''

from typing import Bool


class Joint():
    """
    Class representing a joint
    If 'bend' is true the joint will bend like an elbow
    else it will rotate like a wrist.

    For a joint to freely rotate
    """

    def __init__(self, name: str, bend: Bool, min_angle: float, max_angle: float):
        self.name = name
        self.bend = bend
        self.min = min_angle  
        self.max = max_angle
        self.angle = min_angle

    @property
    def free_rotation(self) -> bool:
        "Check whether the joint rotates freely"
        if self.max - self.min >= 360:
            return self.free_rotation


    def move(self, displacement: float) -> None:
        print(f'Moving {self.name}')
        self.angle += self.displacement
    
        if self.free_rotation:
            self.angle = self.angle % 360
        elif self.angle < self.min:
            self.angle = self.min
        elif self.angle > self.max:
            self.angle = self.max
    
        print(f'Angle now {self.angle}')