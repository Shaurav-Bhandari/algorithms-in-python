#............stack............
stack  = [None for i in range(0,10)] # initialize stack
root = 0 # set the base pointer of the stack. In case of python, it is always zero
top = -1 # set the top of stack pointer. at the start, it is always root -1
full = len(stack) # set the maximum length of the stack
item = None # set the poped value here
def pop(): # function that pops elements in the stack
    global top,root,item, stack # declare global variables
    if top == root-1: # check if stack empty
        print("stack empty cannot pop")
        return 
    else:
        item = stack[top] # set the top item of the stack
        stack[top] = None
        top -= 1 # subtract stack by one
        return 
def push(item): # pushes elements in the stack
    global top,stack
    if top < full -1: # checks if stack is full.
        top += 1 # increment top
        stack[top] = item # set item on the top of stack
        return
    else:
        print("stack full")
        return
    
#....................queue...................
queue = [None for i in range(10)] # initialize the queue with none data types
front = 0 # initialize the front pointer of the queue
rear = -1 # initialize the rear pointer of the queue
full = len(queue) # initialize the length of the queue
length = 0 
Item = None
def enqueue(item):
    global length, rear, queue
    if length < full:
        if rear < len(queue) -1:
            rear += 1
        else:
            rear = 0
        length += 1
        queue[rear] = item
    else:
        print("queue full try again.")

def dequeue():
    global length, front, Item
    if length == 0:
        print("queue empty.")
    else:
        Item = queue[front]
        if front == len[queue] -1:
            front = 0
        else:
            front += 1
    length -= 1
    
