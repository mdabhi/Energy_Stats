import pandas as pd


def Read_DataFile():
    df = pd.read_csv("C:\\Users\\User1\\Desktop\\Energy_Statistics\\WorldEnergyConsumption.csv")
    
    for line in df:
        print(line)


if __name__ == '__main__':
    print("---------------------World Energy consumption-----------------------")
    Read_DataFile()

