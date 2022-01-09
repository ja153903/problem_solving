"""
1041. Robot Bounded In Circle

=======
Problem
=======

On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

* "G": go straight 1 unit;
* "L": turn 90 degrees to the left;
* "R": turn 90 degrees to the right.

The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

========
Approach
========

Approach 1:
    One thing that i can think of intuitively is checking to see if the robot either returns back to the destination it started
    or if it changes direction. If the robot at any point changes the direction its pointing, this means that it's possible in
    the infiniite amount of moves it makes that it'll circle back to the start
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        direction = "N"

        direction_map = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0)
        }

        for instruction in instructions:
            if instruction == "G":
                dx, dy = direction_map.get(direction)
                x += dx
                y += dy
            elif instruction == "L":
                if direction == "N":
                    direction = "W"
                elif direction == "S":
                    direction = "E"
                elif direction == "E":
                    direction = "N"
                else:
                    direction = "S"
            else:
                if direction == "N":
                    direction = "E"
                elif direction == "S":
                    direction = "W"
                elif direction == "E":
                    direction = "S"
                else:
                    direction = "N"

        return direction != "N" or (x == 0 and y == 0)
        

if __name__ == "__main__":
    s = Solution()

    instructions = "GGLLGG"
    assert s.isRobotBounded(instructions)

