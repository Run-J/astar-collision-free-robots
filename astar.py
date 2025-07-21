import heapq

# 定义机器人可以走的四个方向（上下左右）
# Define 4 movement directions: up, down, left, right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(a, b):
    """估价函数：A* 中的 h(n)，这里用曼哈顿距离
    Heuristic function: Manhattan distance as h(n)
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal, grid_size=10, obstacles=None, dynamic_obstacles=None):
    """
    A* 搜索算法，用于从起点到终点规划路径
    A* pathfinding algorithm from start to goal

    Parameters:
        start: 起点坐标 (x, y) / start position
        goal: 终点坐标 (x, y) / goal position
        grid_size: 网格大小 / size of grid (default: 10x10)
        obstacles: 静态障碍集合 / static obstacles (set)
        dynamic_obstacles: 动态障碍时间表 / time-dependent dynamic obstacles
    Returns:
        路径列表 list of path positions [(x1, y1), (x2, y2), ...]
    """

    if obstacles is None:
        obstacles = set()

    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start))  # (f, g, position)

    came_from = {}           # 路径回溯用 / for path reconstruction
    g_score = {start: 0}     # 起点到每个点的代价 / cost from start to this point

    while open_set:
        _, current_g, current = heapq.heappop(open_set)
        t = current_g + 1  # 当前时间帧 + 1 / next time frame

        if current == goal:
            # 回溯重建路径 / reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        for dx, dy in moves:
            neighbor = (current[0] + dx, current[1] + dy)

            # 越界检查 / boundary check
            if not (0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size):
                continue
            # 静态障碍 / static obstacles
            if neighbor in obstacles:
                continue
            # 动态障碍 / dynamic collision check
            if dynamic_obstacles:
                # 避免在同一帧和另一个机器人撞到同一个格子
                if t in dynamic_obstacles and neighbor == dynamic_obstacles[t]:
                    continue
                # 避免面对面交换位置（head-on swap）
                if t in dynamic_obstacles and t-1 in dynamic_obstacles:
                    if neighbor == dynamic_obstacles[t-1] and current == dynamic_obstacles[t]:
                        continue

            tentative_g = current_g + 1  # 每一步代价为1 / cost of step

            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, tentative_g, neighbor))

    return []  # 无法到达目标 / no path found