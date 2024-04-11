'''
Author: LiFangyi lifangyi01@qq.com
Date: 2024-04-05 07:52:31
LastEditors: LiFangyi lifangyi01@qq.com
LastEditTime: 2024-04-05 07:53:23
FilePath: /paperGraph/IR代码与汇编代码体积对比.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
from adjustText import adjust_text 

def drawGraph(
    xlabel,
    dataA,
    dataB,
    dataC,
    colorA,
    colorB,
    colorC,
    labelA,
    labelB,
    labelC,
    graphName,
    ylim = (0.8, 1.2)
):
    """
        xlabel: x轴标签
        dataA: 数据A
        dataB: 数据B
        colorA: 数据A颜色
        colorB: 数据B颜色
        labelA: 数据A图例名字
        labelB: 数据B图例名字
        graphName: 图片名称
    """
    # 画布大小
    fig, ax = plt.subplots(figsize=(10, 6.18))
    plt.rc('font',family='Times New Roman')
    xticks = np.arange(len(xlabel))


    bars = []

    bars.append(ax.bar(xticks, dataA, color=colorA, label=labelA, width=0.25, hatch='///'))

    # ax.bar(xlabel, global_dag_O0_exec_time_rate, color='blue', label="global vs. dag exec time")

    bars.append(ax.bar(xticks+0.25, dataB, color=colorB, label=labelB, width=0.25, hatch='...'))

    # ax.bar(xlabel, dagVLIW_dag_O0_exec_time_rate, color='purple', label="dagVLIW vs. dag exec time")

    ax.set_xlabel('Model Name')

    ax.set_ylabel('Ratio')

    ax.legend()

    ax.set_xticks(xticks+0.25/2)
    ax.set_xticklabels(xlabel)
    # 坐标轴倾斜
    plt.xticks(rotation=20)
    # y轴范围
    plt.ylim(ylim[0],ylim[1])

    plt.axhline(y=1, color='black', linewidth=1)
    texts = []
    # 显示数据
    for y in dataA, dataB:
        for i, v in zip(xticks, y):
            if (y == dataB).all():
                i += 0.25
            
                texts.append(ax.text(i, v+0.01, '%.4f' % v, ha='center', va='center', color=colorB))
            else:
                texts.append(ax.text(i, v+0.01, '%.4f' % v, ha='center', va='center', color = colorA))

    adjust_text(texts, add_objects=bars,
                    autoalign=False, only_move={'points':'y', 'text':'y', 'objects':'y'},
                    ha='center', va='bottom')
    
    # plt.rc('font', family='Times New Roman', size=12)
    # 紧凑布局
    plt.tight_layout()
    plt.savefig(graphName)
    
if __name__ == "__main__":
    