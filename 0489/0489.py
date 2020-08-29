# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
        
        def dfs(i, j, vis, di):
            robot.clean()
            vis.add((i, j))
            for _ in range(4):
                di = (di+1) % 4
                robot.turnRight()
                if (i+dirs[di][0], j+dirs[di][1]) not in vis and robot.move():
                    dfs(i+dirs[di][0], j+dirs[di][1], vis, di)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                    
        dfs(0, 0, set(), 0)
                
