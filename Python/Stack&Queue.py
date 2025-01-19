#stack in python
#stack is last come first out


class Stack:

  def __init__(self) -> None:
    self.items = []

  def push(self, item):
    #push item to the top of the stack
    self.items.append(item)

  def pop(self):
    #remove the top most element
    return self.items.pop()

  def is_empty(self):
    #check if the stack is empty
    return self.items == []

  def peek(self):
    #return the top most element
    if not self.is_empty():
      return self.items[-1]

  def display(self):
    print(self.items)


class Queue:

  def __init__(self) -> None:
    self.items = []

  def is_empty(self):
    #check if the queue is empty
    return self.items == []

  def enqueue(self, item):
    #add item to the back of the queue
    self.items.append(item)

  def dequeue(self):
    #remove the front most element
    return self.items.pop(0)

  def display(self):
    #display the queue
    print(self.items)


print("Stack")

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.display()
print(stack.peek())  #peeking
print(stack.pop())  #popping
stack.display()  #displaying

print("queue")

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.display()
print(queue.dequeue())
queue.display()
