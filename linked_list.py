class Node: # class to initialize the linked list.
    def __init__(self, data=None, next=None): 
        self.data = data
        self.next = next

class LinkedList: # class to perform different operations in an linked list
    def __init__(self):
        self.head = None # initializes the first element of the linked list as none

    def print(self): #prints the linked list
        if self.head is None: #if head is empty,
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self): # returns the length of the linked list
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data): # data inserted at the begining of the list where the new inserted value becomes head
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data): # data inserted at the end
        if self.head is None: #insert the value if the head is none
            self.head = Node(data, None)
            return
        # if list  is not empty,
        itr = self.head

        while itr.next: # loop until the next pointer(self.next) is none
            itr = itr.next
            # after itr.next becomes none insert the value
        itr.next = Node(data, None) 

    def insert_at(self, index, data): # insert the value at a specified location
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0: 
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head # set itr to head pointer
        while itr: # loop until itr is None or break condition is met
            if count == index - 1: # if the value of count reaches exactly below index for eg index = 9 and count = 8,
                node = Node(data, itr.next) # data is the value to insert and itr.next will point the next pointer that is pointed by the previous element
                itr.next = node # set the data that is pointed by next pointer of the element as the values in node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index): # remove element at certain index.
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0: # if the first element is to be removed,
            self.head = self.head.next # set self.hesd as the pointer it is pointing to as the next element
            return
        # if other index values are to be removed,
        count = 0
        itr = self.head
        while itr: # loop until itr is null/none
            if count == index - 1:
                itr.next = itr.next.next # visualize yourself. it's too long to explain
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list): # insert a set of values such as list, tuple
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.insert_at(1,"blueberry")
ll.remove_at(2)
ll.print()

ll.insert_values([45,7,12,567,99])
ll.insert_at_end(67)
ll.print()