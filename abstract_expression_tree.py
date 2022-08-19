 # Supposed to gain insight that this is how to solve the problem and solve it in 20 minutes
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"Node(val:{self.val}, left:{self.left}, right:{self.right})"

def build_eval_tree(expr:str):
    eval_tree=None
    node=eval_tree
    number = '' 
    for index in range(len(expr)):
        value = expr[index]
        if value.isnumeric():
            number = number + value
        elif not node and not value.isnumeric():
            node = Node(value)
            node.left = Node(int(number))
            eval_tree = node
            number = ''
        elif value == "*":
            node.right = Node(value)
            node = node.right
            node.left = Node(int(number))
            number =''
        elif value == "+":
            node.right = Node(int(number))
            node = Node(value)
            node.left = eval_tree
            eval_tree = node
            number = ''
    node.right = Node(int(number))
    return eval_tree

def calculate(node:Node):
    if node.val == "*":
        return calculate(node.left) * calculate(node.right)
    elif node.val == "+":
        return calculate(node.left) + calculate(node.right)
    else:
        return node.val


def walk(node):
    if node:
        walk(node.left)
        print(node.val)
        walk(node.right)
