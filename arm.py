'''
Robot arm class
'''

from joint import Joint

from typing import Optional, List, Union, Tuple

class Arm():
    def __init__(self, parts: Optional[List[Union[Joint, float]]] = []) -> None:
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





    
        

