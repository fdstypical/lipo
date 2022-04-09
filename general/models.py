class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self, head = None):
    self.head = head
  
  def add_last(self, node):
    if self.head == None:
      self.head = node
      return self
    
    last_node = self.head

    while last_node.next is not None:
      last_node = last_node.next
    
    last_node.next = node
    return self

  def iterate(self):
    if self.head == None:
      raise ReferenceError('Empty list')

    last_node = self.head

    while last_node is not None:
      yield last_node
      last_node = last_node.next

  def print(self):
    if self.head == None:
      print('Empty list')
      return
    
    last_node = self.head

    while last_node is not None:
      print(last_node.data, end = '')

      last_node = last_node.next

      if last_node != None:
        print(' --->', end = ' ')
      else:
        print(end = '\n')
