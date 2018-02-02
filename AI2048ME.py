#!/usr/bin/python3
import math
import copy
def Log2Handle(TotalHAHA):
    TotalNumLog = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        pass
        for j in range(4):
            pass
            if(TotalHAHA[i][j] != 0):
                TotalNumLog[i][j] = int(math.log2(TotalHAHA[i][j]))

    return  TotalNumLog

def UPHandle(TotalHAHA):
    TotalNumLog = copy.deepcopy(TotalHAHA)
    merge =0;
    for i in range(4):
        j = 0
        Merge = 0
        while(j < 4):
            for k in range(j+1,4,1):
                if(TotalNumLog[i][k] > 0):
                    if(TotalNumLog[i][j] <= 0):
                        TotalNumLog[i][j] = TotalNumLog[i][k];
                        TotalNumLog[i][k] = 0
                        j = j - 1
                        merge = 1
                        pass
                    elif (TotalNumLog[i][j] == TotalNumLog[i][k]):
                        TotalNumLog[i][j] = TotalNumLog[i][j] * 2
                        TotalNumLog[i][k] = 0;
                        merge = 1
                        pass
                    else:
                        pass

                    break
                else:
                    pass
            j = j + 1;

    print("UPHandle", TotalNumLog)
    return TotalNumLog,merge

def DownHandle(TotalHAHA):
    TotalNumLog = copy.deepcopy(TotalHAHA)
    merge = 0;
    for i in range(4):
        j = 3

        while (j >= 0):
            for k in range(j - 1, -1, -1):
                if (TotalNumLog[i][k] > 0):
                    if (TotalNumLog[i][j] <= 0):
                        TotalNumLog[i][j] = TotalNumLog[i][k];
                        TotalNumLog[i][k] = 0
                        j = j + 1
                        merge = 1;
                        pass
                    elif (TotalNumLog[i][j] == TotalNumLog[i][k]):
                        TotalNumLog[i][j] = TotalNumLog[i][j] * 2
                        TotalNumLog[i][k] = 0;
                        merge = 1;
                        pass
                    else:
                        pass

                    break
                else:
                    pass

            j = j - 1;
    print("DownHandle", TotalNumLog)
    return TotalNumLog,merge

def RightHandle(TotalHAHA):
    TotalNumLog = copy.deepcopy(TotalHAHA)
    merge = 0;
    for j in range(4):
        i = 3

        while (i >= 0):
            for k in range(i - 1, -1, -1):
                if (TotalNumLog[k][j] > 0):
                    if (TotalNumLog[i][j] <= 0):
                        TotalNumLog[i][j] = TotalNumLog[k][j];
                        TotalNumLog[k][j] = 0
                        i = i + 1
                        merge = 1;
                        pass
                    elif (TotalNumLog[i][j] == TotalNumLog[k][j]):
                        TotalNumLog[i][j] = TotalNumLog[i][j] * 2
                        TotalNumLog[k][j] = 0;
                        merge = 1;
                        pass
                    else:
                        pass

                    break
                else:
                    pass
            #print("i=", i)
            i = i - 1;
    print("RightHandle", TotalNumLog)
    return TotalNumLog,merge

def LeftHandle(TotalHAHA):
    TotalNumLog = copy.deepcopy(TotalHAHA)
    merge = 0;
    for j in range(4):
        i = 0
        Merge = 0
        while (i < 4):
            for k in range(i + 1, 4, 1):
                if (TotalNumLog[k][j] > 0):
                    if (TotalNumLog[i][j] <= 0):
                        TotalNumLog[i][j] = TotalNumLog[k][j];
                        TotalNumLog[k][j] = 0
                        i = i - 1
                        merge = 1;
                        pass
                    elif (TotalNumLog[i][j] == TotalNumLog[k][j]):
                        TotalNumLog[i][j] = TotalNumLog[i][j] * 2
                        TotalNumLog[k][j] = 0;
                        merge = 1;
                        pass
                    else:
                        pass

                    break
                else:
                    pass
            i = i + 1;
    print("LeftHandle", TotalNumLog)
    return TotalNumLog,merge

class AI2048ME:
    """一个简单的类实例"""
    i = 12345
    smoothWeight = 0.1,
    monoWeight = 0.0,
    islandWeight = 0.0,
    mono2Weight = 1.0,
    emptyWeight = 2.7,
    maxWeight = 1.0;

    ArrowFour = [[0,-1]]

    def Test(self):
        print( 'hello world')


    def eval(self):
        pass
    #权衡平滑性
    def smoothWeightCount(self,TotalNum):
        SmoothValue =0;
        TotalNumIN = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(4):
            for j in range(4):
                pass
                TotalNumIN = math.log2(TotalNum[i][j])


        pass
        return SmoothValue;
    #权衡空置率
    def emptyWeightCount(self):
        emptyWeightValue =0;
        pass
        return emptyWeightValue;

    #权衡单调性
    def monoWeightCount(self,TotalNum):
        monoWeightValue =0;
        pass
        TotalNumIN = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        monoWeightValueD = 0
        for i in range(4):
            for j in range(1,4):
                pass
                monoWeightValueD += abs(TotalNum[i][j-1] - TotalNum[i][j])
        print("monoWeightValueD", monoWeightValueD)
        monoWeightValueU =0;
        for i in range(4):
            for j in range(3,0,-1):
                pass
                monoWeightValueU += abs(TotalNum[i][j] - TotalNum[i][j-1])
        print("monoWeightValueU", monoWeightValueU)
        monoWeightValueL =0
        for j in range(4):
            for i in range(3,0,-1):
                pass
                monoWeightValueL += abs(TotalNum[i][j] - TotalNum[i-1][j])
        print("monoWeightValueL", monoWeightValueL)
        monoWeightValueR = 0;
        for j in range(4):
            for i in range(1,4):
                pass
                monoWeightValueR += abs(TotalNum[i-1][j] - TotalNum[i][j])
        print("monoWeightValueR", monoWeightValueR)
        monoWeightValue = abs(monoWeightValueD) + abs(monoWeightValueL)
        return monoWeightValue;

    #权衡孤岛效应
    def islandWeightCount(self):
        islandWeightValue =0;
        pass
        return islandWeightValue;

    #劝和最大值的价值
    def maxWeightCount(self):
        maxWeightValue =0;
        pass
        return maxWeightValue;




def WhichOneIsRightToDo(TotalHAHA):
    TotalNumLog = copy.deepcopy(TotalHAHA)
    ShowMe = Log2Handle(TotalNumLog)
