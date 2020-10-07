import matplotlib as plt

from arm import Arm

class Animator():
    def __init__(self, arm: Arm, movements: List[float]) -> None:
        self.arm = arm
        self.movements = movements # TODO add a standard for movements

    