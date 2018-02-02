import copy
import AI2048ME


for i in range(4):
    pass
    for j in range(4):
        pass
        haha = str(i) + "-" + str(j) + "-Grid"
        print(haha)
OKL =[12,234,45,6]

print(max(OKL))
print("OKL")

print("OKL index",OKL.index(max(OKL)))


hahaKK = [[4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4,4]]
#hahaK = [[4, 0, 4, 4], [0, 0, 16, 2], [0, 8, 8, 0], [0, 0, 0, 2]]
hahaK = [[0, 0, 4, 4], [0, 2, 16, 2], [0, 0, 8, 0], [0, 0, 0, 2]]

def UPHandle(TotalHAHA):
    TotalNumLog = copy.deepcopy(TotalHAHA)

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
                        pass
                    elif (TotalNumLog[i][j] == TotalNumLog[i][k]):
                        TotalNumLog[i][j] = TotalNumLog[i][j] * 2
                        TotalNumLog[i][k] = 0;
                        pass
                    else:
                        pass

                    break
                else:
                    pass
            j = j + 1;


    return TotalNumLog

def DownHandle(TotalHAHA):
    TotalNumLog = copy.deepcopy(TotalHAHA)

    for i in range(4):
        j = 3
        Merge = 0
        while (j >= 0):
            for k in range(j - 1, -1, -1):
                if (TotalNumLog[i][k] > 0):
                    if (TotalNumLog[i][j] <= 0):
                        TotalNumLog[i][j] = TotalNumLog[i][k];
                        TotalNumLog[i][k] = 0
                        j = j + 1
                        pass
                    elif (TotalNumLog[i][j] == TotalNumLog[i][k]):
                        TotalNumLog[i][j] = TotalNumLog[i][j] * 2
                        TotalNumLog[i][k] = 0;
                        pass
                    else:
                        pass

                    break
                else:
                    pass

            j = j - 1;

    return TotalNumLog

def RightHandle(TotalHAHA):
    TotalNumLog = copy.deepcopy(TotalHAHA)

    for j in range(4):
        i = 3
        Merge = 0
        while (i >= 0):
            for k in range(i - 1, -1, -1):
                if (TotalNumLog[k][j] > 0):
                    if (TotalNumLog[i][j] <= 0):
                        TotalNumLog[i][j] = TotalNumLog[k][j];
                        TotalNumLog[k][j] = 0
                        i = i + 1
                        pass
                    elif (TotalNumLog[i][j] == TotalNumLog[k][j]):
                        TotalNumLog[i][j] = TotalNumLog[i][j] * 2
                        TotalNumLog[k][j] = 0;
                        pass
                    else:
                        pass

                    break
                else:
                    pass
            #print("i=", i)
            i = i - 1;

    return TotalNumLog

def LeftHandle(TotalHAHA):
    TotalNumLog = copy.deepcopy(TotalHAHA)

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
                        pass
                    elif (TotalNumLog[i][j] == TotalNumLog[k][j]):
                        TotalNumLog[i][j] = TotalNumLog[i][j] * 2
                        TotalNumLog[k][j] = 0;
                        pass
                    else:
                        pass

                    break
                else:
                    pass
            i = i + 1;

    return TotalNumLog
print(hahaK)


NONO = UPHandle(hahaK)
print("NONO",NONO)

print("hahak",hahaK)
DODO = DownHandle(hahaK)

print("Down",DODO)
print("hahak",hahaK)
DODO = RightHandle(hahaK)

print("Right",DODO)


print("hahak",hahaK)
DODO = LeftHandle(hahaK)
print("Left",DODO)


print(hahaKK)
NONO = UPHandle(hahaKK)
haha = AI2048ME.AI2048ME()
haha.Test();
Log2Out = AI2048ME.Log2Handle(hahaKK)
print("Log2Out",Log2Out)
momotemp = haha.monoWeightCount(Log2Out)

print("momotemp",momotemp)

print(NONO)


print("ininin",int(15/4))