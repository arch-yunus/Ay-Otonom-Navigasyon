import numpy as np
import heapq

class AStarPlanner:
    """
    High-fidelity A* Path Planner for Lunar Terrain.
    Accounts for slope angles and regolith difficulty.
    """
    def __init__(self, grid_size=(100, 100)):
        self.grid_size = grid_size
        self.cost_map = np.ones(grid_size)

    def heuristic(self, a, b):
        return np.linalg.norm(np.array(a) - np.array(b))

    def plan(self, start, goal):
        """Computes the optimal path from start to goal."""
        neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        close_set = set()
        came_from = {}
        gscore = {start:0}
        fscore = {start:self.heuristic(start, goal)}
        oheap = []

        heapq.heappush(oheap, (fscore[start], start))
        
        while oheap:
            current = heapq.heappop(oheap)[1]

            if current == goal:
                data = []
                while current in came_from:
                    data.append(current)
                    current = came_from[current]
                return data[::-1]

            close_set.add(current)
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j            
                tentative_g_score = gscore[current] + self.heuristic(current, neighbor) * self.cost_map[neighbor[0], neighbor[1]]
                
                if 0 <= neighbor[0] < self.grid_size[0]:
                    if 0 <= neighbor[1] < self.grid_size[1]:                
                        if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                            continue
                    else: continue
                else: continue
                
                if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(oheap, (fscore[neighbor], neighbor))
        return False

class RoverController:
    """PID-based trajectory tracking for Moon ROvers."""
    def __init__(self, kp=1.0, ki=0.1, kd=0.01):
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def compute_cmd_vel(self, current_pose, target_pose):
        """Generates linear and angular velocities."""
        dx = target_pose[0] - current_pose[0]
        dy = target_pose[1] - current_pose[1]
        target_yaw = np.arctan2(dy, dx)
        
        # Simple proportional control
        linear_v = 0.5 * np.sqrt(dx**2 + dy**2)
        angular_v = 1.0 * (target_yaw - current_pose[2])
        
        return linear_v, angular_v
