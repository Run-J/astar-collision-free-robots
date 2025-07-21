# ===================== 主程序开始 Main Program =====================

from astar import a_star
import random
import matplotlib.pyplot as plt

grid_size = 10  # 网格大小 / grid size


# ---------------------- 设置机器人的起点终点以及路径 Set the robot's start point, end point and path ----------------------

# 随机生成机器人 1 的 起点 和 终点 / Uncomment the random start and end points of robot 1
# while True:
#     start1 = ( random.randint(0, 9), random.randint(0, 9) )
#     goal1 = ( random.randint(0, 9), random.randint(0, 9) )
#     if start1 != goal1: 
#         break

# 随机生成机器人 2 的 起点 和 终点 / Uncomment the random start and end points of robot 2
# while True:
#     start2 = ( random.randint(0, 9), random.randint(0, 9) )
#     goal2 = ( random.randint(0, 9), random.randint(0, 9) )
#     if start2 != goal2: 
#         break


# 手动指定起点终点 / Manually specify the start and end points
start1 = (1, 5)
goal1 = (9, 5)
start2 = (5, 1)
goal2 = (5, 9)



# # 取消注释手动模拟假路径 / Uncomment to manually simulate fake paths
# path1 = [(0, 0), (0, 1), (1, 1), (2, 1), (3, 2), (4, 3)]
# path2 = [(9, 9), (8, 9), (8, 8), (7, 7), (6, 6), (5, 5)]


# A* 算过的路径 / Paths calculated by A*
# Robot 1 先规划路径 / Robot 1 plans first
path1 = a_star(start1, goal1, grid_size)

# 构建 Robot1 的时间路径占用表；Robot 1 的路径用于动态避障 / used as dynamic obstacle for Robot 2
dynamic_obstacles = {t: pos for t, pos in enumerate(path1)}

# Robot 2 规划时，避开 Robot1 和 Robot 2 在同一帧同时会所在位置 以及 交换位置的情况
path2 = a_star(start2, goal2, grid_size, dynamic_obstacles=dynamic_obstacles)
if not path2:
    print("Robot 2 找不到路径！Robot 2 could not find a valid path.")
    exit()




# ---------------------- 画一帧帧动画 Draw one animation frame ----------------------

def draw_frame(pos1, pos2, path1, path2, start1, goal1, start2, goal2, frame_idx):
    plt.clf()  # 清除上一次画面 / Clear the last screen
    plt.title(f"Frame {frame_idx}")
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.grid(True)

    plt.xticks(range(0, grid_size + 1))  # X轴刻度：0 到 grid_size（包含 grid_size）/ X-axis scale: 0 to grid_size (inclusive)
    plt.yticks(range(0, grid_size + 1))  # Y轴刻度：0 到 grid_size（包含 grid_size）/ Y-axis scale: 0 to grid_size (inclusive)


    # 起点终点标记 / Start and goal markers
    # Robot 1 起点终点 / Robot 1 Start and End
    plt.plot(start1[0], start1[1], marker='s', color='red', markersize=10, label='Start 1')
    plt.plot(goal1[0], goal1[1], marker='*', color='red', markersize=13, label='Goal 1')

    # Robot 2 起点终点 / Robot 2 Start and End
    plt.plot(start2[0], start2[1], marker='s', color='green', markersize=10, label='Start 2')
    plt.plot(goal2[0], goal2[1], marker='*', color='green', markersize=13, label='Goal 2')



    # 显示路径点 / Display waypoints
    # 路径 / Paths
    if path1:
        x1, y1 = zip(*path1)
        plt.plot(x1, y1, color='red', linewidth=2, linestyle='--', label='Path1')
    if path2:
        x2, y2 = zip(*path2)
        plt.plot(x2, y2, color='green', linewidth=2, linestyle='--', label='Path2')


    # 当前机器人位置 / Current robot positions
    plt.plot(pos1[0], pos1[1], marker='o', color='red', markersize=13, label='Robot 1')
    plt.plot(pos2[0], pos2[1], marker='o', color='green', markersize=13, label='Robot 2')

    plt.legend(loc='upper right', fontsize=8)
    plt.pause(0.5) # 暂停片刻显示这一帧 / Pause for a moment and display this frame




# ---------------------- 动画播放 Animate all frames ----------------------

# 打开交互模式 / interactive mode on
plt.ion()



# 逐帧播放动画 / step through each frame
for i in range(max(len(path1), len(path2))):
    pos1 = path1[i] if i < len(path1) else path1[-1] # 如果还没走完路径：就用第 i 步；如果路径走完了：就一直待在最后一个位置（path1[-1] 是终点）
    pos2 = path2[i] if i < len(path2) else path2[-1]
    draw_frame(pos1, pos2, path1, path2, start1, goal1, start2, goal2, i)


plt.ioff()  # 关闭交互模式 / interactive mode off
plt.show()