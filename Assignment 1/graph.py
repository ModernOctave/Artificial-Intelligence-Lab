class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.up = None
        self.down = None


class LinkedList:

    def __init__(self):
        self.head = None 


if __name__=='__main__':
    dir = ['up','down','left','right']

    llist = LinkedList()

    llist.head = Node((0,0))

    for x in dir:
        if x == 'up':
            

