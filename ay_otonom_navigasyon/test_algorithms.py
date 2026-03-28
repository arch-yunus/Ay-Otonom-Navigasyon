import numpy as np
import sys
import os
sys.path.append(os.getcwd())
from ay_otonom_navigasyon.navigation import AStarPlanner

def test_astar_simple():
    """Verifies that the A* planner can find a straight path in a clear grid."""
    planner = AStarPlanner(grid_size=(10, 10))
    start = (0, 0)
    goal = (9, 9)
    
    path = planner.plan(start, goal)
    
    assert path is not False
    assert path[0] == (0, 1) or path[0] == (1, 0) or path[0] == (1, 1)
    assert path[-1] == goal
    print("A* Simple Path Test: PASSED")

def test_astar_with_obstacles():
    """Verifies that A* avoids high-cost areas (hazards)."""
    planner = AStarPlanner(grid_size=(10, 10))
    # Place a high-cost barrier
    planner.cost_map[5, 0:8] = 100 
    
    start = (0, 5)
    goal = (9, 5)
    
    path = planner.plan(start, goal)
    
    assert path is not False
    # Ensure no part of the path goes through the barrier
    for point in path:
        assert planner.cost_map[point] < 100
    print("A* Obstacle Avoidance Test: PASSED")

if __name__ == "__main__":
    test_astar_simple()
    test_astar_with_obstacles()
