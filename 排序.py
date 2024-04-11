import pandas
import numpy

def order(
    fileNameNoSuffix
):
    order = []
    with open("./Orderdata.txt") as f:
        op = f.readline().strip()
        while op: 
            order.append(op)
            op = f.readline().strip()
    
    pandas.DataFrame(order).to_csv("Orderdata.csv", index=False, header=False)

    orderFile = pandas.read_csv("Orderdata.csv", header=None)
    orderData = orderFile.values
        
    zeroData_colum = numpy.zeros((orderData.shape[0], 1), dtype=int)
    orderData = numpy.hstack((orderData, zeroData_colum))
    # print(orderData)
    fileName = "ModelNetHaveOP_Num/" + fileNameNoSuffix + ".txt"
    
    df = pandas.read_csv(fileName, header=None)
    
    data_array = df.values
    dataMap = { data_array[i][0]: data_array[i][1]  for i in range(len(data_array))}
    
    # print(data_array)
    
    newDF = pandas.DataFrame(columns=["OpName", "Numbers"])
    
    for i in range(0, len(orderData), 1):
        if orderData[i][0] in dataMap:
            newDF.loc[i] = [orderData[i][0], dataMap[orderData[i][0]]]
        else:
            newDF.loc[i] = [orderData[i][0], 0]

    # print(newDF)
    saveFileName = "ModelNetHaveOP_Num/" + fileNameNoSuffix + ".csv"
    newDF.to_csv(saveFileName, index=False, header=True)

if __name__ == "__main__":
    
    fileLists = [
        "AlexNet",
        "Bert_Tiny",
        "DeepFM",
        "Inception",
        "LeNet",
        "MobileNet",
        "ResNet18",
        "SqueezeNet",
        "Wide_Deep",
        "YOLO",
    ]
    
    for f in fileLists:
        order(f)
        