from arm import Arm
from joint import Joint
from bone import Bone

def main():
    "Function to contsruct an arm and input movements"

    parts = [
        Joint(name='r1', z_axis=[0,0,1]),
        Bone(length= 5),
        Joint(name='r2', z_axis=[0,1,0])
    ]

    robot_arm = Arm(parts=parts)

    


if __name__ == "__main__":
    main()
