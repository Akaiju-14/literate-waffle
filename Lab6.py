class Node :
    def __init__(self,data): 
        self.data = data 
        self.next=None

class Stack:
    def __init__(self):
        self.top =None

    def push(self,data):
        new_node=Node(data)
        if self.top:            
            new_node.next=self.top
        self.top=new_node
    
    def pop(self):
        if self.top is None:
            return  None
        else: 
            popped_node = self.top 
            self.top = self.top.next
            popped_node.next=None
            return popped_node.data
        
    def merge(self, list_1,list_2):
        list1 = list_1
        list2 = list_2
        newStack = Stack()

        current_node = list1.top
        List = []

        while current_node:
            List.append(current_node.data)
            current_node = current_node.next

        current_node = list2.top
        while current_node:
            List.append(current_node.data)
            current_node = current_node.next
        
        List.sort()
        for i in List:
            newStack.push(i)
        
        current_node = newStack.top
        while current_node:
            print(current_node.data)
            current_node = current_node.next

        return newStack

    def peek(self):
        if self.top:
            return self.top.data 
        else:
            return None
        
    def is_empty(self):
        return self.top is None
    
    def print_stack(self):
        current_node=self.top
        while current_node:
            print(current_node.data)
            current_node=current_node.next
        # print("None")
    def size(self):
        current_node=self.top
        count=0
        while current_node:
            count+=1
            current_node=current_node.next
        return count


print("List 1")
stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(4)
stack1.push(3)
stack1.print_stack()

print("\nList 2")
stack2 = Stack()
stack2.push(4)
stack2.push(5)
stack2.push(2)
stack2.push(1)
stack2.push(3)
stack2.print_stack()

print("Merged Stack")
stack_merge = Stack()
stack_merge.merge(stack1,stack2)