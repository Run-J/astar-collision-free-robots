import heapq

# 定义机器人可以走的四个方向（上下左右）
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(a, b):
    """估价函数（曼哈顿距离）：A* 中的 h(n)"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal, grid_size=10, obstacles=None, dynamic_obstacles=None):
    """
    使用 A* 算法从 start 到 goal 搜索路径
    :param start: 起点坐标 (x, y)
    :param goal: 终点坐标 (x, y)
    :param grid_size: 网格大小（默认10x10）
    :param obstacles: 障碍物坐标集合（可选）
    :return: 路径列表 [(x1, y1), (x2, y2), ...]
    """

    if obstacles is None:
        obstacles = set()

    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))  # (f, g, position)

    came_from = {}           # 用于回溯路径：child → parent
    g_score = {start: 0}     # 起点到某点的代价

    while open_set:
        _, current_g, current = heapq.heappop(open_set)
        t = current_g + 1 # 下一步的时间点（帧数）

        if current == goal:
            # 找到终点，回溯路径
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        for dx, dy in moves:
            neighbor = (current[0] + dx, current[1] + dy)

            # 检查边界 & 障碍物 & 和 Path 1 在相同帧的位置
            if not (0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size):
                continue
            # 固定避让其它障碍
            if neighbor in obstacles:
                continue
            # 动态障碍（同位置 + 换位冲突）
            if dynamic_obstacles:
                # 同一位置冲突
                if t in dynamic_obstacles and neighbor == dynamic_obstacles[t]:
                    continue
                # 面对面冲突
                if t in dynamic_obstacles and t-1 in dynamic_obstacles:
                    if neighbor == dynamic_obstacles[t-1] and current == dynamic_obstacles[t]:
                        continue


            tentative_g = current_g + 1  # 假设每一步代价都是1

            if tentative_g < g_score.get(neighbor, float('inf')):
                # 如果到 neighbor 的新路径更短，就更新它
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, tentative_g, neighbor))

    # 没有找到路径
    return []