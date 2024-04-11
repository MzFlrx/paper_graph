'''
Author: LiFangyi lifangyi01@qq.com
Date: 2024-04-03 04:06:12
LastEditors: LiFangyi lifangyi01@qq.com
LastEditTime: 2024-04-03 04:10:02
FilePath: /paperGraph/ReferenceCode/complex.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import matplotlib.pyplot as plt
import numpy as np

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10] # 各部分占比
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

fig, ax = plt.subplots()

# 绘制饼图
wedges, texts, autotexts = ax.pie(sizes, colors=colors, autopct='%1.1f%%',
                                  startangle=90)

# 调整位置和大小
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

# 添加标题
ax.set_title("External Labels")

plt.show()
plt.savefig("complex.svg")