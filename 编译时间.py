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

    ax.legend(bbox_to_anchor=(0.5,1.1))

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
            texts.append(ax.text(i, v*2, '%.2f' % v, ha='center', va='center', rotation=90))

    # adjust_text(texts, add_objects=bars,
    #                 autoalign=False, only_move={'points':'y', 'text':'y', 'objects':'y'},
    #                 ha='center', va='bottom')
    
    # plt.rc('font', family='Times New Roman', size=12)
    # 紧凑布局
    plt.tight_layout()
    plt.yscale('log')
    plt.subplots_adjust(left=0.06, right=0.98, top=0.9, bottom=0.2)
    plt.savefig(graphName)

if __name__ == "__main__":
    plt.rcParams['font.family'] = 'Times New Roman'
    # 数据
    xlabel = ['LeNet','AlexNet','Bert_Tiny','DeepFM','MobileNet','ResNet18',
    'SqueezeNet', 'Wide&Deep','YOLO','Inception']

    dag_Compile_time = np.array([1.985,1342.435,89.832,4.191,173.702,511.657,86.342,0.650,2995.175,3.041,])
    global_compiler_time = np.array([2.011,1354.43,93.306,3.965,167.102,501.935,93.335,0.776,2950.247,3.144,])
    dagVLIW_Compiler_time = np.array([2.018,1366.827,91.100,4.294,175.791,520.089,88.118,0.667,3072.330,3.113,])
    

    
    drawGraph(xlabel, dag_Compile_time, global_compiler_time, dagVLIW_Compiler_time, '#de7a61', '#81b29d', '#f0c986',"DAG Compile Time", "Global Compile Time", "DAGVLIW Compile Time", "CompileTime.svg")
