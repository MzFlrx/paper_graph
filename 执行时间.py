'''
Author: LiFangyi lifangyi01@qq.com
Date: 2024-04-05 11:47:11
LastEditors: LiFangyi lifangyi01@qq.com
LastEditTime: 2024-04-05 14:13:31
FilePath: /paperGraph/执行时间.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# credit: Li Fangyi
# 编译时间、执行时间、代码体积对比图

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
    plt.rcParams['font.family'] = 'Times New Roman'
    # 画布大小
    fig, ax = plt.subplots(figsize=(10, 3.9))
    xticks = np.arange(len(xlabel))


    bars = []

    bars.append(ax.bar(xticks, dataA, color=colorA, label=labelA, width=0.25, hatch='///'))

    # ax.bar(xlabel, global_dag_O0_exec_time_rate, color='blue', label="global vs. dag exec time")

    bars.append(ax.bar(xticks+0.25, dataB, color=colorB, label=labelB, width=0.25, hatch='...'))

    # ax.bar(xlabel, dagVLIW_dag_O0_exec_time_rate, color='purple', label="dagVLIW vs. dag exec time")
    bars.append(ax.bar(xticks+0.5, dataC, color=colorC, label=labelC, width=0.25, hatch='---'))

    ax.set_xlabel('Model Name')

    ax.set_ylabel('times (s)')

    ax.legend(bbox_to_anchor=(0.5,0.95))

    ax.set_xticks(xticks+0.25/2)
    ax.set_xticklabels(xlabel)
    # 坐标轴倾斜
    plt.xticks(rotation=20)
    # y轴范围
    # plt.ylim(ylim[0],ylim[1])

    # plt.axhline(y=1, color='black', linewidth=1)
    texts = []
    # 显示数据
    for y in dataA, dataB, dataC:
        for i, v in zip(xticks, y):
            if (y == dataB).all():
                i += 0.25
            elif (y == dataC).all():
                i += 0.5
            texts.append(ax.text(i, v+2400, '%.4f' % v, ha='center', va='center', rotation=90))

    # adjust_text(texts, add_objects=bars,
    #                 autoalign=False, only_move={'points':'y', 'text':'y', 'objects':'y'},
    #                 ha='center', va='bottom')
    
    # plt.rc('font', family='Times New Roman', size=12)
    # 紧凑布局
    plt.tight_layout()
    # plt.yscale('log')
    plt.savefig(graphName)

if __name__ == "__main__":
    plt.rcParams['font.family'] = 'Times New Roman'
    # 数据
    xlabel = ['LeNet','AlexNet','Bert_Tiny','DeepFM','MobileNet','ResNet18',
    'SqueezeNet', 'Wide&Deep','YOLO','Inception']

    dag_exec_time = np.array([0.253069,275.486077,454.261457,0.805152,95.637521,706.891517,142.16419,0.007814,14981.793668,2.301068,])
    global_exec_time = np.array([0.285462,293.3927,445.6305,0.768115,94.77678,747.8912,137.7571,0.007244,14802.01,2.448336,])
    dagVLIW_exec_time = np.array([0.222,246.525,414.929,0.717,81.762,629.414,119.172,0.0078,13775.654,2.016,])    
    
    drawGraph(xlabel, dag_exec_time, global_exec_time, dagVLIW_exec_time, '#de7a61', '#81b29d', '#f0c986',"DAG exec Time", "Global exec Time", "DAGVLIW exec Time", "ExecTime.svg")
