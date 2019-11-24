from typing import List

class Node:
    def __init__(self, val, children = []):
        self.val = val
        self.children = children 

class BinaryTreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left: Node = left 
        self.right: Node = right
    def __str__(self):
        output = f"{self.val}\n"
        currentLevel = [self.left, self.right] 

        while currentLevel:
            nextLevel = []
            for node in currentLevel:
                if node:
                    output += str(node.val)
                    output += " "
                    nextLevel.append(node.left)
                    nextLevel.append(node.right)
                else:
                    output += "* "


            output += "\n"
            currentLevel = nextLevel

        return output
    def __repr__(self):
        return str(self.val)

class LinkedListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def append(self, val):
        if self.next:
            self.next.append(val)
        else:
            self.next = LinkedListNode(val)
    def __repr__(self):
        if self.next:
            return f"{self.val} -> " + repr(self.next)
        else:
            return f"{self.val}"

class TreesGraphs:
    @staticmethod
    def routeBetweenNodes(startNode: Node, endNode: Node) -> bool:
        # Does not work with graphs with cycles
        if not startNode.children: # where null children or empty children
            return False
        else:
            for c in startNode.children:
                if c is endNode:
                    return True
                else:
                    return TreesGraphs.routeBetweenNodes(c,endNode)

    @staticmethod
    def routeBetweenNodes(startNode: Node, endNode: Node) -> bool:

        queue = [startNode]
        visited: set = set(startNode)

        while queue: # is not empty..
            node: Node = queue.pop(0)
            visited.add(node)

            if node is endNode:
                return True
            else:
                for c in startNode.children:
                    if c not in visited:
                        queue.append(c)
        else:
            return False

    """
    Given a sorted array with unique integer elements, write an algorithm to create a binary search tree with minimal height
    """
    @staticmethod
    def minimalTree(ns: List) -> BinaryTreeNode:
        if len(ns) == 0:
            return None
        elif len(ns) == 1:
            return BinaryTreeNode(ns[0])
        else:
            midPos = len(ns)//2
            leftSubTree = TreesGraphs.minimalTree(ns[:midPos])
            rightSubTree = TreesGraphs.minimalTree(ns[midPos+1:])
            return BinaryTreeNode(ns[midPos],leftSubTree,rightSubTree)
    