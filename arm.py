'''
Robot arm class
'''

from joint import Joint
from bone import Bone
from pincer import Pincer

from enum import Enum
from typing import Optional, List, Union, Tuple

class Part(Enum):
    "Define the parts that can be added"
    JOINT = Joint
    BONE = Bone
    PINCER = Pincer


class Arm():
    """
    Arm class calling the Joint and Pincer classes

    should I add a "Bone" class? Depends how we implement the animation I think
    """
    def __init__(self, parts: Optional[List[Union[Joint, Bone, Pincer]]] = []) -> None:
        self.parts = parts

    def add_part(self, part: Part) -> None:
        self.parts.append(part)

    def show_parts(self):
        for index, part in enumerate(self.parts):
            print(f'Part No: {index}\tType: {type(part)}')

    def add_instruction(self, part_name: str, movement: float) -> None:
        pass





    
        

