'''
Author: LiFangyi lifangyi01@qq.com
Date: 2024-04-05 09:58:06
LastEditors: LiFangyi lifangyi01@qq.com
LastEditTime: 2024-04-07 03:11:34
FilePath: /paperGraph/代码体积.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# credit: Li Fangyi
# 编译时间、执行时间、代码体积对比图

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
from adjustText import adjust_text 
import math
def drawGraph(
    xlabel,
    dataSet,
    colorSet,
    labelSet,
    hatchSet,
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
    plt.rc('font',family='Times New Roman')
    xticks = np.arange(len(xlabel))


    bars = []
    
    for i in range(len(dataSet)):
        bars.append(ax.bar(xticks+i*0.2-0.2, dataSet[i], color=colorSet[i], label=labelSet[i], width=0.2, hatch=hatchSet[i]))

    ax.set_xlabel('Model Name')

    ax.set_ylabel('Code Size (B)')

    ax.legend(bbox_to_anchor=(0.2,0.95))

    ax.set_xticks(xticks+0.25/2)
    ax.set_xticklabels(xlabel)
    # 坐标轴倾斜
    plt.xticks(rotation=20)
    # y轴范围
    # plt.ylim(ylim[0],ylim[1])

    # plt.axhline(y=1, color='black', linewidth=1)
    texts = []
    # 显示数据
    for y in dataSet:
        for i, v in zip(xticks, y):
            if (y == dataSet[0]).all():
                i -= 0.2
            elif (y == dataSet[1]).all():
                pass
            elif (y == dataSet[2]).all():
                i += 0.2
            elif (y == dataSet[3]).all():
                i += 0.4
            texts.append(ax.text(i, v*2-20000, '%d' % v, ha='center', va='center', rotation=90))

    # adjust_text(texts, add_objects=bars,
    #                 autoalign=False, only_move={'points':'y', 'text':'y', 'objects':'y'},
    #                 ha='center', va='bottom')
    
    # plt.rc('font', family='Times New Roman', size=12)
    # 紧凑布局
    plt.tight_layout()
    plt.yscale('log')
    plt.subplots_adjust(left=0.07, right=0.98, top=0.8, bottom=0.2)
    plt.savefig(graphName)

if __name__ == "__main__":
    
    # 数据
    xlabel = ['LeNet','AlexNet','Bert_Tiny','DeepFM','MobileNet','ResNet18',
    'SqueezeNet', 'Wide&Deep','YOLO','Inception']

    LLVMIR_Code_Size = np.array([87020,138117,520955,1077253,2171575,332797,425683,144835,1716321,229524,])
    dag_Code_Size = np.array([89035,151556,645365,1456907,1408643,441226,589085,112715,2761809,253841,])
    global_Code_Size = np.array([88037,146492,633422,1449877,1406715,438356,585055,112359,2754777,251614,])
    dagVLIW_Code_Size = np.array([113964,186668,849855,1670212,1714431,533199,755265,133225,3361425,318898,])
    
    dataSet = [LLVMIR_Code_Size, dag_Code_Size, global_Code_Size, dagVLIW_Code_Size]
    
    colorSet = ['#556293','#de7a61', '#81b29d', '#f0c986']
    
    labelSet = ['LLVMIR', 'dag', 'global', 'dagVLIW']
    
    hatchSet = ['xxx','///','...','---']
    
    drawGraph(xlabel, dataSet, colorSet, labelSet, hatchSet, "CodeSize.svg")
