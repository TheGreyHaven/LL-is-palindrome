class Node(object):
    def __init__(self, data, next=None):
        self.next = next
        self.data = data


class LL(object):
    def __init__(self, node):
        self.head = node


    def is_palindrome(self):

        slow = self.head
        fast = self.head

        my_list = []
        
        

        while fast is not None and fast.next is not None: 
            my_list.append(slow.data)
            slow = slow.next
            fast = fast.next.next
        
        
        if fast is not None:
            slow = slow.next

        while slow is not None:
            if slow.data != my_list.pop():
                return False
            slow = slow.next
        return True



