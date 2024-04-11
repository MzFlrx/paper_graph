'''
Author: LiFangyi lifangyi01@qq.com
Date: 2024-04-04 07:16:48
LastEditors: LiFangyi lifangyi01@qq.com
LastEditTime: 2024-04-05 07:41:52
FilePath: /paperGraph/模型指令数量柱状图.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 十种模型拥有数量前十的指令数量

import numpy as np
import matplotlib.pyplot as plt

Op_color = [["phi","add","insertvalue","inttoptr","getelementptr",
             "load","mul","icmp","call","ptrtoint",
             "urem","sub","select","fcmp","extractvalue",
             "fadd","fmul","fsub","alloca","or",
             "lshr","shl","uitofp","fdiv","xor",
             "fptosi","fneg","fptrunc","bitcast","and",
             "sext","sitofp",],
            ["#cfd7b0","#7f694c","#e8c2db","#86605f","#a38fa3","#554e4e",
             "#52557b","#bbbcb9","#5b5e66","#b0886a","#a54b45","#f18772",
             "#fcefdf","#e1dba2","#cadabd","#af7680","#f1dadb","#c6cee2",
             "#7f8d7b","#d1bfac","#7d90a5","#ddd7d3","#cdb97d","#d8d1e1",
             "#efede9","#755953","#dcd2bd","#8a7b93","#cb9c7a","#dcd7d9",
             "#a59b95","#7a7579",]]

def readData(DataPath):
    """
        读取数据
    """
    retLabels = np.empty(0)
    retNums = np.empty(0, dtype=int)
    with open(DataPath, "r") as f:
        data = f.readline()
        while data:
            data = data.rstrip('\n')
            tmp = data.split('\t')
            retLabels = np.append(retLabels ,tmp[0])
            retNums = np.append(retNums, int(tmp[1]))
            data = f.readline()
    
    return retLabels, retNums

def getColor(Labels):
    """
        获取每个op的相同颜色
    """
    colors = np.empty(0)
    
    for i in range(len(Labels)):
        for j in range(len(Op_color[0])):
            if Labels[i] == Op_color[0][j]:
                colors = np.append(colors, Op_color[1][j])
                break
    return colors

def drawGraph(
    ChartFileName,
    DataPath,
    OutPutPath,
    Title,
    ax
):
    
    Labels, Nums = readData(DataPath)
    Labels = Labels[:10]
    Nums = Nums[:10]
    # Nums = int(Nums)
    colors = getColor(Labels)
    
    # xticks = np.arange(len(Labels))
    xticks = np.arange(len(Labels))
    # ax.set_yscale('log')
    ax.bar(xticks, Nums, color=colors, label=Labels)
    ax.set_xlabel('Opcode Name')
    ax.set_ylabel('Numbers')
    ax.set_xticks(np.arange(0,10,1))
    ax.set_xticklabels(Labels, rotation=90)
    ax.set_title(Title)

    handles, labels = ax.get_legend_handles_labels()
    
    return list(zip(handles, labels))


if __name__ == "__main__":
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.figure()
    fig , axs = plt.subplots(3,5, figsize=(16,10), gridspec_kw={'width_ratios': [1, 1, 1, 1, 1], 'height_ratios': [8, 8, 1]})
    plt.yscale('log')

    LeNetPath = "/root/project/paperGraph/OpNumDir/AlexNetOpNum.txt"
    color_legen1 = drawGraph("LeNet.svg", LeNetPath, "./GraphDir", "LeNet OpNum COUNT", axs[0,0])
    
    AlexNetPath = "/root/project/paperGraph/OpNumDir/AlexNetOpNum.txt"
    color_legen2 = drawGraph("AlexNet.svg", AlexNetPath, "./GraphDir", "AlexNet OpNum COUNT", axs[0,1])
    
    Bert_TinyPath = "/root/project/paperGraph/OpNumDir/Bert_TinyOpNum.txt"
    color_legen3 = drawGraph("Bert_Tiny.svg", Bert_TinyPath, "./GraphDir", "Bert_Tiny OpNum COUNT", axs[0,2])
    
    DeepFMPath = "/root/project/paperGraph/OpNumDir/DeepFMOpNum.txt"
    color_legen4 = drawGraph("DeepFM.svg", DeepFMPath, "./GraphDir", "DeepFM OpNum COUNT", axs[0,3])
    
    MobileNetPath = "/root/project/paperGraph/OpNumDir/MobileNetOpNum.txt"
    color_legen5 = drawGraph("MobileNet.svg", MobileNetPath, "./GraphDir", "MobileNet OpNum COUNT", axs[0,4])
    
    ResNet18Path = "/root/project/paperGraph/OpNumDir/ResNet18OpNum.txt"
    color_legen6 = drawGraph("ResNet18.svg", ResNet18Path, "./GraphDir", "ResNet18 OpNum COUNT", axs[1,0])
    
    SqueezeNetPath = "/root/project/paperGraph/OpNumDir/SqueezeNetOpNum.txt"
    color_legen7 = drawGraph("SqueezeNet.svg", SqueezeNetPath, "./GraphDir", "SqueezeNet OpNum COUNT", axs[1,1])
    
    Wide_DeepPath = "/root/project/paperGraph/OpNumDir/Wide&DeepOpNum.txt"
    color_legen8 = drawGraph("Wide_Deep.svg", Wide_DeepPath, "./GraphDir", "Wide&Deep OpNum COUNT", axs[1,2])
    
    YOLOPath = "/root/project/paperGraph/OpNumDir/YOLOOpNum.txt"
    color_legen9 = drawGraph("YOLO.svg", YOLOPath, "./GraphDir", "YOLO OpNum COUNT", axs[1,3])
    
    InceptionPath = "/root/project/paperGraph/OpNumDir/InceptionOpNum.txt"
    color_legen10 = drawGraph("Inception.svg", InceptionPath, "./GraphDir", "Inception OpNum COUNT", axs[1,4])

    # 提炼所有颜色
    all_colors = set(color_legen1+color_legen2+color_legen3+color_legen4+color_legen5+color_legen6+color_legen7+color_legen8+color_legen9+color_legen10)
    all_colors = {color[1]: color for color in all_colors}.values()
    unique_labels = []
    unique_wedget = []
    for color in all_colors:
        if color[1] not in unique_labels and color[1] != '1':
            unique_labels.append(color[1])
            unique_wedget.append(color[0])


    for i in range(5):
        axs[2,i].axis("off")

    axs[2,2].legend(unique_wedget, unique_labels, loc='upper center', ncol=13)
    plt.subplots_adjust(left=0.05, right=0.97, top=0.95, bottom=0.03)
    plt.subplots_adjust(hspace=0.6, wspace=0.3)
    plt.tight_layout()
    plt.savefig("十种模型前十指令柱状图.svg")