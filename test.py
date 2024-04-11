import matplotlib.pyplot as plt
# 定义数据
sizes_A = [1, 1, 1]
sizes_B = [1, 1, 1, 1]  # 与 sizes_A 长度相同
labels = ['D', 'E', 'F', 'G']
colors = ['red', 'blue', 'green', 'yellow']
# 绘制饼图 A
fig, ax = plt.subplots()
ax.pie(sizes_A, labels=labels[:3], colors=colors[:3], autopct='%1.1f%%', startangle=90)
ax.set_title('Pie Chart A')
# 绘制饼图 B
fig, ax = plt.subplots()
ax.pie(sizes_B, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.set_title('Pie Chart B')
# 创建图例
legend_patches = [plt.Line2D([0], [0], marker='o', color='w', markersize=10, markerfacecolor=color, label=label) 
                  for color, label in zip(colors, labels)]
plt.legend(handles=legend_patches)
# 显示图形
plt.show()
plt.savefig("test.svg")