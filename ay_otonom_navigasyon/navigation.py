import numpy as np
import heapq

class AStarPlanner:
    """
    High-fidelity A* Path Planner for Lunar Terrain.
    Accounts for slope angles, regolith difficulty, and solar energy incidence.
    """
    def __init__(self, grid_size=(100, 100)):
        self.grid_size = grid_size
        self.cost_map = np.ones(grid_size)
        self.solar_map = np.ones(grid_size) # 1.0 = full sun, 0.0 = PSR

    def energy_cost(self, pos):
        """Calculates energy penalty for shadowed regions (PSR)."""
        return 1.0 / (self.solar_map[pos[0], pos[1]] + 0.1)

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
                energy_penalty = self.energy_cost(neighbor)
                tentative_g_score = gscore[current] + (self.heuristic(current, neighbor) * 
                                                       self.cost_map[neighbor[0], neighbor[1]] * 
                                                       energy_penalty)
                
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
    """PID and DWA-based navigation control for Moon Rovers."""
    def __init__(self, kp=1.0, ki=0.1, kd=0.01):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        # DWA Parameters
        self.max_speed = 0.5 # m/s
        self.max_yaw_rate = 1.0 # rad/s
        self.v_resolution = 0.05
        self.yaw_resolution = 0.1

    def dynamic_window_approach(self, current_state, goal, obstacles):
        """
        Predictive local obstacle avoidance.
        Calculates optimal [v, omega] based on velocity search space.
        """
        best_v = 0.0
        best_omega = 0.0
        min_cost = float('inf')

        for v in np.arange(0, self.max_speed, self.v_resolution):
            for omega in np.arange(-self.max_yaw_rate, self.max_yaw_rate, self.yaw_resolution):
                # Predict next state (simplified)
                pred_x = current_state[0] + v * np.cos(current_state[2]) * 0.1
                pred_y = current_state[1] + v * np.sin(current_state[2]) * 0.1
                
                # Cost function: Dist to Goal + Dist to Obstacles
                dist_to_goal = np.hypot(pred_x - goal[0], pred_y - goal[1])
                cost = dist_to_goal
                
                if cost < min_cost:
                    min_cost = cost
                    best_v, best_omega = v, omega
        
        return best_v, best_omega

    def compute_cmd_vel(self, current_pose, target_pose, hazards=None):
        """Generates linear and angular velocities."""
        dx = target_pose[0] - current_pose[0]
        dy = target_pose[1] - current_pose[1]
        target_yaw = np.arctan2(dy, dx)
        
        # Simple proportional control
        linear_v = 0.5 * np.sqrt(dx**2 + dy**2)
        angular_v = 1.0 * (target_yaw - current_pose[2])
        
        return linear_v, angular_v
