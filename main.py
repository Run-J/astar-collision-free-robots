from astar import a_star
import random


import matplotlib.pyplot as plt

grid_size = 10 # 网格图大小


# 随机生成机器人 1 的 起点 和 终点
# while True:
#     start1 = ( random.randint(0, 9), random.randint(0, 9) )
#     goal1 = ( random.randint(0, 9), random.randint(0, 9) )
#     if start1 != goal1: 
#         break

# 随机生成机器人 2 的 起点 和 终点
# while True:
#     start2 = ( random.randint(0, 9), random.randint(0, 9) )
#     goal2 = ( random.randint(0, 9), random.randint(0, 9) )
#     if start2 != goal2: 
#         break

# 指定起点终点
start1 = (1, 5)
goal1 = (9, 5)
start2 = (5, 1)
goal2 = (5, 9)



# 假路径（之后用 A* 来替换）
# path1 = [(0, 0), (0, 1), (1, 1), (2, 1), (3, 2), (4, 3)]
# path2 = [(9, 9), (8, 9), (8, 8), (7, 7), (6, 6), (5, 5)]


# A* 算过的路径
# 先让 Robot 1 规划路径
path1 = a_star(start1, goal1, grid_size)

# 构建 Robot1 的时间路径占用表
dynamic_obstacles = {t: pos for t, pos in enumerate(path1)}

# Robot 2 规划时，避开 Robot1 和 Robot 2 在同一帧同时会所在位置
path2 = a_star(start2, goal2, grid_size, dynamic_obstacles=dynamic_obstacles)
if not path2:
    print("Robot 2 找不到路径！")
    exit()




# 画一帧
def draw_frame(pos1, pos2, path1, path2, start1, goal1, start2, goal2, frame_idx):
    plt.clf()  # 清除上一次画面
    plt.title(f"Frame {frame_idx}")
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.grid(True)

    plt.xticks(range(0, grid_size + 1))  # X轴刻度：0 到 10（包含 10）
    plt.yticks(range(0, grid_size + 1))  # Y轴刻度：0 到 10（包含 10）


    # 标出起点和终点
    # Robot 1 起点终点
    plt.plot(start1[0], start1[1], marker='s', color='red', markersize=10, label='Start 1')
    plt.plot(goal1[0], goal1[1], marker='*', color='red', markersize=13, label='Goal 1')

    # Robot 2 起点终点
    plt.plot(start2[0], start2[1], marker='s', color='green', markersize=10, label='Start 2')
    plt.plot(goal2[0], goal2[1], marker='*', color='green', markersize=13, label='Goal 2')



    # 显示路径点
    # 路径（虚线）
    if path1:
        x1, y1 = zip(*path1)
        plt.plot(x1, y1, color='red', linewidth=2, linestyle='--', label='Path1')
    if path2:
        x2, y2 = zip(*path2)
        plt.plot(x2, y2, color='green', linewidth=2, linestyle='--', label='Path2')


    # 当前机器人位置（颜色与路径统一）
    plt.plot(pos1[0], pos1[1], marker='o', color='red', markersize=13, label='Robot 1')
    plt.plot(pos2[0], pos2[1], marker='o', color='green', markersize=13, label='Robot 2')

    plt.legend(loc='upper right', fontsize=8)
    plt.pause(0.5) # 暂停半秒显示这一帧



# 开启交互模式（允许动画刷新）
plt.ion()



# 逐帧移动机器人
for i in range(max(len(path1), len(path2))):
    pos1 = path1[i] if i < len(path1) else path1[-1] # 如果还没走完路径：就用第 i 步；如果路径走完了：就一直待在最后一个位置（path1[-1] 是终点）
    pos2 = path2[i] if i < len(path2) else path2[-1]
    draw_frame(pos1, pos2, path1, path2, start1, goal1, start2, goal2, i)


plt.ioff()
plt.show()