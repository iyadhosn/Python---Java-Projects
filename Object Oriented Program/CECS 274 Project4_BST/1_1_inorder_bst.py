
class Node:
  def __init__(self, key=None):
    self.key = key
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None

  def findMin_ini(self):
    FNode = self.findMin(self.root)
    return FNode

  def findMax_ini(self):
    FNode = self.findMax(self.root)
    return FNode

  def findMin(self, root):
    # Returns left most node of BST
    while root.left is not None:
      root = root.left
    return root.key

  def findMax(self, root):
    # Returns right most node of BST
    while root.right is not None:
      root = root.right
    return root.key

  def insert(self, data):
    self.root = self.insertInTree(self.root, data)

  def insertInTree(self, root, key):
    # Creates a root if the tree is empty
    if root is None:
      root = Node(key)
      return root
    # Traverse the tree, comparing the key to the value of each node going to the left child if the key is smaller
    # and the right child if the key is bigger until the key reaches its proper location to satisfy the max heap condition.
    if key > root.key:
      if root.right is None:
        root.right = Node(key)
      else:
        root.right = self.insertInTree(root.right, key)
    elif key < root.key:
      if root.left is None:
        root.left = Node(key)
      else:
        root.left = self.insertInTree(root.left, key)
    # If the value you want to insert already exists in the tree
    else:
      print("The value is already present in the tree.")
    return root

  def delete_ini(self, key):
    self.root = self.delete(self.root, key)

  def delete(self, root, key):
    # Traverse the tree getting to the node that contains that key value.
    if key < root.key:
      if root.left:
        self.delete(root.left, key)
    elif key > root.key:
      if root.right:
         self.delete(root.right, key)
    else:
        # Once at proper node the min. val at the right of the root is passed into the delete
        # and recursion is used to delete the node
        if root.left is None and root.right is None:
          return None
        if root.left is None:
          return root.right
        if root.right is None:
          return root.left
        min_val = self.findMin(root.right)
        root.key = min_val
        root.right = self.delete(root.right, min_val)
    return root

  def traverseInOrder_ini(self, elements):
    return self.traverseInOrder(self.root, elements)

  def traverseInOrder(self, root, elements):
    # Traverse the bottom left side of the tree first making way up to root node of subtree and then the right side.
    # Once the whole left side has been traversed head to the root node and repeat the process with the right subtree's.
    if root.left:
      self.traverseInOrder(root.left, elements)
    elements.append(root.key)
    if root.right:
      self.traverseInOrder(root.right, elements)
    return elements

  def visit(self, node):
    print(node.key)

  def getRoot(self):
    return self.root

def main():

  print ("\nInsert the following numbers: ")
  print ("15, 23, 32, 40, 57, 36, 88")

  Tree = BST()
  Tree.insert(15)
  Tree.insert(23)
  Tree.insert(32)
  Tree.insert(40)
  Tree.insert(57)
  Tree.insert(36)
  Tree.insert(88)


  print ("Output the Min Value: ")
  min = Tree.findMin_ini()
  print (min, "\n")
  #
  print ("Output the Max Value: ")
  max = Tree.findMax_ini()
  print (max, "\n")
  #
  elements = []
  print ("Inorder traversal of the given tree: ")
  print(Tree.traverseInOrder_ini(elements))
  #
  print ("\n Now delete 40")
  Tree.delete_ini(40)
  #
  elements = []
  print ("\nInorder traversal of tree")
  print(Tree.traverseInOrder_ini(elements))
  #
  print ("\n Now delete 15")
  Tree.delete_ini(15)
  #
  elements = []
  print ("\nInorder traversal of tree")
  print(Tree.traverseInOrder_ini(elements))

  print ("\nOutput the new root node: ")
  gt = Tree.getRoot()
  print (gt.key)


if __name__ == "__main__":
  main()
