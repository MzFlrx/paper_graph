# create by Lifangyi

import matplotlib.pyplot as plt
import numpy as np

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
    retLabels = np.array(1)
    retNums = np.array(1)
    with open(DataPath, "r") as f:
        data = f.readline()
        while data:
            data.strip()
            tmp = data.split('\t')
            retLabels = np.append(retLabels ,tmp[0])
            retNums = np.append(retNums, tmp[1])
            data = f.readline()
    
    return retLabels, retNums

def getColor(Labels):
    """
        获取每个op的相同颜色
    """
    colors = np.array(1)
    
    for i in range(len(Labels)):
        for j in range(len(Op_color[0])):
            if Labels[i] == Op_color[0][j]:
                colors = np.append(colors, Op_color[1][j])
                break
    return colors

def PieChart(
    ChartFileName, # 图名字
    DataPath, # 数据文件路径
    OutPutPath, # 输出图片路径
    Title, # 图标题
    ax
):
    Labels, Nums = readData(DataPath)
    
    colors = getColor(Labels)
    # for i in range(len(Labels)):
    #     Labels[i] = Labels[i]+ ":" + Nums[i]
    
    # fig, ax = plt.subplots()
    plt.rc('font',family='Times New Roman')
    # wedges, texts, autotexts = ax.pie(Nums, labels=Labels, colors=colors, autopct='%1.1f%%')
    patches, text, autotexts = ax.pie(Nums, labels=Labels, colors=colors, autopct='%1.1f%%')
    
    # fig.suptitle(Title)
    ax.set_title(Title,)
    
    
    handles, labels = ax.get_legend_handles_labels()
    
    return list(zip(handles, labels))
    
    

if __name__ == "__main__":
    plt.rcParams['font.family'] = 'Times New Roman'
    # figsize=(10, 6.18)
    plt.figure()
    fig , axs = plt.subplots(3,5, figsize=(17.5,7.02), gridspec_kw={'width_ratios': [1, 1, 1, 1, 1], 'height_ratios': [8, 8, 1]})
    
    
    LeNetPath = "/root/project/paperGraph/OpNumDir/AlexNetOpNum.txt"
    color_legen1 = PieChart("LeNet.svg", LeNetPath, "./GraphDir", "LeNet OpNum Distribution", axs[0,0])
    
    AlexNetPath = "/root/project/paperGraph/OpNumDir/AlexNetOpNum.txt"
    color_legen2 = PieChart("AlexNet.svg", AlexNetPath, "./GraphDir", "AlexNet OpNum Distribution", axs[0,1])
    
    Bert_TinyPath = "/root/project/paperGraph/OpNumDir/Bert_TinyOpNum.txt"
    color_legen3 = PieChart("Bert_Tiny.svg", Bert_TinyPath, "./GraphDir", "Bert_Tiny OpNum Distribution", axs[0,2])
    
    DeepFMPath = "/root/project/paperGraph/OpNumDir/DeepFMOpNum.txt"
    color_legen4 = PieChart("DeepFM.svg", DeepFMPath, "./GraphDir", "DeepFM OpNum Distribution", axs[0,3])
    
    MobileNetPath = "/root/project/paperGraph/OpNumDir/MobileNetOpNum.txt"
    color_legen5 = PieChart("MobileNet.svg", MobileNetPath, "./GraphDir", "MobileNet OpNum Distribution", axs[0,4])
    
    ResNet18Path = "/root/project/paperGraph/OpNumDir/ResNet18OpNum.txt"
    color_legen6 = PieChart("ResNet18.svg", ResNet18Path, "./GraphDir", "ResNet18 OpNum Distribution", axs[1,0])
    
    SqueezeNetPath = "/root/project/paperGraph/OpNumDir/SqueezeNetOpNum.txt"
    color_legen7 = PieChart("SqueezeNet.svg", SqueezeNetPath, "./GraphDir", "SqueezeNet OpNum Distribution", axs[1,1])
    
    Wide_DeepPath = "/root/project/paperGraph/OpNumDir/Wide&DeepOpNum.txt"
    color_legen8 = PieChart("Wide_Deep.svg", Wide_DeepPath, "./GraphDir", "Wide&Deep OpNum Distribution", axs[1,2])
    
    YOLOPath = "/root/project/paperGraph/OpNumDir/YOLOOpNum.txt"
    color_legen9 = PieChart("YOLO.svg", YOLOPath, "./GraphDir", "YOLO OpNum Distribution", axs[1,3])
    
    InceptionPath = "/root/project/paperGraph/OpNumDir/InceptionOpNum.txt"
    color_legen10 = PieChart("Inception.svg", InceptionPath, "./GraphDir", "Inception OpNum Distribution", axs[1,4])
    
    all_colors = set(color_legen1+color_legen2+color_legen3+color_legen4+color_legen5+color_legen6+color_legen7+color_legen8+color_legen9+color_legen10)
    
    all_colors = {color[1]: color for color in all_colors}.values()

    unique_labels = []
    unique_wedget = []
    
    for color in all_colors:
        if color[1] not in unique_labels and color[1] != '1':
            unique_labels.append(color[1])
            unique_wedget.append(color[0])
    
    for i in range(5):
        axs[2,i].axis('off')

    axs[2,0].legend(unique_wedget, unique_labels, loc="center left", ncol=16,)
    plt.subplots_adjust(left=0.02, right=0.95, top=0.95, bottom=0.02)
    plt.subplots_adjust()
    plt.tight_layout()
    plt.savefig("PieChart.svg")
    
    