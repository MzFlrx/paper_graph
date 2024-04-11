import matplotlib.pyplot as plt

# 准备数据
sizes = [15, 30, 45, 10]  # 数据总和为 100

# 设置阈值
threshold = 10

# 对数据进行处理，将小于阈值的部分的标签设为 ''，并将 autopct 参数设为 None
labels = ['A', 'B', 'C', 'D']
for i, size in enumerate(sizes):
    if size < threshold:
        labels[i] = ''
        
# 绘制饼图，autopct 参数设为 None
plt.pie(sizes, labels=labels, autopct=None, startangle=90)

# 显示图例
plt.legend()

# 显示图形
plt.show()
plt.savefig("test2.svg")