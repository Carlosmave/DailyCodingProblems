## Daily Coding Problem: Problem #3 [Medium]



Good morning! Here's your coding interview problem for today.<br/><br/>
This problem was asked by Google.<br/><br/>
Given the root to a binary tree, implement ```serialize(root)```, which serializes the tree into a string, and ```deserialize(s)```, which deserializes the string back into the tree.<br/><br/>
For example, given the following ```Node``` class:<br/>
```
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
The following test should pass:<br/>
```
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```
