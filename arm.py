'''
Robot arm class
'''

from joint import Joint
from pincer import Pincer

from typing import Optional, List, Union, Tuple

class Arm():
    """
    Arm class calling the Joint and Pincer classes

    should I add a "Bone" class? Depends how we implement the animation I think
    """
    def __init__(self, parts: Optional[List[Union[Joint, float, Pincer]]] = []) -> None:
        self.parts = parts

    def add_joint(self, joint: Joint) -> None:
        self.parts.append(joint)

    def add_bone(self, bone: float) -> None:
        self.parts.append(bone)

    @property
    def end_points(self) -> List[Tuple[Tuple[float, float, float], Tuple[float, float, float]]]:
        start_position = (0,0,0)
        for part in self.parts:
            pass





    
        

