class Node:
    def __init__(self,item):
        self.item = item
        self.Name = "Me"
        self.child = [None]*4

        self.Level  = 0
class NodeComputer:
    def __init__(self,item):
        self.item = item
        self.Name = "Computer"
        self.child = [None]*16
        self.Level  = 0
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
            node = Node(itumNum)
            nodeEnemy = NodeComputer(itumNum)
            while (itumNum < Num):
                pop_node = q.pop(0)
                node.Level = pop_node.Level + 1
                nodeEnemy.Level = pop_node.Level + 1
                if(pop_node.Level%2 == 0):
                    pass
                    #print("pop_node16", pop_node, "item", item)
                    for i in range(16):
                        node = Node(itumNum)
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
                        pop_node.child[i] = nodeEnemy
                        itumNum = itumNum + 1
                        if(itumNum == Num):
                            return

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
                print('')
                LevelChange = pop_node.Level
            if(pop_node.Level%2 == 1):
                for i in range(4):
                    if pop_node.child[i] is not None:
                        q.append(pop_node.child[i])
                        res.append(pop_node.child[i].item)
                        print(pop_node.child[i].item," ",end='')
                        resLevel.append(pop_node.child[i].Level)

            else:
                for i in range(16):
                    if pop_node.child[i] is not None:
                        q.append(pop_node.child[i])
                        res.append(pop_node.child[i].item)
                        print(pop_node.child[i].item," ", end='')
                        resLevel.append(pop_node.child[i].Level)




        return res,resLevel


t = Tree()
'''
for i in range(144):
    t.add(i)
'''
t.Create(144);
print("add over")
resOut,resLevel = t.traverse()
#print('层序遍历Res:',resOut)

#print('层序遍历Lev:',resLevel)

print('层序遍历Lev:',len(resLevel))