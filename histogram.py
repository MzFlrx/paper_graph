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
    colorA,
    colorB,
    labelA,
    labelB,
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
            
                texts.append(ax.text(i, v+0.02, '%.4f' % v, ha='center', va='center' , rotation=90))
            else:
                texts.append(ax.text(i, v+0.02, '%.4f' % v, ha='center', va='center' , rotation=90))

    # adjust_text(texts, add_objects=bars,
    #                 autoalign=False, only_move={'points':'y', 'text':'y', 'objects':'y'},
    #                 ha='center', va='bottom')
    
    # plt.rc('font', family='Times New Roman', size=12)
    # 紧凑布局
    plt.tight_layout()
    plt.savefig(graphName)

if __name__ == "__main__":
    
    # 数据
    xlabel = ['LeNet','AlexNet','Bert_Tiny','DeepFM','MobileNet','ResNet18',
    'SqueezeNet', 'Wide&Deep','YOLO','Inception','average']

    dag_O0_compile_time = np.array([1.985, 1342.435, 89.832, 4.191, 173.702, 511.657,
                        86.342, 0.650, 2995.175, 3.041,] )

    dag_O0_exec_time = np.array([0.253069, 275.486077, 454.261457, 0.805152, 95.637521,
                        706.891517, 142.16419, 0.007814, 14981.793668, 2.301068,])

    global_O0_exec_time = np.array([0.285462, 293.3927, 445.6305, 0.768115, 94.77678, 
                        747.8912, 137.7571, 0.007244, 14802.01, 2.448336,])

    global_O0_compile_time = np.array([2.011, 1354.43, 93.306, 3.965, 167.102, 501.935,
                            93.335, 0.776, 2,950.247, 3.144,] )

    dag_O0_VILW_compile_time = np.array([2.018, 1366.827, 91.100, 4.294, 175.791, 520.089, 
                            88.118, 0.667, 3072.330, 3.113,])

    dag_O0_VILW_exec_time = np.array([0.222, 246.525, 414.929, 0.717, 81.762, 629.414,
                            119.172, 0.0078, 13775.654, 2.016])

    global_dag_O0_compile_time_rate = np.array([1.013, 1.009, 1.038, 0.946, 0.962, 0.981, 1.081,
                                    1.187, 0.985, 1.034,])
    # 添加均值
    global_dag_O0_compile_time_rate = np.append(global_dag_O0_compile_time_rate, np.average(global_dag_O0_compile_time_rate))

    global_dag_O0_exec_time_rate = np.array([1.128, 1.065, 0.981, 0.954, 0.991, 1.058, 0.969, 
                                0.927, 0.988, 1.064,])
    # 添加均值
    global_dag_O0_exec_time_rate = np.append(global_dag_O0_exec_time_rate, np.average(global_dag_O0_exec_time_rate))
    # globalVLIW_dag_O0_compile_time_rate = 

    dagVLIW_dag_O0_compile_time_rate = dag_O0_compile_time/dag_O0_VILW_compile_time
    dagVLIW_dag_O0_compile_time_rate = np.append(dagVLIW_dag_O0_compile_time_rate, np.average(dagVLIW_dag_O0_compile_time_rate))

    dagVLIW_dag_O0_exec_time_rate = dag_O0_exec_time/dag_O0_VILW_exec_time
    dagVLIW_dag_O0_exec_time_rate = np.append(dagVLIW_dag_O0_exec_time_rate, np.average(dagVLIW_dag_O0_exec_time_rate))

    colorA = (254/255, 212/255, 152/255)
    colorB = (158/255, 148/255, 182/255)
    
    # 画图
    # 编译时间
    drawGraph(xlabel, global_dag_O0_compile_time_rate, dagVLIW_dag_O0_compile_time_rate, colorA, colorB, "global vs. dag compile time", "dagVLIW vs. dag compile time", 'compile_time_rate.svg')
    # 执行时间
    drawGraph(xlabel, global_dag_O0_exec_time_rate, dagVLIW_dag_O0_exec_time_rate, colorA, colorB,"global vs. dag exec time", "dagVLIW vs. dag exec time", 'exec_time_rate.svg')
    
    dag_O0_code_size = np.array([89035,151556,645365,1456907,1408643,441226,589085,112715,2761809,253841,])
    global_O0_code_size = np.array([88037, 146492, 633422, 1449877, 1406715, 
                                    438356, 585055, 112359, 2754777, 251614,])
    dagVLIW_O0_code_size = np.array([113964, 186668, 849855, 1670212, 1714431,
                                     533199, 755265, 133225, 3361425, 318898,])
    
    global_dag_O0_code_size_rate = dag_O0_code_size/global_O0_code_size
    global_dag_O0_code_size_rate = np.append(global_dag_O0_code_size_rate, np.average(global_dag_O0_code_size_rate))
    
    dagVLIW_dag_O0_code_size_rate = dag_O0_code_size/dagVLIW_O0_code_size
    dagVLIW_dag_O0_code_size_rate = np.append(dagVLIW_dag_O0_code_size_rate, np.average(dagVLIW_dag_O0_code_size_rate))
    # 代码体积
    drawGraph(xlabel, global_dag_O0_code_size_rate, dagVLIW_dag_O0_code_size_rate, colorA, colorB, "global vs. dag code size", "dagVLIW vs. dag code size", 'code_size_rate.svg', ylim=(0.7, 1.1))
