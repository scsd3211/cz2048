class Node:
    def __init__(self,item):
        self.item = item
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None
        self.Level  = None

class Tree:
    def __init__(self):
        self.root = None
        self.LevelAll = None
    def add(self, item):
        node = Node(item)
        if self.root is None:
            node.Level =  1
            self.root = node
            self.LevelAll = 1
        else:
            q = [self.root]

            while True:
                pop_node = q.pop(0)
                node.Level = pop_node.Level + 1
                print("pop_node",pop_node,"item",item)
                if pop_node.child1 is None:
                    pop_node.child1 = node
                    return
                elif pop_node.child2 is None:
                    pop_node.child2 = node
                    return
                elif pop_node.child3 is None:
                    pop_node.child3 = node
                    return
                elif pop_node.child4 is None:
                    pop_node.child4 = node
                    return
                else:
                    q.append(pop_node.child1)
                    q.append(pop_node.child2)
                    q.append(pop_node.child3)
                    q.append(pop_node.child4)
    def traverse(self):  # 层次遍历
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.item]
        resLevel = [self.root.Level]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.child1 is not None:
                q.append(pop_node.child1)
                res.append(pop_node.child1.item)
                resLevel.append(pop_node.child1.Level)

            if pop_node.child2 is not None:
                q.append(pop_node.child2)
                res.append(pop_node.child2.item)
                resLevel.append(pop_node.child2.Level)

            if pop_node.child3 is not None:
                q.append(pop_node.child3)
                res.append(pop_node.child3.item)
                resLevel.append(pop_node.child3.Level)

            if pop_node.child4 is not None:
                q.append(pop_node.child4)
                res.append(pop_node.child4.item)
                resLevel.append(pop_node.child4.Level)
        return res,resLevel


t = Tree()
for i in range(22):
    t.add(i)

resOut,resLevel = t.traverse()
print('层序遍历Res:',resOut)

print('层序遍历Lev:',resLevel)