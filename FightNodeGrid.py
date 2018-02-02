import datetime
import AI2048ME
import math
import copy
#[[2, 0, 0, 0], [2, 2, 0, 0], [8, 4, 2, 0], [32, 16, 4, 0]]
class Node:
    def __init__(self,item):
        self.item = item
        self.Name = "Me"
        self.child = [None]*4
        self.Grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.Level  = 0
        self.Over   = False
class NodeComputer:
    def __init__(self,item):
        self.item = item
        self.Name = "Computer"
        self.child = [None]*16
        self.Grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.Level  = 0         #记录这是第几层的节点
        self.Over   = False
class Tree:
    def __init__(self):
        self.root = None
        self.LevelAll = 0
        self.Lastroot = None

    def add(self, item):
        node = Node(item)
        nodeEnemy = NodeComputer(item)
        if self.root is None:
            node.Level =  1
            self.root = node
            self.LevelAll = 1
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                node.Level = pop_node.Level + 1
                nodeEnemy.Level = pop_node.Level + 1
                if(pop_node.Level%2 == 0):
                    pass
                    #print("pop_node16", pop_node, "item", item)
                    for i in range(16):
                        if pop_node.child[i] is None:
                            pop_node.child[i] = node
                            return

                    for i in range(16):
                        q.append(pop_node.child[i])
                else:
                    #print("pop_node",pop_node,"item",item)
                    for i in range(4):
                        if pop_node.child[i] is None:
                            pop_node.child[i] = nodeEnemy
                            return

                    for i in range(4):
                        q.append(pop_node.child[i])
    def Create(self, Num):

        if(Num > 0) and self.root is None:
            node = Node(0)
            nodeEnemy = NodeComputer(0)
            node.Level =  1
            self.root = node
            self.LevelAll = 1

        index16i =0;
        index4i =0
        itumNum = 1
        while(itumNum < Num):

            q = [self.root]

            while (itumNum < Num):
                node = Node(itumNum)
                nodeEnemy = NodeComputer(itumNum)

                pop_node = q.pop(0)



                #print("pop_node.Level",pop_node.Level)
                if(pop_node.Level%2 == 0):
                    pass
                    #print("pop_node16", pop_node, "item", item)
                    for i in range(16):
                        node = Node(itumNum)
                        node.Level = pop_node.Level + 1
                        pop_node.child[i] = node
                        itumNum = itumNum + 1
                        if(itumNum == Num):
                            return

                    for i in range(16):
                        q.append(pop_node.child[i])
                else:
                    #print("pop_node",pop_node,"item",item)
                    for i in range(4):
                        nodeEnemy = NodeComputer(itumNum)
                        nodeEnemy.Level = pop_node.Level + 1
                        pop_node.child[i] = nodeEnemy
                        itumNum = itumNum + 1
                        if(itumNum == Num):
                            return

                    for i in range(4):
                        q.append(pop_node.child[i])
    def CreateNew(self, HowManyLevel,TotalHAHA):
        TotalNumLog = copy.deepcopy(TotalHAHA)
        if(HowManyLevel > 0) and self.root is None:
            node = Node(0)
            nodeEnemy = NodeComputer(0)
            node.Level =  1
            node.Grid = copy.deepcopy(TotalHAHA)
            self.root = node
            self.LevelAll = 1

        index16i =0;
        index4i =0
        itumNum = 1
        NowLevel = 1

        q = [self.root]
        while (NowLevel <= HowManyLevel):
            pop_node = q.pop(0)
            if(pop_node.Level + 1 > HowManyLevel):
                break

            #print("pop_node.Level",pop_node.Level)
            if(pop_node.Level%2 == 0 and pop_node.Level <= HowManyLevel):
                pass
                #print("pop_node16", pop_node, "item", item)
                for i in range(16):
                    node = Node(itumNum)
                    node.Grid = AI2048ME.GridSetEmpty2(pop_node.Grid,i)
                    node.Level = pop_node.Level + 1
                    pop_node.child[i] = node
                    itumNum = itumNum + 1
                for i in range(16):
                    q.append(pop_node.child[i])
            elif(pop_node.Level%2 == 1 and pop_node.Level <= HowManyLevel):
                #print("pop_node",pop_node,"item",item)
                for i in range(4):
                    nodeEnemy = NodeComputer(itumNum)
                    if(i == 0):
                        nodeEnemy.Grid,nodeEnemy.Over = AI2048ME.UPHandle(pop_node.Grid)
                    elif(i == 1):
                        nodeEnemy.Grid,nodeEnemy.Over  = AI2048ME.DownHandle(pop_node.Grid)
                    elif(i == 2):
                        nodeEnemy.Grid,nodeEnemy.Over  = AI2048ME.RightHandle(pop_node.Grid)
                    elif(i == 3):
                        nodeEnemy.Grid,nodeEnemy.Over  = AI2048ME.LeftHandle(pop_node.Grid)
                    print("nodeEnemy.Grid ", i,nodeEnemy.Grid,)
                    nodeEnemy.Level = pop_node.Level + 1
                    pop_node.child[i] = nodeEnemy
                    itumNum = itumNum + 1
                for i in range(4):
                    q.append(pop_node.child[i])



    def addNodeMe(self):
        pass
    def addNodeComputer(self):
        pass

    def traverse(self):  # 层次遍历
        LevelChange =0;
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.item]
        print(self.root.item)
        resLevel = [self.root.Level]
        while q != []:
            pop_node = q.pop(0)
            if(LevelChange != pop_node.Level):
                #print('')
                LevelChange = pop_node.Level
            #if(pop_node.Level%2 == 1):
            if (pop_node.Name == "Me"):
                for i in range(4):
                    if pop_node.child[i] is not None:
                        q.append(pop_node.child[i])
                        #res.append(pop_node.child[i].item)
                        #print(pop_node.child[i].item," ",end='')

                        #resLevel.append(pop_node.child[i].Level)

            else:
                for i in range(16):
                    if pop_node.child[i] is not None:
                        q.append(pop_node.child[i])
                        #res.append(pop_node.child[i].item)
                        #print(pop_node.child[i].item," ", end='')
                        #resLevel.append(pop_node.child[i].Level)
        return res, resLevel

    def traverseNew(self,HowManyLevel):  # 层次遍历
        LevelChange = 0;
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.item]
        print(self.root.item)
        print(self.root.Grid)
        resLevel = [self.root.Level]
        NowLevel =0;

        while (NowLevel <= HowManyLevel):
            pop_node = q.pop(0)
            if(LevelChange != pop_node.Level):
                print('')
                LevelChange = pop_node.Level
            if(pop_node.Level < HowManyLevel):
                pass
            else:
                break
            if (pop_node.Name == "Me"):
                for i in range(4):
                    q.append(pop_node.child[i])
                        # res.append(pop_node.child[i].item)
                    print(pop_node.child[i].item," ",end='')
                    print(pop_node.child[i].Grid)
                    resLevel.append(pop_node.child[i].Level)

            else:
                for i in range(16):
                    q.append(pop_node.child[i])
                        # res.append(pop_node.child[i].item)
                    print(pop_node.child[i].item," ", end='')
                    print(pop_node.child[i].Grid)
                    resLevel.append(pop_node.child[i].Level)

        return res,resLevel

print("Start",datetime.datetime.now())
t = Tree()
'''
for i in range(144):
    t.add(i)
'''
#t.Create(262144);
CreateLevel = 3
GeneraFrid = [[2, 0, 0, 0], [2, 2, 0, 0], [8, 4, 2, 0], [32, 16, 4, 0]]
t.CreateNew(CreateLevel,GeneraFrid);
print("add over")

print("TreeOK",datetime.datetime.now())
#resOut,resLevel = t.traverse()

resOut,resLevel = t.traverseNew(CreateLevel)
#print('层序遍历Res:',resOut)

#print('层序遍历Lev:',resLevel)

print('层序遍历Lev:',len(resLevel))
print("SearchOver",datetime.datetime.now())