import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# 中文显示设置（Windows 下用黑体）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

n_walks = 5        # 序列个数
n_steps = 300      # 每步走一次，共 300 步

rng = np.random.default_rng()          # 随机数生成器
# 每步等概率取 +1 或 -1，形状 (5, 300)
steps = rng.choice([-1, 1], size=(n_walks, n_steps))
# 从 0 开始累加，前面补一列 0，得到形状 (5, 301) 的游走序列
walks = np.concatenate(
    [np.zeros((n_walks, 1), dtype=int), np.cumsum(steps, axis=1)],
    axis=1
)

# 准备画布：5 个序列用不同颜色
fig, ax = plt.subplots(figsize=(9, 5))
colors = plt.cm.tab10(np.linspace(0, 1, n_walks))       # 取 5 种区分度高的颜色
lines = []
for i in range(n_walks):
    line, = ax.plot([], [], color=colors[i], lw=1.2, label=f'序列{i + 1}')
    lines.append(line)

ax.set_xlim(0, n_steps)
ax.set_ylim(walks.min() - 1, walks.max() + 1)
ax.set_xlabel('步数')
ax.set_ylabel('位置')
ax.set_title('5 个随机游走序列（每 100ms 走一步）')
ax.legend(loc='upper left', ncol=n_walks, fontsize=8)
ax.grid(alpha=0.3)

# 动态绘制：每 step 一次，暂停 0.1s 形成动画效果
plt.ion()                    # 打开交互模式
fig.show()
for t in range(1, n_steps + 1):
    for i in range(n_walks):
        lines[i].set_data(np.arange(t + 1), walks[i, :t + 1])
    plt.pause(0.1)           # 每 100ms 刷新一次

plt.ioff()
output_path = Path(__file__).resolve().parent / '随机游走.png'
plt.savefig(output_path, dpi=150)
plt.show()
