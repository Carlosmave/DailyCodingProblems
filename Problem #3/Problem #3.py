##First solution:
##class Node: 
##    def __init__(self, val, left=None, right=None): 
##        self.val = val 
##        self.left = left 
##        self.right = right
##
##def serialize(node):
##    val = node.val
##    if node.left:
##        left = serialize(node.left)
##    else:
##        left = None
##    if node.right:
##        right = serialize(node.right)
##    else:
##        right = None
##    serialized = [val, left, right]
##    print(serialized)
##    return serialized
##
##def deserialize(serialized_node):
##    val = serialized_node[0]
##    if serialized_node[1]:
##        left = deserialize(serialized_node[1])
##    else:
##        left = None
##    if serialized_node[2]:
##        right = deserialize(serialized_node[2])
##    else:
##        right = None
##    return Node(val, left, right)
##
##tree = Node('root', Node('left', Node('left.left')), Node('right'))
##assert deserialize(serialize(tree)).left.left.val=="left.left"


##Pythonic way:
class Node: 
    def __init__(self, val, left=None, right=None): 
        self.val = val 
        self.left = left 
        self.right = right

    def __repr__(self):
        return ('Node(' + repr(self.val) + ', ' + repr(self.left)
                +   ', ' + repr(self.right) + ")")


tree = Node('root', Node('left', Node('left.left')), Node('right'))
serialized_tree = repr(tree)
print(serialized_tree)
deserialized_tree = eval(serialized_tree)
assert deserialized_tree.left.left.val == "left.left"







##class Complex: 
##  
##    # Constructor 
##    def __init__(self, real, imag): 
##       self.real = real 
##       self.imag = imag 
##  
##    # For call to repr(). Prints object's information 
##    def __repr__(self): 
##       return 'Rational(%s, %s)' % (self.real, self.imag)     
##  
##    # For call to str(). Prints readable form 
##    def __str__(self): 
##       return '%s + i%s' % (self.real, self.imag)     
##  
##  
### Driver program to test above 
##t = Complex(10, 20) 
##print(t) 
##print (str(t))  # Same as "print t" 
##print (repr(t)) 



##class Pepe: 
##    def __init__(self, val=""): 
##        self.val = val 
##
##    def __str__(self):
##        return self.val + "pepe"
##    
##    def __type__(self):
##        return self.val
##
###blar=Pepe()
###print(len(blar))
###blar2=True
###print(str(blar2))
##blar3=Pepe("JOJOJO")
##print(blar3)
##print(str(blar3))
##print(type(blar3))


