class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str("%s:%s" %(self.key, self.value))

class HashChainMap:
    def __init__(self, M):
        self.table = [None] * M
        self.M = M

    def hachFn(self, key):
        sum = 0
        for c in key:
            sum += ord(c)

        return sum%self.M

    def insert(self, key, value):
        idx = self.hashFn(key)

        self.table[idx] = Node(Entry(key, value), self.table[idx])

    def search(self, key):
        idx = self.hashFn(key)
        node = self.table[idx]
        
        while node is not None:
            if node.data.key == key:
                return node.data
            
            node = node.link

        return None

    def delete(self, key):
        idx = self.hashFn(key)
        node = self.table[idx]

        before = None
        while node is not None:
            if node.dtat.key == key:
                if before == None:
                    self.table[idx] = node.link
                else:
                    before.link = node.link

                return

            before = node
            node = node.link

    def display(self, msg):
        print(msg)
        for idx in range(len(self.table)):
            node = self.table[idx]

            if node is not None:
                print("[2%d] -> " %(idx), end = '')

                while node is not None:
                    print(node.data, end = ' -> ')
                    node = node.link

                print()
