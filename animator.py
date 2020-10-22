import matplotlib as plt

from arm import Arm


class Animator:
    """
    Creates and displays an animation
    """
    def __init__(self, arm: Arm) -> None:
        self.arm = arm
    
    
