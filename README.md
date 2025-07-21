# 🤖 双/多机器人路径规划仿真 / Dual/Multi Robot Path Planning Simulation

一个基于 Python 的机器人路径仿真项目，模拟两个机器人在 10x10 网格中使用 A* 算法避开静态和动态障碍进行路径规划，确保无碰撞、安全抵达。

A Python simulation for **dual-robot path planning** using the A* algorithm on a 10x10 grid. It handles both **static** and **dynamic collision avoidance**, ensuring safe arrival of both agents.

---

## 🎥 Demo 展示 / Demo

下列测试场景展示了本项目支持的典型路径规划场景和动态避障能力：

The following test scenarios demonstrate typical planning and collision-avoidance capabilities of this project:

| 场景 / Scenario | 描述 / Description | 动图 / Demo |
|----------------|--------------------|-------------|
| 🟥 正面相遇（对冲）<br>**Head-on Conflict** | 两个机器人起点和终点完全相同，测试动态避障和冲突处理。<br>Robots start and end at the same position, testing head-on conflict avoidance. | ![Image](https://github.com/user-attachments/assets/ff61d969-8764-4c17-b183-dfc8b26523db) |
| 🟩 交叉路径<br>**Cross Paths** | 两条路径在中点交叉，测试时序避让机制。<br>Paths cross at center; validates time-based separation. | ![Image](https://github.com/user-attachments/assets/47643c80-d3f7-4858-910c-b19987ac8a35) |
| 🟦 一前一后<br>**One Following Another** | Robot 2 紧跟 Robot 1 后方，测试“跟车”避障。<br>Robot 2 follows Robot 1; tests trailing safety. | ![Image](https://github.com/user-attachments/assets/64e33f4b-dde9-43a4-992f-05410a3003b3) |
| 🟪 绕过障碍<br>**Obstacle Avoidance** | 地图中包含静态障碍，测试绕行能力。<br>Static obstacles added; tests replanning and detour logic. | ![Image](https://github.com/user-attachments/assets/3b428328-c562-45ba-95bb-f196e9774d70) |

---

## 🔧 技术实现 / Technical Highlights

### ✅ 核心算法 / Core Algorithm

- A* 路径规划算法（启发式使用曼哈顿距离）  
  A* pathfinding algorithm with a Manhattan distance heuristic

- 每个机器人独立规划路径，Robot 2 需考虑 Robot 1 的动态路径占用  
  Each robot plans its path independently; Robot 2 treats Robot 1’s path as dynamic path occupancy (time-dependent obstacles)

- 避免以下两类冲突 / Avoids the following types of conflicts:  
  - **同位置冲突（Position Conflict）**：两个机器人在同一帧占据同一格  
    **Position Conflict** – both robots occupy the same cell at the same timestep  
  - **换位冲突（Head-on Swap）**：机器人在连续帧中互换位置  
    **Head-on Swap** – robots swap positions between two consecutive timesteps

---

### 📊 可视化仿真 / Visualization

- 使用 `matplotlib` 动态绘制网格动画  
  Animated grid simulation using `matplotlib`

- 每一帧动态更新机器人位置与路径轨迹  
  Each frame updates robot positions and traversed paths

- 支持如下可视元素 / Visual elements supported:  
  - ✅ 静态障碍（可手动/随机设置）  
    ✅ Static obstacles (manually or randomly generated)  
  - ✅ 动态冲突检测与避让  
    ✅ Dynamic collision detection and avoidance  
  - ✅ 不同颜色、起点/终点标识、路径虚线展示  
    ✅ Distinct colors, markers for start/goal, and dashed path visualization

---

## ⚙️ 功能亮点 / Key Features

- ✅ 支持两个机器人无碰撞路径规划  
  ✅ Supports collision-free path planning for two robots

- ✅ A* 搜索结合时间维度冲突检测  
  ✅ A* search extended with temporal conflict checking

- ✅ 可自定义机器人起点、终点与障碍配置  
  ✅ Fully customizable start/end points and obstacles

- ✅ 每一步帧动画展示运动过程，便于观察路径策略  
  ✅ Frame-by-frame animation to visualize motion strategy

- ✅ 适合研究双智能体规划、多智能体避障演示  
  ✅ Ideal for dual-agent pathfinding and multi-agent planning education/demo

---

## 📁 项目结构 / Project Structure
```
astar-collision-free-robots/
│
├── main.py              # 主程序（动画 + 可视化） / Main program (animation + visualization)
├── astar.py             # A* 算法实现，含动态避障逻辑 / A* algorithm implementation, including dynamic obstacle avoidance logic
└── README.md            # 项目说明 / Project documentation
```
