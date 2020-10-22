"""
Robot arm class
"""

from joint import Joint
from bone import Bone
from pincer import Pincer

from enum import Enum
from typing import Optional

import numpy as np
from math import sin, cos, tan

class Part(Enum):
    "Define the parts that can be added"
    JOINT = Joint
    BONE = Bone
    PINCER = Pincer


class Arm:
    """
    Arm class calling the Joint and Pincer classes

    should I add a "Bone" class? Depends how we implement the animation I think
    """

    def __init__(self, parts: List[Part] = list()) -> None:
        self.parts = parts

    def add_part(self, part: Part) -> None:
        self.parts.append(part)

    def show_parts(self) -> None:
        for index, part in enumerate(self.parts):
            print(f"Part No: {index}\tType: {type(part)}")

    def add_instruction(self, part_name: str, movement: float) -> None:
        pass

    def forward_kinematics(self) -> None:
        "Verbose named fk function"
        return self.fk()

    def fk(self) -> None:
        # first part will always start flat on the ground
        z_axis = (0,0,1)
        normal = (1,0,0)
        position = (0,0,0)

        for part in self.parts.reverse():
            

            matrix = [
                [cos(t), -1*sin(t)*cos(a), sin(t)*sin(a), r*cos(t)],
                [sin(t), cos(t)*cos(a), -1*cos(t)*sin(a), r*sin(t)],
                [0, sin(a), cos(a), d],
                [0, 0, 0, 1],
            ]



    @staticmethod
    def animate(self) -> None:
        pass
